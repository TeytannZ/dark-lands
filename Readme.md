# 🌍 Dark Lands — Tunisia Rural Collapse Intelligence System

> **EcoWave 2.0 Hackathon** · IEEE FSS Student Branch · Sfax, Tunisia · 2025
> *Making Tunisia's Invisible Rural Collapse Visible from Space*

---

## 🔴 The Problem

Tunisia is experiencing a **silent rural crisis** that nobody can see with the naked eye:

- Farmlands across interior Tunisia are **dying and being abandoned**
- Rainfall has dropped **27.9% since 2019**
- Vegetation health hit an **all-time low in 2024**
- People are **fleeing to cities** — up to 28% population loss in some regions
- **9 out of 23 regions** are now in critical collapse

This is happening **invisibly** — no headlines, no visible disasters. Just a slow, satellite-detectable collapse.

---

## 💡 Our Solution

**Dark Lands** is a satellite-powered intelligence dashboard that:

- Pulls **real satellite data** from NASA, ESA, and NOAA
- Analyzes **10 years of trends** (2015–2025) across all of Tunisia
- Calculates a **Rural Vulnerability Score** per region using AI
- **Predicts** which areas will collapse next (2026–2028)
- Provides **actionable recommendations** for governments and NGOs
- Makes everything **understandable for non-technical decision makers**

---

## 🛰️ Data Sources

| Source | Data | Provider |
|--------|------|----------|
| Landsat 8 C2 | Vegetation Health (NDVI) | ESA / USGS |
| CHIRPS Pentad | Annual Rainfall | UCSB Climate Hazards Group |
| NOAA VIIRS DNB | Nighttime Lights (Migration Signal) | NASA / NOAA |
| Google Earth Engine | Processing Platform | Google |

---

## 🤖 AI Model

Our vulnerability model combines 3 satellite signals:

```
Vulnerability Score = (1 - NDVI) × 40% + (1 - Rainfall) × 35% + Nightlights × 25%
```

- **NDVI** → how much farmland is dying
- **Rainfall** → how severe the drought is
- **Nightlights** → how many people are fleeing to cities

Score range: **0 (safe) → 100 (critical collapse)**

---

## 📊 Expected Outputs

- ✅ Interactive maps & dashboards
- ✅ Satellite heatmaps (time-lapse animation)
- ✅ Environmental / agricultural KPIs
- ✅ AI prediction model (2026–2028 forecast)
- ✅ Regional vulnerability scoring
- ✅ Actionable recommendations aligned with UN SDGs

---

## 🗂️ Project Structure

```
darklands/
├── dashboard.py          # Main Streamlit dashboard
├── data_extraction.py    # Satellite data extraction via GEE
├── ai_model.py           # AI vulnerability model + predictions
├── config.py             # Configuration (GEE project, regions, datasets)
├── requirements.txt      # Python dependencies
├── data/
│   ├── tunisia_yearly_data.csv    # Raw satellite data
│   ├── tunisia_analysis.csv       # Processed + scored data
│   └── tunisia_predictions.csv    # AI predictions 2026-2028
└── charts/
    └── dark_lands_analysis.png    # Static analysis chart
```

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/TeytannZ/dark-lands.git
cd dark-lands
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Authenticate Google Earth Engine
```bash
python -c "import ee; ee.Authenticate()"
```

### 4. Run the dashboard
```bash
python -m streamlit run dashboard.py
```

---

## 🌐 Live Demo

👉 **[View Live Dashboard](https://teytannz-dark-lands.streamlit.app)**

---

## 🎯 UN SDGs Addressed

| SDG | How |
|-----|-----|
| SDG 2 — Zero Hunger | Monitors farmland collapse, supports food security decisions |
| SDG 6 — Clean Water | Tracks water stress and drought progression |
| SDG 7 — Clean Energy | Identifies solar potential in energy-poor regions |
| SDG 10 — Reduced Inequalities | Maps rural vs urban inequality gap |
| SDG 11 — Sustainable Cities | Monitors climate-driven urbanization |
| SDG 13 — Climate Action | Provides early warning system for climate impacts |

---

## 🏆 Hackathon

**EcoWave 2.0** — Make The Invisible Visible from Space
Organized by **IEEE FSS Student Branch**, Faculty of Sciences of Sfax
Theme: Humanitarian & Sustainable Solutions for Tunisia

---

## 👥 Team

Built with ❤️ for Tunisia · EcoWave 2.0 · 2025
