# =============================================================================
# pages/page_simulasi.py
# Halaman 3: Simulasi Keputusan Investasi (Implementasi Interaktif)
# =============================================================================

import numpy as np
import pandas as pd
import streamlit as st

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from config import CLUSTER_LABELS, CLUSTER_RECOMMENDATIONS


# ---------------------------------------------------------------------------
# Entry point halaman
# ---------------------------------------------------------------------------

def render(scaler: StandardScaler, kmeans: KMeans) -> None:
    """
    Menampilkan seluruh konten Halaman 3:
      - Hero banner penjelasan halaman
      - Form input 4 variabel pasar
      - Tombol analisis → prediksi cluster → rekomendasi investasi
      - Tabel jarak Euclidean ke setiap centroid
      - Tabel nilai input setelah Z-Score

    Args:
        scaler : StandardScaler yang sudah di-fit pada data training.
        kmeans : KMeans model yang sudah di-fit pada data training.
    """
    _render_hero()
    _render_form(scaler, kmeans)


# ---------------------------------------------------------------------------
# Sub-fungsi private
# ---------------------------------------------------------------------------

def _render_hero() -> None:
    """Menampilkan banner judul dan deskripsi Halaman 3."""
    st.markdown(
        """
        <div class="hero-banner" style="padding:24px 28px;">
            <h1 style="font-size:1.5rem;">💡 Simulasi Keputusan Investasi</h1>
            <p>
                Masukkan kondisi pasar saat ini. Sistem akan menganalisis ke cluster
                mana kondisi tersebut termasuk dan memberikan rekomendasi apakah emas
                layak dijadikan aset <i>safe haven</i>.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_form(scaler: StandardScaler, kmeans: KMeans) -> None:
    """
    Menampilkan form input 4 variabel.
    Setelah tombol ditekan, memanggil fungsi prediksi & tampil hasil.
    """
    st.markdown(
        '<p class="section-title" style="margin-top:4px">🔢 Input Kondisi Pasar</p>',
        unsafe_allow_html=True,
    )

    with st.form("form_simulasi"):
        col1, col2 = st.columns(2)

        gold = col1.number_input(
            "🪙 Harga Emas (XAU/USD)",
            min_value=500.0, max_value=5000.0,
            value=2350.0, step=10.0,
            help="Harga emas spot dalam USD per troy ounce.",
        )
        dxy = col1.number_input(
            "💵 Indeks Dolar AS (DXY)",
            min_value=70.0, max_value=130.0,
            value=103.5, step=0.1,
            help="US Dollar Index (DXY) mencerminkan kekuatan dolar.",
        )
        oil = col2.number_input(
            "🛢️ Harga Minyak Mentah (USD/bbl)",
            min_value=10.0, max_value=200.0,
            value=82.0, step=1.0,
            help="Harga minyak mentah Brent/WTI dalam USD per barel.",
        )
        infl = col2.number_input(
            "📈 Tingkat Inflasi (%)",
            min_value=-2.0, max_value=20.0,
            value=3.2, step=0.1,
            help="Tingkat inflasi tahunan dalam persen.",
        )

        submitted = st.form_submit_button(
            "🔍 Analisis Kondisi Pasar",
            use_container_width=True,
            type="primary",
        )

    if submitted:
        _run_prediction(scaler, kmeans, gold, dxy, oil, infl)


def _run_prediction(
    scaler: StandardScaler,
    kmeans: KMeans,
    gold: float,
    dxy: float,
    oil: float,
    infl: float,
) -> None:
    """
    Menjalankan pipeline prediksi:
      1. Susun array input
      2. Standarisasi Z-Score menggunakan scaler yang sudah di-fit
      3. Prediksi cluster dengan KMeans
      4. Hitung jarak Euclidean ke setiap centroid
      5. Tampilkan hasil dan rekomendasi

    Args:
        scaler : StandardScaler ter-fit.
        kmeans : KMeans ter-fit.
        gold   : Harga emas input.
        dxy    : Indeks DXY input.
        oil    : Harga minyak input.
        infl   : Inflasi input.
    """
    # 1. Array input
    X_user = np.array([[gold, dxy, oil, infl]])

    # 2. Transformasi Z-Score (menggunakan parameter scaler dari data training)
    X_user_scaled = scaler.transform(X_user)

    # 3. Prediksi cluster
    cluster_pred = int(kmeans.predict(X_user_scaled)[0])

    # 4. Jarak Euclidean ke setiap centroid
    distances = np.linalg.norm(kmeans.cluster_centers_ - X_user_scaled, axis=1)
    dist_df = pd.DataFrame({
        "Cluster": [f"Cluster {i}" for i in range(3)],
        "Label":   [CLUSTER_LABELS[i] for i in range(3)],
        "Jarak Euclidean": distances.round(4),
    })

    # 5. Tampilkan hasil
    _render_prediction_result(cluster_pred)
    _render_distance_table(dist_df)
    _render_zscore_table(gold, dxy, oil, infl, X_user_scaled)


def _render_prediction_result(cluster_pred: int) -> None:
    """Menampilkan kotak rekomendasi investasi berwarna sesuai cluster."""
    rec = CLUSTER_RECOMMENDATIONS[cluster_pred]
    st.markdown(
        f"""
        <div class="pred-box pred-box-{cluster_pred}">
            <h3 style="margin:0 0 10px 0;">
                {rec['status']}
            </h3>
            <p style="font-size:0.95rem; line-height:1.65; margin:0;">
                {rec['detail']}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_distance_table(dist_df: pd.DataFrame) -> None:
    """
    Menampilkan tabel jarak Euclidean ke setiap centroid.
    Baris dengan jarak terkecil (cluster prediksi) di-highlight.
    """
    st.markdown(
        '<p class="section-title">📏 Jarak Euclidean ke Setiap Centroid</p>',
        unsafe_allow_html=True,
    )

    min_idx = dist_df["Jarak Euclidean"].idxmin()

    def _highlight_min(row):
        return (
            ["background-color: rgba(255,215,0,0.12)"] * len(row)
            if row.name == min_idx
            else [""] * len(row)
        )

    st.dataframe(
        dist_df.style
            .apply(_highlight_min, axis=1)
            .format({"Jarak Euclidean": "{:.4f}"}),
        use_container_width=True,
        hide_index=True,
    )


def _render_zscore_table(
    gold: float, dxy: float, oil: float, infl: float,
    X_user_scaled: np.ndarray,
) -> None:
    """Menampilkan tabel nilai input asli vs. nilai setelah standarisasi Z-Score."""
    st.markdown(
        '<p class="section-title">🔎 Input yang Dianalisis (setelah Z-Score)</p>',
        unsafe_allow_html=True,
    )

    input_table = pd.DataFrame({
        "Variabel": [
            "Harga Emas (XAU/USD)",
            "Indeks DXY",
            "Harga Minyak (USD/bbl)",
            "Inflasi (%)",
        ],
        "Nilai Asli":              [gold, dxy, oil, infl],
        "Z-Score (Standarisasi)": X_user_scaled[0].round(4),
    })

    st.dataframe(
        input_table.style.format({
            "Nilai Asli":              "{:.2f}",
            "Z-Score (Standarisasi)": "{:.4f}",
        }),
        use_container_width=True,
        hide_index=True,
    )
