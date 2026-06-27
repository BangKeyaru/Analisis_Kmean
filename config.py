# =============================================================================
# config.py – Konstanta Global & Styling
# =============================================================================

# ---------------------------------------------------------------------------
# Kolom fitur yang digunakan dalam pemodelan
# ---------------------------------------------------------------------------
FEATURES = [
    "Gold_Price_XAU_USD",
    "US_Dollar_Index_DXY",
    "Crude_Oil_Price",
    "Inflation_Rate_Pct",
]

# ---------------------------------------------------------------------------
# Label, warna, dan ikon setiap cluster
# ---------------------------------------------------------------------------
CLUSTER_LABELS = {
    0: "Safe Haven Penuh – Inflasi Tinggi",
    1: "Penguatan Emas Tanpa Tekanan Inflasi",
    2: "Dominasi Dolar AS",
}

CLUSTER_COLORS = {
    0: "#FFD700",
    1: "#00C9A7",
    2: "#E84393",
}

CLUSTER_ICONS = {
    0: "🔴",
    1: "🟢",
    2: "🔵",
}

# ---------------------------------------------------------------------------
# Deskripsi naratif setiap cluster (untuk kartu penjelasan)
# ---------------------------------------------------------------------------
CLUSTER_DESCRIPTIONS = {
    0: (
        "#2a1a0e", "#FFD700",
        "Cluster 0 – Safe Haven Penuh (Inflasi Tinggi)",
        "Dolar AS lemah (di bawah rata-rata), harga emas & minyak tinggi (di atas "
        "rata-rata), dan inflasi tinggi. Investor beralih ke emas akibat tekanan "
        "ekonomi dan pelemahan daya beli mata uang. Kondisi ini adalah skenario "
        "'safe haven klasik'.",
    ),
    1: (
        "#0a2a1e", "#00C9A7",
        "Cluster 1 – Penguatan Emas Tanpa Tekanan Inflasi",
        "Dolar AS lemah, harga emas & minyak tinggi, namun inflasi tetap rendah. "
        "Penguatan emas didorong murni oleh pelemahan dolar (efek inverse DXY), "
        "bukan oleh tekanan inflasi. Emas berperan sebagai pelindung nilai terhadap "
        "depresiasi mata uang.",
    ),
    2: (
        "#1a0a1e", "#E84393",
        "Cluster 2 – Dominasi Dolar AS",
        "Dolar AS sangat kuat, harga emas & minyak rendah, inflasi dalam kondisi "
        "netral. Investor cenderung memegang dolar dibandingkan komoditas. Emas "
        "tidak berfungsi sebagai safe haven pada periode ini.",
    ),
}

# ---------------------------------------------------------------------------
# Rekomendasi investasi per cluster (untuk Halaman 3)
# ---------------------------------------------------------------------------
CLUSTER_RECOMMENDATIONS = {
    0: {
        "status": "✅ EMAS SANGAT DIREKOMENDASIKAN SEBAGAI SAFE HAVEN",
        "bg": "#0d2a1a",
        "border": "#00C9A7",
        "text_color": "#00ffc8",
        "detail": (
            "Kondisi pasar masuk ke <b>Cluster 0 – Safe Haven Penuh (Inflasi Tinggi)</b>. "
            "Dolar AS melemah sementara emas dan minyak berada di level tinggi disertai "
            "inflasi yang signifikan. Ini adalah kondisi klasik di mana emas berfungsi "
            "optimal sebagai lindung nilai. <b>Aksi: BELI / TAHAN EMAS</b> — momentum "
            "sangat mendukung untuk alokasi aset pada emas."
        ),
    },
    1: {
        "status": "🟡 EMAS DIREKOMENDASIKAN (Didorong Pelemahan Dolar)",
        "bg": "#2a2200",
        "border": "#FFD700",
        "text_color": "#FFD700",
        "detail": (
            "Kondisi pasar masuk ke <b>Cluster 1 – Penguatan Emas Tanpa Tekanan Inflasi</b>. "
            "Pelemahan dolar mendorong kenaikan emas meski inflasi masih rendah. "
            "Emas berperan sebagai pelindung nilai terhadap depresiasi mata uang. "
            "<b>Aksi: BELI EMAS secara selektif</b> — waspadai reversal jika dolar "
            "kembali menguat."
        ),
    },
    2: {
        "status": "🔴 EMAS TIDAK DIREKOMENDASIKAN SEBAGAI SAFE HAVEN",
        "bg": "#2a0a18",
        "border": "#E84393",
        "text_color": "#ff6b9d",
        "detail": (
            "Kondisi pasar masuk ke <b>Cluster 2 – Dominasi Dolar AS</b>. "
            "Dolar AS sangat kuat menekan harga emas dan komoditas lain. "
            "Investor cenderung mengalihkan aset ke instrumen berbasis dolar. "
            "<b>Aksi: HINDARI / KURANGI POSISI EMAS</b> — pertimbangkan diversifikasi "
            "ke instrumen dolar atau obligasi AS."
        ),
    },
}

# ---------------------------------------------------------------------------
# Dynamic CSS Generator (Supports Dark and Light themes)
# ---------------------------------------------------------------------------
def get_css(theme: str = "dark") -> str:
    is_dark = (theme == "dark")
    
    bg_gradient = "radial-gradient(circle at 50% 0%, #121324 0%, #0b0c16 100%)" if is_dark else "radial-gradient(circle at 50% 0%, #f8fafc 0%, #e2e8f0 100%)"
    body_color = "#e2e8f0" if is_dark else "#1e293b"
    sidebar_bg = "rgba(15, 17, 36, 0.7)" if is_dark else "rgba(241, 245, 249, 0.85)"
    sidebar_border = "rgba(255, 215, 0, 0.08)" if is_dark else "rgba(0, 0, 0, 0.06)"
    sidebar_text = "#cbd5e1" if is_dark else "#334155"
    sidebar_hover = "rgba(255, 215, 0, 0.06)" if is_dark else "rgba(0, 0, 0, 0.03)"
    sidebar_hover_text = "#ffd700" if is_dark else "#b89600"
    
    metric_bg = "rgba(26, 29, 58, 0.45)" if is_dark else "rgba(255, 255, 255, 0.7)"
    metric_border = "rgba(255, 255, 255, 0.08)" if is_dark else "rgba(0, 0, 0, 0.08)"
    metric_label = "#cbd5e1" if is_dark else "#475569"
    metric_val = "#ffd700" if is_dark else "#b89600"
    
    hero_bg = "linear-gradient(135deg, rgba(22, 33, 62, 0.7) 0%, rgba(15, 23, 42, 0.85) 100%)" if is_dark else "linear-gradient(135deg, rgba(219, 234, 254, 0.85) 0%, rgba(241, 245, 249, 0.9) 100%)"
    hero_border = "rgba(255, 215, 0, 0.15)" if is_dark else "rgba(255, 215, 0, 0.25)"
    hero_title = "#ffd700" if is_dark else "#b89600"
    hero_text = "#cbd5e1" if is_dark else "#334155"
    
    sec_title = "#ffffff" if is_dark else "#0f172a"
    
    insight_bg = "rgba(255, 215, 0, 0.03)" if is_dark else "rgba(255, 215, 0, 0.06)"
    insight_border = "rgba(255, 215, 0, 0.15)" if is_dark else "rgba(255, 215, 0, 0.35)"
    insight_text = "#f8fafc" if is_dark else "#1e293b"
    
    cluster_card_border = "rgba(255, 255, 255, 0.06)" if is_dark else "rgba(0, 0, 0, 0.08)"
    cluster_card_text = "#f1f5f9" if is_dark else "#1e293b"
    
    upload_banner_bg = "rgba(26, 29, 58, 0.3)" if is_dark else "rgba(255, 255, 255, 0.5)"
    upload_banner_border = "rgba(255, 215, 0, 0.25)" if is_dark else "rgba(255, 215, 0, 0.4)"
    upload_banner_text = "#cbd5e1" if is_dark else "#475569"
    
    dropzone_bg = "rgba(18, 20, 42, 0.6)" if is_dark else "rgba(255, 255, 255, 0.85)"
    dropzone_border = "rgba(255, 215, 0, 0.3)" if is_dark else "rgba(255, 215, 0, 0.4)"
    dropzone_text = "#ffd700" if is_dark else "#b89600"
    dropzone_small = "#cbd5e1" if is_dark else "#475569"
    dropzone_btn_bg = "rgba(255, 215, 0, 0.12)" if is_dark else "rgba(255, 215, 0, 0.08)"
    
    form_bg = "rgba(26, 29, 58, 0.25)" if is_dark else "rgba(255, 255, 255, 0.7)"
    form_border = "rgba(255, 255, 255, 0.06)" if is_dark else "rgba(0, 0, 0, 0.08)"
    
    dataframe_border = "rgba(255, 255, 255, 0.05)" if is_dark else "rgba(0, 0, 0, 0.06)"
    
    pred_box_custom_styles = """
    .stApp .pred-box-0 {
        background-color: #0d2a1a !important;
        border-color: #00C9A7 !important;
    }
    .stApp .pred-box-0 h3 {
        color: #00ffc8 !important;
    }
    .stApp .pred-box-0 p, .stApp .pred-box-0 b {
        color: #ffffff !important;
    }

    .stApp .pred-box-1 {
        background-color: #2a2200 !important;
        border-color: #FFD700 !important;
    }
    .stApp .pred-box-1 h3 {
        color: #FFD700 !important;
    }
    .stApp .pred-box-1 p, .stApp .pred-box-1 b {
        color: #ffffff !important;
    }

    .stApp .pred-box-2 {
        background-color: #2a0a18 !important;
        border-color: #E84393 !important;
    }
    .stApp .pred-box-2 h3 {
        color: #ff6b9d !important;
    }
    .stApp .pred-box-2 p, .stApp .pred-box-2 b {
        color: #ffffff !important;
    }
    """ if is_dark else """
    .stApp .pred-box-0 {
        background-color: #d1e7dd !important;
        border-color: #badbcc !important;
    }
    .stApp .pred-box-0 h3, .stApp .pred-box-0 p, .stApp .pred-box-0 b {
        color: #0f5132 !important;
    }

    .stApp .pred-box-1 {
        background-color: #fff3cd !important;
        border-color: #ffecb5 !important;
    }
    .stApp .pred-box-1 h3, .stApp .pred-box-1 p, .stApp .pred-box-1 b {
        color: #664d03 !important;
    }

    .stApp .pred-box-2 {
        background-color: #f8d7da !important;
        border-color: #f5c2c7 !important;
    }
    .stApp .pred-box-2 h3, .stApp .pred-box-2 p, .stApp .pred-box-2 b {
        color: #842029 !important;
    }
    """

    cluster_card_custom_styles = """
    .stApp .cluster-card-0 {
        background-color: #2a1a0e !important;
        border-color: rgba(255, 215, 0, 0.25) !important;
    }
    .stApp .cluster-card-0 h4 {
        color: #FFD700 !important;
    }
    .stApp .cluster-card-0 p {
        color: #f1f5f9 !important;
    }

    .stApp .cluster-card-1 {
        background-color: #0a2a1e !important;
        border-color: rgba(0, 201, 167, 0.25) !important;
    }
    .stApp .cluster-card-1 h4 {
        color: #00C9A7 !important;
    }
    .stApp .cluster-card-1 p {
        color: #f1f5f9 !important;
    }

    .stApp .cluster-card-2 {
        background-color: #1a0a1e !important;
        border-color: rgba(232, 67, 147, 0.25) !important;
    }
    .stApp .cluster-card-2 h4 {
        color: #E84393 !important;
    }
    .stApp .cluster-card-2 p {
        color: #f1f5f9 !important;
    }
    """ if is_dark else """
    .stApp .cluster-card-0 {
        background-color: #fff3cd !important;
        border-color: #ffecb5 !important;
    }
    .stApp .cluster-card-0 h4, .stApp .cluster-card-0 p {
        color: #664d03 !important;
    }

    .stApp .cluster-card-1 {
        background-color: #d1e7dd !important;
        border-color: #badbcc !important;
    }
    .stApp .cluster-card-1 h4, .stApp .cluster-card-1 p {
        color: #0f5132 !important;
    }

    .stApp .cluster-card-2 {
        background-color: #f8d7da !important;
        border-color: #f5c2c7 !important;
    }
    .stApp .cluster-card-2 h4, .stApp .cluster-card-2 p {
        color: #842029 !important;
    }
    """
    
    custom_light_styles = "" if is_dark else """
    /* Fix Streamlit widgets text in light mode */
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
        color: #334155 !important;
    }
    .stApp label, .stApp p, .stApp span, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: #1e293b !important;
    }
    .hero-banner h1, .section-title, .insight-box b, .cluster-card h4, .upload-banner h2 {
        color: #b89600 !important;
    }
    /* Let dataframes display with standard black/gray text in light mode */
    .stDataFrame div {
        color: inherit !important;
    }
    """

    return f"""
<style>
/* ---- Google Font Import ---- */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

/* ---- Base Reset & Fonts ---- */
html, body, [class*="css"] {{
    font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
    color: {body_color};
}}

/* ---- Base Styling ---- */
.stApp {{
    background: {bg_gradient};
}}

/* ---- Sidebar Glassmorphism ---- */
[data-testid="stSidebar"] {{
    background: {sidebar_bg} !important;
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border-right: 1px solid {sidebar_border} !important;
}}
[data-testid="stSidebar"] * {{
    color: {sidebar_text} !important;
}}
[data-testid="stSidebar"] .stRadio label {{
    font-size: 0.95rem;
    font-weight: 500;
    padding: 8px 12px;
    border-radius: 8px;
    transition: all 0.3s ease;
    margin-bottom: 4px;
}}
[data-testid="stSidebar"] .stRadio label:hover {{
    background: {sidebar_hover};
    color: {sidebar_hover_text} !important;
}}

/* ---- Metric Cards ---- */
[data-testid="stMetric"] {{
    background: {metric_bg} !important;
    backdrop-filter: blur(10px);
    border: 1px solid {metric_border} !important;
    border-radius: 16px !important;
    padding: 20px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
    transition: transform 0.3s ease, border-color 0.3s ease;
}}
[data-testid="stMetric"]:hover {{
    transform: translateY(-4px);
    border-color: rgba(255, 215, 0, 0.3) !important;
}}
[data-testid="stMetricLabel"] {{
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: {metric_label} !important;
}}
[data-testid="stMetricValue"] {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: {metric_val} !important;
    font-weight: 800 !important;
    font-size: 1.8rem !important;
}}

/* ---- Hero Banner ---- */
.hero-banner {{
    background: {hero_bg};
    border: 1px solid {hero_border};
    border-radius: 20px;
    padding: 36px;
    margin-bottom: 28px;
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.2);
    position: relative;
    overflow: hidden;
}}
.hero-banner::before {{
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 250px;
    height: 250px;
    background: radial-gradient(circle, rgba(255, 215, 0, 0.08) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}}
.hero-banner h1 {{
    font-size: 2.2rem;
    font-weight: 800;
    color: {hero_title};
    margin: 0 0 12px 0;
    letter-spacing: -0.02em;
}}
.hero-banner p {{
    color: {hero_text};
    font-size: 1.05rem;
    margin: 0;
    line-height: 1.65;
    max-width: 90%;
}}

/* ---- Section Title ---- */
.section-title {{
    font-size: 1.25rem;
    font-weight: 700;
    color: {sec_title};
    border-left: 5px solid #ffd700;
    padding-left: 14px;
    margin: 36px 0 18px 0;
    letter-spacing: -0.01em;
}}

/* ---- Insight Box ---- */
.insight-box {{
    background: {insight_bg};
    border: 1px solid {insight_border};
    border-radius: 12px;
    padding: 16px 20px;
    margin: 12px 0;
    font-size: 0.95rem;
    color: {insight_text};
    line-height: 1.55;
    transition: background 0.3s ease;
}}
.insight-box:hover {{
    background: rgba(255, 215, 0, 0.05);
}}
.insight-box b {{
    color: #ffd700;
    font-weight: 600;
}}

/* ---- Cluster Cards ---- */
.cluster-card {{
    border-radius: 16px;
    padding: 20px 24px;
    margin: 14px 0;
    border: 1px solid {cluster_card_border};
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}}
.cluster-card:hover {{
    transform: translateX(4px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
}}
.cluster-card h4 {{
    margin: 0 0 8px 0;
    font-size: 1.1rem;
    font-weight: 700;
}}
.cluster-card p {{
    margin: 0;
    font-size: 0.92rem;
    color: {cluster_card_text};
    line-height: 1.6;
}}

{cluster_card_custom_styles}

/* ---- Prediction Result Box ---- */
.pred-box {{
    border-radius: 18px;
    padding: 28px 32px;
    margin-top: 24px;
    border: 2px solid;
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.2);
}}

{pred_box_custom_styles}

/* ---- Upload Area ---- */
.upload-banner {{
    background: {upload_banner_bg};
    border: 2px dashed {upload_banner_border};
    border-radius: 20px;
    padding: 50px 30px;
    text-align: center;
    margin: 32px 0;
    transition: border-color 0.3s ease;
}}
.upload-banner:hover {{
    border-color: rgba(255, 215, 0, 0.5);
}}
.upload-banner h2 {{
    color: #ffd700;
    font-size: 1.6rem;
    font-weight: 700;
    margin: 0 0 12px 0;
}}
.upload-banner p {{
    color: {upload_banner_text};
    font-size: 0.95rem;
    margin: 0;
}}

/* ---- File Uploader Dropzone Customization ---- */
[data-testid="stFileUploaderDropzone"] {{
    background: {dropzone_bg} !important;
    border: 1px dashed {dropzone_border} !important;
    border-radius: 12px !important;
}}
[data-testid="stFileUploaderDropzone"] * {{
    color: {dropzone_text} !important;
}}
[data-testid="stFileUploaderDropzone"] small {{
    color: {dropzone_small} !important;
}}
[data-testid="stFileUploaderDropzone"] button {{
    background-color: {dropzone_btn_bg} !important;
    border: 1px solid {dropzone_border} !important;
    color: {dropzone_text} !important;
}}

/* ---- Custom Dataframes & Tables Styling ---- */
.stDataFrame {{
    border: 1px solid {dataframe_border} !important;
    border-radius: 12px;
    overflow: hidden;
}}

/* ---- Buttons Customization ---- */
.stButton>button {{
    background: linear-gradient(135deg, #ffd700 0%, #b89600 100%) !important;
    color: #0b0c16 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 24px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}}
.stButton>button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(255, 215, 0, 0.3);
}}

/* ---- Form Styling ---- */
[data-testid="stForm"] {{
    background: {form_bg};
    border: 1px solid {form_border};
    border-radius: 20px;
    padding: 28px !important;
}}

{custom_light_styles}
</style>
"""

