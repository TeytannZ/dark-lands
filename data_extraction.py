# ============================================
# DARK LANDS - Data Extraction (Lightweight)
# ============================================

import ee
import pandas as pd
import os
import time
from config import GEE_PROJECT, TUNISIA_BBOX, START_YEAR, END_YEAR

ee.Initialize(project=GEE_PROJECT)
print("✅ GEE Initialized")

tunisia = ee.Geometry.Rectangle([
    TUNISIA_BBOX['west'],
    TUNISIA_BBOX['south'],
    TUNISIA_BBOX['east'],
    TUNISIA_BBOX['north']
])

save_path = 'data/tunisia_yearly_data.csv'
os.makedirs('data', exist_ok=True)

# ============================================
# SAFE FETCH
# ============================================
def safe_fetch(func, retries=3):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f"  ⚠️ Retry {attempt+1}: {e}")
            time.sleep(10)
    return None

# ============================================
# NDVI — Landsat 8 (lighter than Sentinel-2)
# ============================================
def get_ndvi(year):
    def fetch():
        img = (ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
            .filterBounds(tunisia)
            .filterDate(f'{year}-05-01', f'{year}-08-31')
            .filter(ee.Filter.lt('CLOUD_COVER', 30))
            .select(['SR_B5', 'SR_B4'])
            .median())
        ndvi = img.normalizedDifference(['SR_B5', 'SR_B4'])
        result = ndvi.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=tunisia,
            scale=10000,
            maxPixels=1e7,
            bestEffort=True
        )
        return result.getInfo().get('nd', None)
    return safe_fetch(fetch)

# ============================================
# RAINFALL — CHIRPS
# ============================================
def get_rainfall(year):
    def fetch():
        img = (ee.ImageCollection('UCSB-CHG/CHIRPS/PENTAD')
            .filterBounds(tunisia)
            .filterDate(f'{year}-01-01', f'{year}-12-31')
            .sum())
        result = img.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=tunisia,
            scale=10000,
            maxPixels=1e7,
            bestEffort=True
        )
        return result.getInfo().get('precipitation', None)
    return safe_fetch(fetch)

# ============================================
# NIGHTLIGHTS — VIIRS
# ============================================
def get_nightlights(year):
    def fetch():
        img = (ee.ImageCollection('NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG')
            .filterBounds(tunisia)
            .filterDate(f'{year}-01-01', f'{year}-12-31')
            .select('avg_rad')
            .mean())
        result = img.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=tunisia,
            scale=10000,
            maxPixels=1e7,
            bestEffort=True
        )
        return result.getInfo().get('avg_rad', None)
    return safe_fetch(fetch)

# ============================================
# MAIN
# ============================================
def extract_all_data():
    # Load existing
    if os.path.exists(save_path):
        df_existing = pd.read_csv(save_path)
        done_years = df_existing['year'].tolist()
        records = df_existing.to_dict('records')
        print(f"📂 Already have: {done_years}")
    else:
        records = []
        done_years = []

    for year in range(START_YEAR, END_YEAR + 1):
        if year in done_years:
            print(f"⏭️ Skip {year}")
            continue

        print(f"\n📡 Extracting {year}...")

        ndvi        = get_ndvi(year)
        rainfall    = get_rainfall(year)
        nightlights = get_nightlights(year)

        record = {
            'year':         year,
            'ndvi':         round(ndvi, 4)        if ndvi        else None,
            'rainfall_mm':  round(rainfall, 2)    if rainfall    else None,
            'nightlights':  round(nightlights, 4) if nightlights else None
        }
        records.append(record)
        pd.DataFrame(records).to_csv(save_path, index=False)
        print(f"  ✅ NDVI: {record['ndvi']} | Rain: {record['rainfall_mm']} | Lights: {record['nightlights']} 💾")

        # Small pause between years to avoid rate limiting
        time.sleep(3)

    df = pd.DataFrame(records)
    print("\n✅ Done!")
    print(df)
    return df

if __name__ == '__main__':
    extract_all_data()
