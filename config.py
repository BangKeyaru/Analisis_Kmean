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
# Custom CSS (dark-mode premium theme)
# ---------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
/* ---- Google Font ---- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    border-right: 1px solid rgba(255,215,0,0.15);
}
[data-testid="stSidebar"] * { color: #e0e0e0 !important; }
[data-testid="stSidebar"] .stRadio label { font-size: 0.95rem; padding: 6px 0; }

/* ---- Metric Cards ---- */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, #1e1e3f 0%, #252545 100%);
    border: 1px solid rgba(255,215,0,0.25);
    border-radius: 12px;
    padding: 16px !important;
}
[data-testid="stMetricValue"] { color: #FFD700 !important; font-weight: 700 !important; }

/* ---- Hero Banner ---- */
.hero-banner {
    background: linear-gradient(135deg, #0f3460 0%, #16213e 50%, #1a1a2e 100%);
    border: 1px solid rgba(255,215,0,0.3);
    border-radius: 16px;
    padding: 32px 36px;
    margin-bottom: 24px;
}
.hero-banner h1 { font-size: 2rem; font-weight: 700; color: #FFD700; margin: 0 0 8px 0; }
.hero-banner p  { color: #b0b8cc; font-size: 1rem; margin: 0; line-height: 1.6; }

/* ---- Section Title ---- */
.section-title {
    font-size: 1.15rem;
    font-weight: 600;
    color: #FFD700;
    border-left: 4px solid #FFD700;
    padding-left: 10px;
    margin: 28px 0 14px 0;
}

/* ---- Insight Box ---- */
.insight-box {
    background: rgba(255,215,0,0.06);
    border: 1px solid rgba(255,215,0,0.25);
    border-radius: 10px;
    padding: 14px 18px;
    margin: 8px 0;
    font-size: 0.9rem;
    color: #d0d8e8;
}
.insight-box b { color: #FFD700; }

/* ---- Cluster Cards ---- */
.cluster-card {
    border-radius: 12px;
    padding: 18px 20px;
    margin: 8px 0;
    border: 1px solid rgba(255,255,255,0.12);
}
.cluster-card h4 { margin: 0 0 6px 0; font-size: 1rem; font-weight: 600; }
.cluster-card p  { margin: 0; font-size: 0.88rem; color: #c8d0e0; line-height: 1.55; }

/* ---- Prediction Result Box ---- */
.pred-box {
    border-radius: 14px;
    padding: 24px 28px;
    margin-top: 18px;
    border: 2px solid;
}

/* ---- Upload Area ---- */
.upload-banner {
    background: linear-gradient(135deg, #16213e 0%, #1a1a2e 100%);
    border: 2px dashed rgba(255,215,0,0.4);
    border-radius: 16px;
    padding: 40px 24px;
    text-align: center;
    margin: 24px 0;
}
.upload-banner h2 { color: #FFD700; font-size: 1.4rem; margin: 0 0 8px 0; }
.upload-banner p  { color: #8090b0; font-size: 0.9rem; margin: 0; }
</style>
"""
