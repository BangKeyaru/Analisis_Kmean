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
# Custom CSS (premium modern UI, glassmorphism, smooth animations)
# ---------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
/* ---- Google Font Import ---- */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

/* ---- Base Reset & Fonts ---- */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
    color: #e2e8f0;
}

/* ---- Dark Mode Base Styling ---- */
.stApp {
    background: radial-gradient(circle at 50% 0%, #121324 0%, #0b0c16 100%);
}

/* ---- Sidebar Glassmorphism ---- */
[data-testid="stSidebar"] {
    background: rgba(15, 17, 36, 0.7) !important;
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255, 215, 0, 0.08) !important;
}
[data-testid="stSidebar"] * {
    color: #cbd5e1 !important;
}
[data-testid="stSidebar"] .stRadio label {
    font-size: 0.95rem;
    font-weight: 500;
    padding: 8px 12px;
    border-radius: 8px;
    transition: all 0.3s ease;
    margin-bottom: 4px;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255, 215, 0, 0.06);
    color: #ffd700 !important;
}

/* ---- Metric Cards ---- */
[data-testid="stMetric"] {
    background: rgba(26, 29, 58, 0.45) !important;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 16px !important;
    padding: 20px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, border-color 0.3s ease;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-4px);
    border-color: rgba(255, 215, 0, 0.3) !important;
}
[data-testid="stMetricLabel"] {
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #94a3b8 !important;
}
[data-testid="stMetricValue"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffd700 !important;
    font-weight: 800 !important;
    font-size: 1.8rem !important;
}

/* ---- Hero Banner ---- */
.hero-banner {
    background: linear-gradient(135deg, rgba(22, 33, 62, 0.7) 0%, rgba(15, 23, 42, 0.85) 100%);
    border: 1px solid rgba(255, 215, 0, 0.15);
    border-radius: 20px;
    padding: 36px;
    margin-bottom: 28px;
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.3);
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 250px;
    height: 250px;
    background: radial-gradient(circle, rgba(255, 215, 0, 0.1) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}
.hero-banner h1 {
    font-size: 2.2rem;
    font-weight: 800;
    color: #ffd700;
    margin: 0 0 12px 0;
    letter-spacing: -0.02em;
}
.hero-banner p {
    color: #94a3b8;
    font-size: 1.05rem;
    margin: 0;
    line-height: 1.65;
    max-width: 90%;
}

/* ---- Section Title ---- */
.section-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #ffffff;
    border-left: 5px solid #ffd700;
    padding-left: 14px;
    margin: 36px 0 18px 0;
    letter-spacing: -0.01em;
}

/* ---- Insight Box ---- */
.insight-box {
    background: rgba(255, 215, 0, 0.03);
    border: 1px solid rgba(255, 215, 0, 0.15);
    border-radius: 12px;
    padding: 16px 20px;
    margin: 12px 0;
    font-size: 0.95rem;
    color: #cbd5e1;
    line-height: 1.55;
    transition: background 0.3s ease;
}
.insight-box:hover {
    background: rgba(255, 215, 0, 0.05);
}
.insight-box b {
    color: #ffd700;
    font-weight: 600;
}

/* ---- Cluster Cards ---- */
.cluster-card {
    border-radius: 16px;
    padding: 20px 24px;
    margin: 14px 0;
    border: 1px solid rgba(255, 255, 255, 0.06);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.cluster-card:hover {
    transform: translateX(4px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
}
.cluster-card h4 {
    margin: 0 0 8px 0;
    font-size: 1.1rem;
    font-weight: 700;
}
.cluster-card p {
    margin: 0;
    font-size: 0.92rem;
    color: #94a3b8;
    line-height: 1.6;
}

/* ---- Prediction Result Box ---- */
.pred-box {
    border-radius: 18px;
    padding: 28px 32px;
    margin-top: 24px;
    border: 2px solid;
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.3);
}

/* ---- Upload Area ---- */
.upload-banner {
    background: rgba(26, 29, 58, 0.3);
    border: 2px dashed rgba(255, 215, 0, 0.25);
    border-radius: 20px;
    padding: 50px 30px;
    text-align: center;
    margin: 32px 0;
    transition: border-color 0.3s ease;
}
.upload-banner:hover {
    border-color: rgba(255, 215, 0, 0.5);
}
.upload-banner h2 {
    color: #ffd700;
    font-size: 1.6rem;
    font-weight: 700;
    margin: 0 0 12px 0;
}
.upload-banner p {
    color: #94a3b8;
    font-size: 0.95rem;
    margin: 0;
}

/* ---- Custom Dataframes & Tables Styling ---- */
.stDataFrame {
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 12px;
    overflow: hidden;
}

/* ---- Buttons Customization ---- */
.stButton>button {
    background: linear-gradient(135deg, #ffd700 0%, #b89600 100%) !important;
    color: #0b0c16 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 24px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(255, 215, 0, 0.3);
}

/* ---- Form Styling ---- */
[data-testid="stForm"] {
    background: rgba(26, 29, 58, 0.25);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    padding: 28px !important;
}
</style>
"""
