# =============================================================================
# utils/data_loader.py
# Bertanggung jawab untuk: membaca CSV (dari upload atau path lokal)
# dan menyimpannya di session_state agar tersedia di seluruh halaman.
# =============================================================================

import io
import streamlit as st
import pandas as pd

from config import FEATURES


# ---------------------------------------------------------------------------
# Widget Upload CSV (ditampilkan di sidebar)
# ---------------------------------------------------------------------------

def sidebar_csv_uploader() -> None:
    """
    Menampilkan widget st.file_uploader di sidebar.
    Hasil upload disimpan ke st.session_state["csv_bytes"] agar
    dapat diakses dari modul lain tanpa re-upload.
    """
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        '<p style="color:#FFD700; font-weight:600; font-size:0.85rem;">'
        "📂 Upload Dataset CSV</p>",
        unsafe_allow_html=True,
    )

    uploaded = st.sidebar.file_uploader(
        label="Pilih file CSV",
        type=["csv"],
        help="Upload file Gold_vs_Economic_Factors_2015_2026.csv",
        label_visibility="collapsed",
    )

    if uploaded is not None:
        # Simpan bytes ke session_state (tidak hilang saat halaman berganti)
        st.session_state["csv_bytes"] = uploaded.read()
        st.session_state["csv_name"]  = uploaded.name
        st.sidebar.success(f"✅ {uploaded.name}")
    elif "csv_bytes" in st.session_state:
        # File sudah di-upload sebelumnya — tampilkan info
        st.sidebar.info(f"📄 {st.session_state.get('csv_name', 'dataset.csv')}")
    else:
        st.sidebar.warning("⚠️ Belum ada dataset")


# ---------------------------------------------------------------------------
# Fungsi pembaca CSV (dengan cache per konten bytes)
# ---------------------------------------------------------------------------

@st.cache_data(show_spinner="⏳ Memuat dataset …")
def parse_csv(csv_bytes: bytes) -> pd.DataFrame:
    """
    Mem-parse bytes CSV menjadi DataFrame.
    Gunakan @st.cache_data agar tidak di-parse ulang selama bytes-nya sama.

    Args:
        csv_bytes: Isi file CSV dalam bentuk bytes.

    Returns:
        DataFrame yang sudah diurutkan berdasarkan kolom Date.
    """
    df = pd.read_csv(io.BytesIO(csv_bytes), parse_dates=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# Validasi kolom dataset yang diupload
# ---------------------------------------------------------------------------

def validate_columns(df: pd.DataFrame) -> tuple[bool, list[str]]:
    """
    Memastikan DataFrame memiliki kolom yang diperlukan.

    Returns:
        (is_valid, missing_columns)
    """
    required = ["Date"] + FEATURES
    missing  = [col for col in required if col not in df.columns]
    return len(missing) == 0, missing


# ---------------------------------------------------------------------------
# Render halaman "belum upload" (placeholder)
# ---------------------------------------------------------------------------

def render_upload_prompt() -> None:
    """
    Menampilkan pesan instruksi upload bila dataset belum tersedia.
    """
    st.markdown(
        """
        <div class="upload-banner">
            <h2>📂 Upload Dataset untuk Memulai</h2>
            <p>
                Gunakan panel <b>Upload Dataset CSV</b> di sidebar kiri untuk
                mengunggah file <code>Gold_vs_Economic_Factors_2015_2026.csv</code>.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "**Format kolom yang diperlukan:**\n\n"
        "| Kolom | Tipe | Keterangan |\n"
        "|---|---|---|\n"
        "| `Date` | Date | Tanggal observasi (identifier) |\n"
        "| `Gold_Price_XAU_USD` | Numerik | Harga emas (USD) |\n"
        "| `US_Dollar_Index_DXY` | Numerik | Indeks dolar AS |\n"
        "| `Crude_Oil_Price` | Numerik | Harga minyak mentah |\n"
        "| `Inflation_Rate_Pct` | Numerik | Tingkat inflasi (%) |"
    )
