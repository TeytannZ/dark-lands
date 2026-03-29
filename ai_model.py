# ============================================
# DARK LANDS - AI Vulnerability Model
# ============================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import os

# ============================================
# LOAD DATA
# ============================================
df = pd.read_csv('data/tunisia_yearly_data.csv')
print("✅ Data loaded")
print(df)

# ============================================
# FEATURE ENGINEERING
# ============================================

# Normalize all indicators (0 to 1)
scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[['ndvi', 'rainfall_mm', 'nightlights']] = scaler.fit_transform(
    df[['ndvi', 'rainfall_mm', 'nightlights']]
)

# Vulnerability Score Formula:
# High vulnerability = low NDVI + low rainfall + high nightlights (people fleeing to cities)
df['vulnerability_score'] = (
    (1 - df_scaled['ndvi']) * 0.40 +        # 40% weight — farmland death
    (1 - df_scaled['rainfall_mm']) * 0.35 + # 35% weight — drought
    df_scaled['nightlights'] * 0.25          # 25% weight — urban migration signal
)

# Normalize vulnerability score to 0-100
df['vulnerability_score'] = (
    (df['vulnerability_score'] - df['vulnerability_score'].min()) /
    (df['vulnerability_score'].max() - df['vulnerability_score'].min())
) * 100

# Risk classification
def classify_risk(score):
    if score >= 75:
        return '🔴 Critical'
    elif score >= 50:
        return '🟠 High'
    elif score >= 25:
        return '🟡 Moderate'
    else:
        return '🟢 Low'

df['risk_level'] = df['vulnerability_score'].apply(classify_risk)

# ============================================
# TREND ANALYSIS
# ============================================
df['ndvi_change'] = df['ndvi'].pct_change() * 100
df['rainfall_change'] = df['rainfall_mm'].pct_change() * 100
df['lights_change'] = df['nightlights'].pct_change() * 100

# ============================================
# PREDICTION — Next 3 Years (2026-2028)
# ============================================
def predict_next_years(df, years_ahead=3):
    predictions = []
    last_row = df.iloc[-1]

    # Calculate average trends from last 5 years
    last5 = df.tail(5)
    ndvi_trend = last5['ndvi'].diff().mean()
    rain_trend = last5['rainfall_mm'].diff().mean()
    lights_trend = last5['nightlights'].diff().mean()

    for i in range(1, years_ahead + 1):
        pred_year = int(last_row['year']) + i
        pred_ndvi = max(0, last_row['ndvi'] + (ndvi_trend * i))
        pred_rain = max(0, last_row['rainfall_mm'] + (rain_trend * i))
        pred_lights = last_row['nightlights'] + (lights_trend * i)

        predictions.append({
            'year': pred_year,
            'ndvi': round(pred_ndvi, 4),
            'rainfall_mm': round(pred_rain, 2),
            'nightlights': round(pred_lights, 4),
            'predicted': True
        })

    return pd.DataFrame(predictions)

pred_df = predict_next_years(df)

# ============================================
# SAVE RESULTS
# ============================================
os.makedirs('data', exist_ok=True)
df.to_csv('data/tunisia_analysis.csv', index=False)
pred_df.to_csv('data/tunisia_predictions.csv', index=False)

# ============================================
# VISUALIZE
# ============================================
os.makedirs('charts', exist_ok=True)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('🌍 DARK LANDS — Tunisia Rural Collapse Analysis',
             fontsize=16, fontweight='bold', color='darkred')

# 1. NDVI over time
axes[0,0].plot(df['year'], df['ndvi'], 'g-o', linewidth=2, markersize=6)
axes[0,0].fill_between(df['year'], df['ndvi'], alpha=0.3, color='green')
axes[0,0].set_title('🌾 Vegetation Health (NDVI)', fontweight='bold')
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('NDVI Index')
axes[0,0].axvline(x=2019, color='red', linestyle='--', alpha=0.7, label='Peak 2019')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)

# 2. Rainfall over time
axes[0,1].bar(df['year'], df['rainfall_mm'], color='steelblue', alpha=0.8)
axes[0,1].set_title('💧 Annual Rainfall (mm)', fontweight='bold')
axes[0,1].set_xlabel('Year')
axes[0,1].set_ylabel('Rainfall (mm)')
axes[0,1].axhline(y=df['rainfall_mm'].mean(), color='red',
                   linestyle='--', label=f"Avg: {df['rainfall_mm'].mean():.0f}mm")
axes[0,1].legend()
axes[0,1].grid(True, alpha=0.3)

# 3. Nightlights over time
axes[1,0].plot(df['year'], df['nightlights'], 'y-o', linewidth=2,
               markersize=6, color='orange')
axes[1,0].fill_between(df['year'], df['nightlights'], alpha=0.3, color='orange')
axes[1,0].set_title('💡 Nighttime Lights (Urban Migration Signal)', fontweight='bold')
axes[1,0].set_xlabel('Year')
axes[1,0].set_ylabel('Light Radiance')
axes[1,0].grid(True, alpha=0.3)

# 4. Vulnerability Score
colors = ['green' if s < 25 else 'yellow' if s < 50
          else 'orange' if s < 75 else 'red'
          for s in df['vulnerability_score']]
axes[1,1].bar(df['year'], df['vulnerability_score'], color=colors, alpha=0.85)
axes[1,1].set_title('🔴 Rural Vulnerability Score', fontweight='bold')
axes[1,1].set_xlabel('Year')
axes[1,1].set_ylabel('Score (0-100)')
axes[1,1].axhline(y=75, color='red', linestyle='--', alpha=0.7, label='Critical threshold')
axes[1,1].legend()
axes[1,1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('charts/dark_lands_analysis.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n✅ Charts saved to charts/dark_lands_analysis.png")

# ============================================
# PRINT SUMMARY
# ============================================
print("\n" + "="*50)
print("📊 DARK LANDS — ANALYSIS SUMMARY")
print("="*50)
print(df[['year', 'ndvi', 'rainfall_mm', 'nightlights',
          'vulnerability_score', 'risk_level']].to_string(index=False))
print("\n🔮 PREDICTIONS (2026-2028):")
print(pred_df[['year', 'ndvi', 'rainfall_mm', 'nightlights']].to_string(index=False))
print("="*50)

