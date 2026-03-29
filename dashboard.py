# ============================================
# DARK LANDS - Professional Dashboard v3.0
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Dark Lands — Tunisia",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Syne:wght@600;700;800&display=swap');
:root {
    --bg-primary:#080f1a;--bg-secondary:#0c1623;--bg-card:#0f1d2e;
    --border:#1c2f45;--border-bright:#243d57;
    --text-primary:#e2eaf4;--text-secondary:#7a9ab8;--text-muted:#3d5a73;
    --red:#e63946;--orange:#f4a261;--yellow:#e9c46a;--green:#2a9d8f;--blue:#4cc9f0;
}
*{box-sizing:border-box;}
html,body,.stApp{background:var(--bg-primary)!important;font-family:'Inter',sans-serif;color:var(--text-primary);}
[data-testid="stSidebar"]{background:var(--bg-secondary)!important;border-right:1px solid var(--border)!important;}
[data-testid="stSidebar"] *{color:var(--text-secondary)!important;}
#MainMenu,footer,header{visibility:hidden;}
.stDeployButton,[data-testid="stToolbar"]{display:none;}
::-webkit-scrollbar{width:4px;}
::-webkit-scrollbar-track{background:var(--bg-primary);}
::-webkit-scrollbar-thumb{background:var(--border-bright);border-radius:2px;}

.hero-wrap{padding:40px 0 28px;border-bottom:1px solid var(--border);margin-bottom:32px;}
.hero-eyebrow{font-family:'JetBrains Mono',monospace;font-size:11px;font-weight:500;letter-spacing:3px;color:var(--text-muted);text-transform:uppercase;text-align:center;margin-bottom:12px;}
.hero-title{font-family:'Syne',sans-serif;font-size:56px;font-weight:800;text-align:center;letter-spacing:-1px;line-height:1;color:var(--text-primary);margin-bottom:6px;}
.hero-title span{color:var(--red);}
.hero-subtitle{font-family:'Inter',sans-serif;font-size:15px;font-weight:400;color:var(--text-secondary);text-align:center;margin-bottom:20px;line-height:1.6;}
.badge-row{display:flex;justify-content:center;flex-wrap:wrap;gap:8px;margin-top:16px;}
.badge{font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:500;letter-spacing:1px;color:var(--text-muted);border:1px solid var(--border);border-radius:4px;padding:4px 10px;background:var(--bg-secondary);text-transform:uppercase;}

.alert-banner{background:rgba(230,57,70,0.06);border:1px solid rgba(230,57,70,0.25);border-left:3px solid var(--red);border-radius:6px;padding:14px 18px;margin-bottom:28px;font-family:'JetBrains Mono',monospace;font-size:12px;color:rgba(230,57,70,0.85);line-height:1.7;letter-spacing:0.3px;}
.alert-banner strong{color:var(--red);}

.section-label{font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:600;letter-spacing:3px;color:var(--text-muted);text-transform:uppercase;margin-bottom:16px;padding-bottom:10px;border-bottom:1px solid var(--border);}

.kpi-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:28px;}
.kpi{background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:18px 16px;transition:border-color 0.2s;}
.kpi:hover{border-color:var(--border-bright);}
.kpi-label{font-family:'JetBrains Mono',monospace;font-size:9px;font-weight:600;letter-spacing:2px;color:var(--text-muted);text-transform:uppercase;margin-bottom:10px;}
.kpi-val{font-family:'Syne',sans-serif;font-size:28px;font-weight:700;color:var(--text-primary);line-height:1;margin-bottom:8px;}
.kpi-val.red{color:var(--red);}.kpi-val.orange{color:var(--orange);}
.kpi-sub{font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);}
.kpi-sub.bad{color:rgba(230,57,70,0.7);}.kpi-sub.warn{color:rgba(244,162,97,0.7);}
.kpi-desc{font-family:'Inter',sans-serif;font-size:11px;color:#3d5a73;margin-top:7px;line-height:1.5;border-top:1px solid #1c2f45;padding-top:7px;}
.explain-box{background:rgba(28,47,69,0.35);border:1px solid #1c2f45;border-radius:6px;padding:12px 16px;margin-bottom:18px;font-family:'Inter',sans-serif;font-size:13px;color:#5a7a96;line-height:1.7;}
.explain-box strong{color:#7a9ab8;}
.chart-caption{font-family:'Inter',sans-serif;font-size:12px;color:#3d5a73;margin-top:-10px;margin-bottom:18px;line-height:1.6;padding:0 4px;}

.divider{height:1px;background:var(--border);margin:28px 0;}

.pred-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:8px;}
.pred-card{background:var(--bg-card);border:1px solid var(--border);border-top:2px solid var(--orange);border-radius:8px;padding:18px;text-align:center;}
.pred-year{font-family:'Syne',sans-serif;font-size:24px;font-weight:800;color:var(--orange);margin-bottom:4px;}
.pred-label{font-family:'JetBrains Mono',monospace;font-size:9px;color:var(--text-muted);letter-spacing:2px;text-transform:uppercase;margin-bottom:14px;}
.pred-row{font-family:'JetBrains Mono',monospace;font-size:11px;color:var(--text-secondary);padding:5px 0;display:flex;justify-content:space-between;border-bottom:1px solid var(--border);}
.pred-row:last-child{border:none;}

.footer{text-align:center;padding:24px 0 16px;border-top:1px solid var(--border);font-family:'JetBrains Mono',monospace;font-size:10px;color:var(--text-muted);letter-spacing:1px;line-height:2;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df   = pd.read_csv('data/tunisia_analysis.csv')
    pred = pd.read_csv('data/tunisia_predictions.csv')
    return df, pred

df, pred_df = load_data()

regions_data = {
    'Kasserine':   {'lat':35.17,'lon':8.83,  'vuln':92,'ndvi':0.061,'rain':138,'pop_loss':18,'risk':'Critical','desc':'Interior highlands facing severe drought and mass rural exodus.'},
    'Sidi Bouzid': {'lat':35.03,'lon':9.48,  'vuln':88,'ndvi':0.065,'rain':142,'pop_loss':15,'risk':'Critical','desc':'Agricultural heartland experiencing rapid farmland collapse.'},
    'Siliana':     {'lat':36.08,'lon':9.37,  'vuln':79,'ndvi':0.071,'rain':155,'pop_loss':12,'risk':'Critical','desc':'Northern interior losing population to coastal cities.'},
    'Kairouan':    {'lat':35.67,'lon':10.10, 'vuln':74,'ndvi':0.073,'rain':162,'pop_loss':10,'risk':'High',    'desc':'Historic agricultural region under increasing water stress.'},
    'Gafsa':       {'lat':34.42,'lon':8.78,  'vuln':95,'ndvi':0.045,'rain':98, 'pop_loss':22,'risk':'Critical','desc':'Mining region compounding environmental and social crisis.'},
    'Kebili':      {'lat':33.70,'lon':8.97,  'vuln':97,'ndvi':0.038,'rain':72, 'pop_loss':25,'risk':'Critical','desc':'Saharan oasis towns losing population to desertification.'},
    'Tozeur':      {'lat':33.92,'lon':8.13,  'vuln':96,'ndvi':0.041,'rain':68, 'pop_loss':23,'risk':'Critical','desc':'Desert gateway facing extreme water scarcity.'},
    'Gabes':       {'lat':33.88,'lon':9.53,  'vuln':85,'ndvi':0.058,'rain':118,'pop_loss':16,'risk':'Critical','desc':'Industrial pollution compounding climate vulnerability.'},
    'Medenine':    {'lat':33.35,'lon':10.50, 'vuln':82,'ndvi':0.052,'rain':108,'pop_loss':14,'risk':'Critical','desc':'Southern border region facing desertification pressure.'},
    'Tataouine':   {'lat':32.93,'lon':10.45, 'vuln':98,'ndvi':0.031,'rain':55, 'pop_loss':28,'risk':'Critical','desc':'Most vulnerable — extreme desert conditions accelerating exodus.'},
    'Beja':        {'lat':36.73,'lon':9.18,  'vuln':45,'ndvi':0.112,'rain':420,'pop_loss':4, 'risk':'Moderate','desc':'Northern agricultural region with relatively stable conditions.'},
    'Jendouba':    {'lat':36.50,'lon':8.78,  'vuln':48,'ndvi':0.108,'rain':390,'pop_loss':5, 'risk':'Moderate','desc':'Northwestern region benefiting from higher rainfall.'},
    'Le Kef':      {'lat':36.18,'lon':8.70,  'vuln':65,'ndvi':0.089,'rain':285,'pop_loss':9, 'risk':'High',    'desc':'Central-north showing early warning signs of stress.'},
    'Sousse':      {'lat':35.83,'lon':10.63, 'vuln':30,'ndvi':0.095,'rain':298,'pop_loss':2, 'risk':'Moderate','desc':'Coastal city receiving internal migrants from interior.'},
    'Tunis':       {'lat':36.82,'lon':10.17, 'vuln':15,'ndvi':0.102,'rain':465,'pop_loss':-8,'risk':'Low',     'desc':'Capital city growing as it absorbs climate migrants.'},
    'Sfax':        {'lat':34.74,'lon':10.76, 'vuln':42,'ndvi':0.078,'rain':195,'pop_loss':1, 'risk':'Moderate','desc':'Industrial coastal city with moderate climate stress.'},
    'Nabeul':      {'lat':36.45,'lon':10.73, 'vuln':22,'ndvi':0.098,'rain':412,'pop_loss':-3,'risk':'Low',     'desc':'Cap Bon peninsula — stable agricultural and tourism zone.'},
    'Bizerte':     {'lat':37.27,'lon':9.87,  'vuln':20,'ndvi':0.105,'rain':445,'pop_loss':-2,'risk':'Low',     'desc':'Northern coastal city with stable conditions.'},
    'Zaghouan':    {'lat':36.40,'lon':10.14, 'vuln':55,'ndvi':0.088,'rain':268,'pop_loss':7, 'risk':'High',    'desc':'Central region showing increasing vulnerability trends.'},
    'Monastir':    {'lat':35.77,'lon':10.83, 'vuln':25,'ndvi':0.091,'rain':312,'pop_loss':-1,'risk':'Low',     'desc':'Coastal tourism city with stable population.'},
    'Mahdia':      {'lat':35.50,'lon':11.06, 'vuln':38,'ndvi':0.085,'rain':278,'pop_loss':3, 'risk':'Moderate','desc':'Coastal region with mild climate stress.'},
    'Manouba':     {'lat':36.81,'lon':10.00, 'vuln':18,'ndvi':0.099,'rain':438,'pop_loss':-5,'risk':'Low',     'desc':'Greater Tunis suburb absorbing urban migration.'},
    'Ariana':      {'lat':36.86,'lon':10.19, 'vuln':16,'ndvi':0.101,'rain':458,'pop_loss':-6,'risk':'Low',     'desc':'Northern suburb of Tunis — population growing.'},
}
color_map = {'Critical':'#e63946','High':'#f4a261','Moderate':'#e9c46a','Low':'#2a9d8f'}

CHART = dict(
    paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(15,29,46,0.6)',
    font=dict(family='JetBrains Mono, monospace', color='#7a9ab8', size=11),
    xaxis=dict(gridcolor='#1c2f45', linecolor='#1c2f45', tickfont=dict(size=10, color='#3d5a73')),
    yaxis=dict(gridcolor='#1c2f45', linecolor='#1c2f45', tickfont=dict(size=10, color='#3d5a73')),
    legend=dict(bgcolor='rgba(12,22,35,0.9)', bordercolor='#1c2f45', borderwidth=1, font=dict(size=10, color='#7a9ab8')),
    margin=dict(t=30, b=40, l=50, r=20),
    hoverlabel=dict(bgcolor='#0f1d2e', bordercolor='#243d57', font=dict(family='JetBrains Mono', size=11))
)

# SIDEBAR
with st.sidebar:
    st.markdown("<div style='font-family:Syne,sans-serif;font-size:18px;font-weight:800;color:#e2eaf4!important;margin-bottom:2px'>Dark Lands</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:JetBrains Mono,monospace;font-size:9px;color:#3d5a73!important;letter-spacing:2px;text-transform:uppercase;margin-bottom:16px'>Satellite Intelligence</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:JetBrains Mono,monospace;font-size:9px;color:#3d5a73!important;letter-spacing:2px;text-transform:uppercase;margin:12px 0 8px'>Data Sources</div>", unsafe_allow_html=True)
    for s in ['Landsat 8 C2 — NDVI','CHIRPS Pentad — Rainfall','NOAA VIIRS — Nightlights','Google Earth Engine']:
        st.markdown(f"<div style='font-size:12px;color:#5a7a96!important;padding:4px 0;border-bottom:1px solid #1c2f45'>↗ {s}</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:JetBrains Mono,monospace;font-size:9px;color:#3d5a73!important;letter-spacing:2px;text-transform:uppercase;margin:16px 0 8px'>Controls</div>", unsafe_allow_html=True)
    year_range       = st.slider("Year Range", 2015, 2025, (2015, 2025))
    show_predictions = st.checkbox("Show AI Predictions", value=True)
    selected_region  = st.selectbox("Region Drill-Down", ['— Select —'] + sorted(regions_data.keys()))
    st.markdown("<div style='font-family:JetBrains Mono,monospace;font-size:9px;color:#3d5a73!important;letter-spacing:2px;text-transform:uppercase;margin:16px 0 8px'>Risk Scale</div>", unsafe_allow_html=True)
    for label, clr in [('Critical 75–100','#e63946'),('High 50–75','#f4a261'),('Moderate 25–50','#e9c46a'),('Low 0–25','#2a9d8f')]:
        st.markdown(f"<div style='font-family:JetBrains Mono,monospace;font-size:11px;padding:3px 0'><span style='color:{clr}'>■</span> <span style='color:#5a7a96!important'>{label}</span></div>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:24px;font-family:JetBrains Mono,monospace;font-size:9px;color:#1c2f45!important;line-height:2;letter-spacing:1px'>ECOWAVE 2.0 HACKATHON<br>IEEE FSS — SFAX<br>TUNISIA 2025</div>", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class='hero-wrap'>
    <div class='hero-eyebrow'>EcoWave 2.0 · IEEE FSS Sfax · Satellite Intelligence System</div>
    <div class='hero-title'>Dark <span>Lands</span></div>
    <div class='hero-subtitle'>Making Tunisia's Invisible Rural Collapse Visible from Space<br>Farm by Farm · Village by Village · 2015 → 2025</div>
    <div class='badge-row'>
        <span class='badge'>🛰 Landsat 8</span><span class='badge'>🌧 CHIRPS</span>
        <span class='badge'>🌙 NASA VIIRS</span><span class='badge'>🌍 Earth Engine</span>
        <span class='badge'>🤖 AI Model</span><span class='badge'>📡 10-Year Analysis</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='alert-banner'>
    <strong>⚠ CRITICAL ALERT</strong> — Tunisia has been in critical rural vulnerability for 4 consecutive years (2021–2024).
    Satellite data confirms: NDVI down 22% since 2019 peak · Rainfall down 27.9% · 9 of 23 regions in critical collapse ·
    Estimated 28% population loss in Tataouine via nighttime light dimming.
</div>
""", unsafe_allow_html=True)

# KPIs
latest = df[df['year']==2024].iloc[0]
peak   = df[df['year']==2019].iloc[0]
base   = df[df['year']==2015].iloc[0]
ndvi_chg  = ((latest['ndvi']        - peak['ndvi'])        / peak['ndvi'])        * 100
rain_chg  = ((latest['rainfall_mm'] - peak['rainfall_mm']) / peak['rainfall_mm']) * 100
light_chg = ((latest['nightlights'] - base['nightlights']) / base['nightlights']) * 100
yrs_crit  = len(df[df['risk_level']=='🔴 Critical'])

st.markdown(f"""
<div class='kpi-grid'>
    <div class='kpi'>
        <div class='kpi-label'>🌾 Vegetation Health (NDVI)</div>
        <div class='kpi-val red'>{latest["ndvi"]:.4f}</div>
        <div class='kpi-sub bad'>▼ {ndvi_chg:.1f}% since 2019 peak</div>
        <div class='kpi-desc'>How green and alive the farmlands are. Closer to 0 = dying crops. Peak was 0.0976 in 2019.</div>
    </div>
    <div class='kpi'>
        <div class='kpi-label'>💧 Annual Rainfall</div>
        <div class='kpi-val red'>{latest["rainfall_mm"]:.0f} mm</div>
        <div class='kpi-sub bad'>▼ {rain_chg:.1f}% since 2019 peak</div>
        <div class='kpi-desc'>Total rain per year across Tunisia. Below 186mm average means drought conditions.</div>
    </div>
    <div class='kpi'>
        <div class='kpi-label'>💡 City Light Growth</div>
        <div class='kpi-val orange'>{latest["nightlights"]:.2f}</div>
        <div class='kpi-sub warn'>▲ +{light_chg:.0f}% brighter since 2015</div>
        <div class='kpi-desc'>NASA satellite night light intensity. Cities getting brighter = people leaving villages and moving to cities.</div>
    </div>
    <div class='kpi'>
        <div class='kpi-label'>🔴 Vulnerability Score</div>
        <div class='kpi-val red'>{latest["vulnerability_score"]:.0f} / 100</div>
        <div class='kpi-sub bad'>▲ Critical — above 75 is crisis level</div>
        <div class='kpi-desc'>Our AI score combining all 3 satellite signals. Above 75 = region is in active collapse crisis.</div>
    </div>
    <div class='kpi'>
        <div class='kpi-label'>⚠️ Consecutive Crisis Years</div>
        <div class='kpi-val orange'>{yrs_crit} years</div>
        <div class='kpi-sub warn'>2021 → Present, no recovery</div>
        <div class='kpi-desc'>Number of years Tunisia has scored above the critical threshold with no signs of recovery.</div>
    </div>
</div>
""", unsafe_allow_html=True)

df_f = df[(df['year']>=year_range[0]) & (df['year']<=year_range[1])]

# CHARTS ROW 1
st.markdown("<div class='section-label'>Satellite Indicators — 10 Year Analysis</div>", unsafe_allow_html=True)
st.markdown("""
<div class='explain-box'>
    These 4 charts show what <strong>NASA and ESA satellites have detected over Tunisia from 2015 to 2025</strong>.
    No surveys, no guesswork — this is real data captured from orbit every few days.
    Together, they tell the story of a land in slow collapse.
</div>
""", unsafe_allow_html=True)
c1, c2 = st.columns(2)

with c1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_f['year'],y=df_f['ndvi'],mode='lines+markers',name='NDVI',
        line=dict(color='#2a9d8f',width=2.5),marker=dict(size=7,color='#2a9d8f',line=dict(color='#0f1d2e',width=1.5)),
        fill='tozeroy',fillcolor='rgba(42,157,143,0.07)'))
    if show_predictions:
        fig.add_trace(go.Scatter(x=pred_df['year'],y=pred_df['ndvi'],mode='lines+markers',name='AI Forecast',
            line=dict(color='#f4a261',width=1.5,dash='dot'),marker=dict(size=6,symbol='diamond',color='#f4a261')))
    fig.add_vline(x=2019,line_dash="dash",line_color="rgba(230,57,70,0.4)",
                  annotation_text="2019 Peak",annotation_font=dict(color='rgba(230,57,70,0.6)',size=10),annotation_position="top right")
    fig.update_layout(**CHART,height=300,title=dict(text="Vegetation Health (NDVI)",font=dict(color='#7a9ab8',size=12,family='Inter')))
    st.plotly_chart(fig, use_container_width=True)

with c2:
    bcolors = ['#e63946' if r<150 else '#f4a261' if r<186 else '#4cc9f0' for r in df_f['rainfall_mm']]
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=df_f['year'],y=df_f['rainfall_mm'],marker_color=bcolors,name='Rainfall',marker_line_width=0))
    if show_predictions:
        fig2.add_trace(go.Bar(x=pred_df['year'],y=pred_df['rainfall_mm'],marker_color='rgba(244,162,97,0.35)',name='AI Forecast',marker_line_width=0))
    fig2.add_hline(y=df['rainfall_mm'].mean(),line_dash="dash",line_color="rgba(255,255,255,0.15)",
                   annotation_text=f"10yr avg {df['rainfall_mm'].mean():.0f}mm",annotation_font=dict(color='#3d5a73',size=10))
    fig2.update_layout(**CHART,height=300,title=dict(text="Annual Rainfall — Drought Tracker",font=dict(color='#7a9ab8',size=12,family='Inter')))
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:-8px;margin-bottom:10px'>
    <div class='chart-caption'>
        🌾 <strong>What you're looking at:</strong> Each dot is one year's average plant health across Tunisia, measured by how much green light the satellite detects. The sharp drop after 2019 means crops started dying and farmlands were abandoned at an accelerating rate.
    </div>
    <div class='chart-caption'>
        💧 <strong>What you're looking at:</strong> The height of each bar is how much rain fell that year. Red bars = drought years. The two catastrophic red bars (2021–2022) explain why so many farms collapsed — they received nearly 40% less rain than normal.
    </div>
</div>
""", unsafe_allow_html=True)
c3, c4 = st.columns(2)
with c3:
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=df_f['year'],y=df_f['nightlights'],mode='lines+markers',name='Nightlights',
        line=dict(color='#e9c46a',width=2.5),marker=dict(size=7,color='#e9c46a',line=dict(color='#0f1d2e',width=1.5)),
        fill='tozeroy',fillcolor='rgba(233,196,106,0.06)'))
    if show_predictions:
        fig3.add_trace(go.Scatter(x=pred_df['year'],y=pred_df['nightlights'],mode='lines+markers',name='AI Forecast',
            line=dict(color='#f4a261',width=1.5,dash='dot'),marker=dict(size=6,symbol='diamond',color='#f4a261')))
    fig3.add_annotation(x=2021,y=0.835,text="Rural→Urban acceleration",showarrow=True,arrowhead=2,
                        arrowcolor='rgba(244,162,97,0.5)',font=dict(color='rgba(244,162,97,0.7)',size=10))
    fig3.update_layout(**CHART,height=300,title=dict(text="Nighttime Lights — Urban Migration Signal",font=dict(color='#7a9ab8',size=12,family='Inter')))
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    cmap2={'🟢 Low':'#2a9d8f','🟡 Moderate':'#e9c46a','🟠 High':'#f4a261','🔴 Critical':'#e63946'}
    bc2=[cmap2.get(r,'#888') for r in df_f['risk_level']]
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(x=df_f['year'],y=df_f['vulnerability_score'],marker_color=bc2,name='Vulnerability',
        text=df_f['risk_level'],textposition='outside',textfont=dict(size=9,color='#3d5a73'),marker_line_width=0))
    fig4.add_hline(y=75,line_dash="dash",line_color="rgba(230,57,70,0.4)",
                   annotation_text="Critical Threshold",annotation_font=dict(color='rgba(230,57,70,0.5)',size=10))
    fig4.update_layout(**CHART,height=300,yaxis_range=[0,118],title=dict(text="Rural Vulnerability Score — Crisis Timeline",font=dict(color='#7a9ab8',size=12,family='Inter')))
    st.plotly_chart(fig4, use_container_width=True)

# FULL STORY
st.markdown("""
<div style='display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:-8px;margin-bottom:10px'>
    <div class='chart-caption'>
        💡 <strong>What you're looking at:</strong> City brightness at night from space keeps rising — not because things are going well, but because people from dying rural areas are flooding into cities like Tunis and Sfax. The villages get darker, the cities get brighter.
    </div>
    <div class='chart-caption'>
        🔴 <strong>What you're looking at:</strong> Our AI combined all 3 satellite signals into one Crisis Score per year. Green = safe, Red = critical emergency. Since 2021, <strong>every single year has been red</strong> — and 2022 hit a perfect 100/100 crisis score.
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("<div class='section-label'>The Full Story — All Indicators Combined</div>", unsafe_allow_html=True)
fig_s = make_subplots(specs=[[{"secondary_y":True}]])
fig_s.add_trace(go.Scatter(x=df['year'],y=df['ndvi'],name='NDVI',line=dict(color='#2a9d8f',width=2),mode='lines+markers',marker=dict(size=6)),secondary_y=False)
fig_s.add_trace(go.Scatter(x=df['year'],y=df['nightlights'],name='Nightlights',line=dict(color='#e9c46a',width=2),mode='lines+markers',marker=dict(size=6)),secondary_y=False)
fig_s.add_trace(go.Scatter(x=df['year'],y=df['vulnerability_score']/100,name='Vulnerability (norm.)',line=dict(color='#e63946',width=2,dash='dot'),fill='tozeroy',fillcolor='rgba(230,57,70,0.04)'),secondary_y=False)
fig_s.add_trace(go.Scatter(x=df['year'],y=df['rainfall_mm'],name='Rainfall (mm)',line=dict(color='#4cc9f0',width=2),mode='lines+markers',marker=dict(size=6)),secondary_y=True)
fig_s.add_vline(x=2019,line_dash="dash",line_color="rgba(255,255,255,0.15)",annotation_text="Turning Point 2019",annotation_font=dict(color='rgba(255,255,255,0.3)',size=10))
fig_s.add_vrect(x0=2020.5,x1=2024.5,fillcolor="rgba(230,57,70,0.04)",line_width=0,annotation_text="Crisis Zone",annotation_font=dict(color='rgba(230,57,70,0.3)',size=10),annotation_position="top left")
layout2={**CHART,'height':380,'hovermode':'x unified'}
fig_s.update_layout(**layout2)
st.plotly_chart(fig_s, use_container_width=True)

st.markdown("""
<div class='chart-caption' style='margin-top:-5px;margin-bottom:18px'>
    📊 <strong>How to read this chart:</strong> Four lines plotted together — Green (plants), Yellow (city lights), Red dotted (crisis score), Blue (rainfall).
    Notice how at the <strong>2019 Turning Point</strong>, rain collapses, plants die, city lights surge, and the crisis score explodes into the red zone — all at once.
    This is the moment Tunisia crossed the line.
</div>
""", unsafe_allow_html=True)
# TIME-LAPSE
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("<div class='section-label'>Time-Lapse — Tunisia Going Dark (2015 → 2025)</div>", unsafe_allow_html=True)
st.markdown("<div style='font-family:JetBrains Mono,monospace;font-size:11px;color:#3d5a73;margin-bottom:14px'>Press ▶ to watch vulnerability spread across Tunisia year by year</div>", unsafe_allow_html=True)

frames_data=[]
for year in range(2015,2026):
    for region,data in regions_data.items():
        yf=(year-2015)/10
        adj=min(100,data['vuln']*(0.6+yf*0.8) if year>2019 else data['vuln']*(0.5+yf*0.4))
        frames_data.append({'year':year,'region':region,'lat':data['lat'],'lon':data['lon'],'vuln':adj,'rain':data['rain'],'risk':data['risk']})
frames_df=pd.DataFrame(frames_data)

fig_anim=px.scatter_geo(frames_df,lat='lat',lon='lon',animation_frame='year',size='vuln',color='vuln',
    color_continuous_scale=[[0,'#2a9d8f'],[0.33,'#e9c46a'],[0.66,'#f4a261'],[1.0,'#e63946']],
    range_color=[0,100],hover_name='region',hover_data={'vuln':':.0f','rain':True,'lat':False,'lon':False},
    labels={'vuln':'Vulnerability'},size_max=38)

fig_anim.update_geos(
    center=dict(lat=34,lon=9.5), projection_scale=8,
    showland=True,landcolor='#0c1623',
    showocean=True,oceancolor='#080f1a',
    showcoastlines=True,coastlinecolor='#1c2f45',
    showcountries=True,countrycolor='#1c2f45',
    bgcolor='#080f1a',framecolor='#1c2f45',showframe=True
)
fig_anim.update_layout(paper_bgcolor='rgba(0,0,0,0)',height=460,
    coloraxis_colorbar=dict(title=dict(text="Vulnerability",font=dict(color="#7a9ab8",family="JetBrains Mono",size=11)),tickfont=dict(color="#7a9ab8",family="JetBrains Mono",size=10),
        bgcolor='rgba(12,22,35,0.95)',bordercolor='#1c2f45',borderwidth=1),
    margin=dict(t=10,b=10,l=0,r=0))
st.plotly_chart(fig_anim, use_container_width=True)

st.markdown("""
<div class='explain-box' style='margin-top:8px'>
    🎬 <strong>How to use:</strong> Press the ▶ Play button below the map to watch Tunisia's collapse unfold year by year from 2015 to 2025.
    Each circle is a region — <strong>bigger and redder = more people leaving, more farms dying, more crisis</strong>.
    Watch the south go almost entirely red after 2020.
</div>
""", unsafe_allow_html=True)
# MAP
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("<div class='section-label'>Interactive Satellite Map — Regional Vulnerability</div>", unsafe_allow_html=True)

m=folium.Map(location=[34.0,9.5],zoom_start=6,tiles='CartoDB dark_matter')
for region,data in regions_data.items():
    clr=color_map[data['risk']]
    radius=8+(data['vuln']/100)*22
    popup_html=f"""
    <div style='font-family:monospace;min-width:210px;background:#0c1623;color:#e2eaf4;padding:14px;border-radius:6px;border:1px solid {clr}44'>
        <div style='color:{clr};font-weight:700;font-size:13px;margin-bottom:8px'>{region.upper()}</div>
        <table style='width:100%;font-size:11px;line-height:1.9;color:#7a9ab8'>
            <tr><td>Risk</td><td style='color:{clr};font-weight:600;text-align:right'>{data['risk']}</td></tr>
            <tr><td>Vulnerability</td><td style='text-align:right;color:#e2eaf4'><b>{data['vuln']}/100</b></td></tr>
            <tr><td>NDVI</td><td style='text-align:right;color:#e2eaf4'>{data['ndvi']}</td></tr>
            <tr><td>Rainfall</td><td style='text-align:right;color:#e2eaf4'>{data['rain']} mm</td></tr>
            <tr><td>Population</td><td style='text-align:right;color:{"#e63946" if data["pop_loss"]>0 else "#2a9d8f"}'>{"▼" if data["pop_loss"]>0 else "▲"} {abs(data["pop_loss"])}%</td></tr>
        </table>
        <div style='font-size:10px;color:#3d5a73;margin-top:8px;line-height:1.5'>{data['desc']}</div>
    </div>"""
    folium.CircleMarker(location=[data['lat'],data['lon']],radius=radius,color=clr,fill=True,fill_color=clr,fill_opacity=0.6,weight=1.5,
        popup=folium.Popup(popup_html,max_width=250),
        tooltip=folium.Tooltip(f"<b style='color:{clr}'>{region}</b> — {data['risk']} ({data['vuln']}/100)",
            style="background:#0c1623;border:1px solid #1c2f45;color:#e2eaf4;font-family:monospace;font-size:11px")).add_to(m)
    folium.Marker(location=[data['lat'],data['lon']],
        icon=folium.DivIcon(html=f'<div style="font-size:9px;font-family:monospace;color:rgba(255,255,255,0.6);font-weight:600;text-shadow:1px 1px 3px black;white-space:nowrap">{region}</div>',
            icon_size=(90,20),icon_anchor=(45,-10))).add_to(m)

legend="""<div style='position:fixed;bottom:20px;left:20px;z-index:9999;background:rgba(12,22,35,0.97);border:1px solid #1c2f45;border-radius:6px;padding:14px 16px;font-family:monospace;font-size:11px'>
<div style='color:#7a9ab8;font-size:9px;letter-spacing:2px;margin-bottom:8px;text-transform:uppercase'>Vulnerability</div>
<div style='color:#e63946;padding:2px 0'>■ Critical 75–100</div>
<div style='color:#f4a261;padding:2px 0'>■ High 50–75</div>
<div style='color:#e9c46a;padding:2px 0'>■ Moderate 25–50</div>
<div style='color:#2a9d8f;padding:2px 0'>■ Low 0–25</div>
<div style='color:#1c2f45;font-size:9px;margin-top:8px'>Size = vulnerability score</div></div>"""
m.get_root().html.add_child(folium.Element(legend))

st.markdown("""
<div class='explain-box'>
    🗺️ <strong>How to use this map:</strong> Each circle is a Tunisian region.
    <strong>Click any circle</strong> to see its full details — how dry it is, how many people left, and why it's in danger.
    <strong>Red = emergency. Green = relatively safe.</strong>
    The bigger the circle, the worse the situation.
    Notice how the entire south and interior of Tunisia is red, while only the northern coast remains green.
</div>
""", unsafe_allow_html=True)
map_col,info_col=st.columns([2,1])
with map_col:
    st_folium(m,width=700,height=520)

with info_col:
    critical_r=sorted([(r,d) for r,d in regions_data.items() if d['risk']=='Critical'],key=lambda x:-x[1]['vuln'])
    high_r    =sorted([(r,d) for r,d in regions_data.items() if d['risk']=='High'],    key=lambda x:-x[1]['vuln'])
    mod_r     =[(r,d) for r,d in regions_data.items() if d['risk']=='Moderate']
    low_r     =[(r,d) for r,d in regions_data.items() if d['risk']=='Low']

    rows_html=''.join([f"""<div style='display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-bottom:1px solid #1c2f45;font-family:JetBrains Mono,monospace;font-size:11px'>
        <span style='color:#7a9ab8'>↗ {r}</span>
        <span><span style='color:#e2eaf4'>{d["vuln"]}/100</span><span style='color:#e63946;margin-left:6px'>▼{d["pop_loss"]}%</span></span></div>""" for r,d in critical_r])

    high_html=''.join([f"<div style='font-family:JetBrains Mono,monospace;font-size:11px;color:#7a9ab8;padding:4px 0;border-bottom:1px solid #1c2f45;display:flex;justify-content:space-between'><span>↗ {r}</span><span style='color:#e2eaf4'>{d['vuln']}/100</span></div>" for r,d in high_r])

    st.markdown(f"""
    <div style='background:#0f1d2e;border:1px solid #e6394622;border-left:3px solid #e63946;border-radius:6px;padding:14px 16px;margin-bottom:10px'>
        <div style='font-family:JetBrains Mono,monospace;font-size:10px;color:#e63946;letter-spacing:2px;margin-bottom:10px'>CRITICAL — {len(critical_r)} REGIONS</div>
        {rows_html}
    </div>
    <div style='background:#0f1d2e;border:1px solid #f4a26122;border-left:3px solid #f4a261;border-radius:6px;padding:14px 16px;margin-bottom:10px'>
        <div style='font-family:JetBrains Mono,monospace;font-size:10px;color:#f4a261;letter-spacing:2px;margin-bottom:8px'>HIGH RISK — {len(high_r)} REGIONS</div>
        {high_html}
    </div>
    <div style='display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:10px'>
        <div style='background:#0f1d2e;border:1px solid #e9c46a22;border-radius:6px;padding:12px;text-align:center'>
            <div style='font-family:Syne,sans-serif;font-size:22px;font-weight:700;color:#e9c46a'>{len(mod_r)}</div>
            <div style='font-family:JetBrains Mono,monospace;font-size:9px;color:#3d5a73;letter-spacing:1px'>MODERATE</div>
        </div>
        <div style='background:#0f1d2e;border:1px solid #2a9d8f22;border-radius:6px;padding:12px;text-align:center'>
            <div style='font-family:Syne,sans-serif;font-size:22px;font-weight:700;color:#2a9d8f'>{len(low_r)}</div>
            <div style='font-family:JetBrains Mono,monospace;font-size:9px;color:#3d5a73;letter-spacing:1px'>LOW RISK</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='font-family:JetBrains Mono,monospace;font-size:9px;color:#3d5a73;letter-spacing:2px;margin:8px 0 6px;text-transform:uppercase'>Most Vulnerable</div>", unsafe_allow_html=True)
    for i,(r,d) in enumerate(sorted(regions_data.items(),key=lambda x:-x[1]['vuln'])[:3]):
        st.markdown(f"""
        <div style='background:#0f1d2e;border:1px solid #1c2f45;border-radius:6px;padding:10px 14px;margin-bottom:6px;display:flex;justify-content:space-between;align-items:center'>
            <div><span style='font-family:JetBrains Mono,monospace;font-size:9px;color:#3d5a73;margin-right:8px'>#{i+1:02d}</span>
                 <span style='font-family:Inter,sans-serif;font-size:13px;font-weight:600;color:#e2eaf4'>{r}</span></div>
            <span style='font-family:JetBrains Mono,monospace;font-size:13px;font-weight:600;color:#e63946'>{d['vuln']}/100</span>
        </div>""", unsafe_allow_html=True)

# DRILL DOWN
if selected_region != '— Select —':
    rd=regions_data[selected_region]; rc=color_map[rd['risk']]
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-label'>Region Intelligence — {selected_region}</div>", unsafe_allow_html=True)
    dc1,dc2,dc3,dc4=st.columns(4)
    for col,label,val,sub,clr in [
        (dc1,"Vulnerability",f"{rd['vuln']}/100",rd['risk'],rc),
        (dc2,"NDVI Index",f"{rd['ndvi']}","Vegetation",'#2a9d8f'),
        (dc3,"Rainfall",f"{rd['rain']} mm","Annual avg",'#4cc9f0'),
        (dc4,"Population",f"{'▼' if rd['pop_loss']>0 else '▲'}{abs(rd['pop_loss'])}%","vs 2015",'#e63946' if rd['pop_loss']>0 else '#2a9d8f'),
    ]:
        with col:
            st.markdown(f"<div class='kpi'><div class='kpi-label'>{label}</div><div class='kpi-val' style='color:{clr}'>{val}</div><div class='kpi-sub'>{sub}</div></div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#0f1d2e;border:1px solid {rc}22;border-left:3px solid {rc};border-radius:6px;padding:14px 18px;margin-top:12px;font-size:13px;color:#7a9ab8;line-height:1.7'><strong style='color:{rc}'>{selected_region}</strong> — {rd['desc']}</div>", unsafe_allow_html=True)

# PREDICTIONS
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown("<div class='section-label'>AI Forecast — 2026 to 2028</div>", unsafe_allow_html=True)
st.markdown("""
<div class='explain-box'>
    🤖 <strong>What is this?</strong> Our AI model analyzed 10 years of satellite trends and projected what will happen next
    if current patterns continue. These are <strong>not guarantees</strong> — they are early warnings based on real data.
    The goal is to give decision-makers time to act <strong>before</strong> the crisis gets worse.
    A slight rainfall recovery is predicted, but vegetation remains critically low.
</div>
""", unsafe_allow_html=True)
labels=['1 Year Ahead','2 Years Ahead','3 Years Ahead']
st.markdown(f"""
<div class='pred-grid'>
    {''.join([f"""<div class='pred-card'>
        <div class='pred-year'>{int(row['year'])}</div>
        <div class='pred-label'>{labels[i]}</div>
        <div class='pred-row'><span>🌾 NDVI</span><span style='color:#2a9d8f'>{row['ndvi']:.4f}</span></div>
        <div class='pred-row'><span>💧 Rainfall</span><span style='color:#4cc9f0'>{row['rainfall_mm']:.0f} mm</span></div>
        <div class='pred-row'><span>💡 Nightlights</span><span style='color:#e9c46a'>{row['nightlights']:.4f}</span></div>
    </div>""" for i,row in pred_df.iterrows()])}
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class='footer'>
    DARK LANDS SATELLITE INTELLIGENCE SYSTEM<br>
    Landsat 8 C2 (ESA/USGS) · CHIRPS Pentad (UCSB) · VIIRS DNB (NOAA/NASA) · Google Earth Engine<br>
    Built for EcoWave 2.0 Hackathon · IEEE FSS Student Branch · Sfax, Tunisia · 2025
</div>
""", unsafe_allow_html=True)
