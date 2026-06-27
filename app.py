# =============================================================================
# app.py – Entry Point Utama Aplikasi
#
# Struktur Proyek:
#   app.py                  ← (file ini) konfigurasi, sidebar, routing
#   config.py               ← konstanta & CSS global
#   utils/
#     data_loader.py        ← upload CSV, parsing, validasi
#     model.py              ← train_pipeline, compute_evaluation_metrics
#   pages/
#     page_eksplorasi.py    ← Halaman 1: Eksplorasi Data & Korelasi
#     page_evaluasi.py      ← Halaman 2: Evaluasi Model & K-Means
#     page_simulasi.py      ← Halaman 3: Simulasi Keputusan Investasi
# =============================================================================

import streamlit as st

# ---------------------------------------------------------------------------
# Import modul internal
# ---------------------------------------------------------------------------
from config import CUSTOM_CSS
from utils.data_loader import (
    sidebar_csv_uploader,
    parse_csv,
    validate_columns,
    render_upload_prompt,
)
from utils.model import train_pipeline
from pages import page_eksplorasi, page_evaluasi, page_simulasi


# ---------------------------------------------------------------------------
# Konfigurasi halaman (HARUS menjadi perintah Streamlit pertama)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Gold Safe Haven Analysis | CRISP-DM",
    page_icon="🥇",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Injeksi CSS premium
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Sidebar: Header & Navigasi
# ---------------------------------------------------------------------------
def _render_sidebar() -> str:
    """
    Membangun seluruh konten sidebar:
      - Logo & judul aplikasi
      - Menu navigasi
      - Widget upload CSV
      - Informasi metodologi

    Returns:
        Kunci halaman yang dipilih pengguna ('eksplorasi', 'evaluasi', 'simulasi').
    """
    # -- Logo & judul --
    st.sidebar.markdown(
        """
        <div style="text-align:center; padding:16px 0 20px 0;">
            <div style="font-size:2.8rem;">🥇</div>
            <div style="font-size:1rem; font-weight:700; color:#FFD700; margin-top:6px;">
                Gold Safe Haven
            </div>
            <div style="font-size:0.75rem; color:#8090b0; margin-top:2px;">
                CRISP-DM | K-Means Clustering
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # -- Navigasi --
    PAGE_OPTIONS = {
        "📊 Eksplorasi Data & Korelasi":      "eksplorasi",
        "📈 Evaluasi Model & K-Means":         "evaluasi",
        "💡 Simulasi Keputusan Investasi":     "simulasi",
    }
    choice = st.sidebar.radio(
        "Navigasi",
        list(PAGE_OPTIONS.keys()),
        label_visibility="collapsed",
    )

    # -- Upload CSV --
    sidebar_csv_uploader()

    # -- Info metodologi --
    st.sidebar.markdown(
        """
        <div style="font-size:0.78rem; color:#6070a0; padding:8px;">
            <b style="color:#8090b0;">Dataset:</b><br>
            Gold_vs_Economic_Factors_2015_2026.csv<br><br>
            <b style="color:#8090b0;">Metodologi:</b><br>
            CRISP-DM · Z-Score Standardization<br>
            K-Means (k=3) · PCA 2D · Euclidean Distance
        </div>
        """,
        unsafe_allow_html=True,
    )

    return PAGE_OPTIONS[choice]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    """
    Fungsi utama aplikasi:
      1. Render sidebar dan dapatkan halaman yang dipilih
      2. Periksa apakah dataset sudah diupload
      3. Validasi kolom dataset
      4. Latih pipeline (cached) dan routing ke halaman yang sesuai
    """
    page_key = _render_sidebar()

    # -- Cek apakah CSV sudah diupload --
    if "csv_bytes" not in st.session_state:
        render_upload_prompt()
        st.stop()

    # -- Parse & validasi dataset --
    csv_bytes = st.session_state["csv_bytes"]
    df_raw    = parse_csv(csv_bytes)

    is_valid, missing_cols = validate_columns(df_raw)
    if not is_valid:
        st.error(
            f"❌ Kolom berikut tidak ditemukan dalam dataset: **{missing_cols}**\n\n"
            "Pastikan file CSV memiliki kolom yang sesuai lalu upload ulang."
        )
        st.stop()

    # -- Latih pipeline (di-cache, hanya dilatih sekali per file) --
    df_raw, X_scaled, scaler, kmeans, pca, df_result = train_pipeline(csv_bytes)

    # -- Routing halaman --
    if page_key == "eksplorasi":
        page_eksplorasi.render(df_raw)

    elif page_key == "evaluasi":
        page_evaluasi.render(df_result, X_scaled, kmeans, pca)

    elif page_key == "simulasi":
        page_simulasi.render(scaler, kmeans)


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
