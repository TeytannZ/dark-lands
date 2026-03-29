# ============================================
# DARK LANDS - Configuration File
# ============================================

# Your GEE Project ID
GEE_PROJECT = 'dark-lands-123'  # Replace with yours

# Tunisia bounding box coordinates
TUNISIA_BBOX = {
    'west': 7.5,
    'south': 30.2,
    'east': 11.6,
    'north': 37.5
}

# Time range for analysis
START_YEAR = 2015
END_YEAR = 2025

# Key regions to monitor (interior/rural Tunisia)
REGIONS = {
    'Kasserine': [8.8, 35.1],
    'Sidi Bouzid': [9.5, 35.0],
    'Siliana': [9.4, 36.0],
    'Kairouan': [10.1, 35.7],
    'Gabes': [9.5, 33.8],
    'Kebili': [8.9, 33.7],
    'Tozeur': [8.1, 33.9],
    'Gafsa': [8.8, 34.4]
}

# Satellite datasets
DATASETS = {
    'NDVI': 'COPERNICUS/S2_SR_HARMONIZED',
    'RAINFALL': 'UCSB-CHG/CHIRPS/DAILY',
    'NIGHTLIGHTS': 'NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG',
    'SOIL_MOISTURE': 'NASA/SMAP/SPL3SMP_E/005'
}

print("Config loaded successfully!")
