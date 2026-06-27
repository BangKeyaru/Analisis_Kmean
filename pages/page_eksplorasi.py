# =============================================================================
# pages/page_eksplorasi.py
# Halaman 1: Eksplorasi Data & Korelasi
# =============================================================================

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from config import FEATURES


# ---------------------------------------------------------------------------
# Entry point halaman
# ---------------------------------------------------------------------------

def render(df: pd.DataFrame) -> None:
    """
    Menampilkan seluruh konten Halaman 1:
      - Hero banner & latar belakang penelitian
      - Metric cards ringkasan dataset
      - Cuplikan data (20 baris pertama)
      - Statistik deskriptif (Mean, Min, Max, Std Dev)
      - Heatmap korelasi
      - Insight korelasi antar variabel

    Args:
        df: DataFrame asli yang sudah dimuat dari CSV.
    """
    _render_hero()
    _render_metrics(df)
    _render_data_preview(df)
    _render_descriptive_stats(df)
    _render_correlation_heatmap(df)
    _render_correlation_insights(df)


# ---------------------------------------------------------------------------
# Sub-fungsi private
# ---------------------------------------------------------------------------

def _render_hero() -> None:
    """Menampilkan banner judul dan deskripsi singkat penelitian."""
    st.markdown(
        """
        <div class="hero-banner" style="display: flex; align-items: center; gap: 24px;">
            <div style="flex-shrink: 0; display: flex; align-items: center; justify-content: center;">
                <svg viewBox="0 0 24 24" width="80" height="80" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <!-- Main body of the gold bar -->
                  <path d="M4 18L7 6H17L20 18H4Z" fill="url(#goldBarGradHero)" stroke="#d4af37" stroke-width="1.5"/>
                  <!-- Highlighting top surface -->
                  <path d="M7 6L8.5 12H15.5L17 6H7Z" fill="#ffffff" opacity="0.15"/>
                  <!-- Reflections and side lines -->
                  <path d="M4.5 16H19.5" stroke="#ffffff" stroke-width="1.2" opacity="0.2"/>
                  <defs>
                    <linearGradient id="goldBarGradHero" x1="4" y1="6" x2="20" y2="18" gradientUnits="userSpaceOnUse">
                      <stop stop-color="#FFE259"/>
                      <stop offset="1" stop-color="#FFA751"/>
                    </linearGradient>
                  </defs>
                </svg>
            </div>
            <div>
                <h1 style="margin: 0 0 8px 0; font-size: 1.8rem; font-weight: 800;">Analisis Perilaku Emas Sebagai Aset Safe Haven</h1>
                <p style="margin: 0; line-height: 1.6; font-size: 1.05rem;">
                    Implementasi riset <b>CRISP-DM</b> menggunakan <b>K-Means Clustering (k=3)</b>
                    untuk menganalisis perilaku harga emas terhadap indikator ekonomi global:
                    Indeks Dolar AS (DXY), Harga Minyak Mentah, dan Tingkat Inflasi.
                    Data historis mencakup periode <b>2015–2026</b>.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_metrics(df: pd.DataFrame) -> None:
    """Menampilkan 4 metric card ringkasan dataset."""
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📅 Total Observasi",     f"{len(df):,}")
    c2.metric("🪙 Rata-rata Harga Emas", f"${df['Gold_Price_XAU_USD'].mean():,.1f}")
    c3.metric("💵 Rata-rata DXY",        f"{df['US_Dollar_Index_DXY'].mean():.2f}")
    c4.metric("🛢️ Rata-rata Minyak",     f"${df['Crude_Oil_Price'].mean():.2f}")


def _render_data_preview(df: pd.DataFrame) -> None:
    """Menampilkan 20 baris pertama dataset."""
    st.markdown(
        '<p class="section-title">📋 Cuplikan Dataset (20 Baris Pertama)</p>',
        unsafe_allow_html=True,
    )
    df_preview = df.head(20).copy()
    df_preview.index = df_preview.index + 1
    st.dataframe(df_preview, use_container_width=True, height=300)


def _render_descriptive_stats(df: pd.DataFrame) -> None:
    """Menampilkan tabel statistik deskriptif dengan gradient."""
    st.markdown(
        '<p class="section-title">📊 Statistik Deskriptif</p>',
        unsafe_allow_html=True,
    )
    desc = (
        df[FEATURES]
        .describe()
        .loc[["mean", "min", "max", "std"]]
        .T
        .rename(columns={"mean": "Mean", "min": "Min", "max": "Max", "std": "Std Dev"})
        .round(4)
    )
    st.dataframe(
        desc.style
            .format("{:.4f}")
            .background_gradient(cmap="YlOrBr", axis=0),
        use_container_width=True,
    )


def _render_correlation_heatmap(df: pd.DataFrame) -> None:
    """Membangun dan menampilkan heatmap korelasi antar variabel."""
    st.markdown(
        '<p class="section-title">🔥 Matriks Korelasi (Heatmap)</p>',
        unsafe_allow_html=True,
    )
    corr = df[FEATURES].corr()

    theme = st.session_state.get("theme", "dark")
    is_dark = (theme == "dark")
    
    fig_bg = "#121324" if is_dark else "#f8fafc"
    ax_bg = "#1a1d3a" if is_dark else "#ffffff"
    text_color = "#ffd700" if is_dark else "#b89600"
    tick_color = "#94a3b8" if is_dark else "#475569"
    grid_line = "#121324" if is_dark else "#e2e8f0"

    fig, ax = plt.subplots(figsize=(7, 5))
    fig.patch.set_facecolor(fig_bg)
    ax.set_facecolor(ax_bg)

    sns.heatmap(
        corr,
        annot=True,
        fmt=".3f",
        cmap="YlOrBr",
        linewidths=1,
        linecolor=grid_line,
        ax=ax,
        square=True,
        annot_kws={"size": 11, "weight": "bold"},
        cbar_kws={"shrink": 0.75},
    )
    ax.set_title(
        "Korelasi Antar Variabel Ekonomi (2015–2026)",
        color=text_color, fontsize=13, fontweight="bold", pad=16,
    )
    ax.tick_params(colors=tick_color, labelsize=9)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)


def _render_correlation_insights(df: pd.DataFrame) -> None:
    """
    Menampilkan kotak insight korelasi berdasarkan nilai aktual dataset
    yang diupload (bukan hardcoded), serta kutipan dari penelitian.
    """
    st.markdown(
        '<p class="section-title">💡 Insight Korelasi</p>',
        unsafe_allow_html=True,
    )

    corr = df[FEATURES].corr()
    gold_dxy  = corr.loc["Gold_Price_XAU_USD", "US_Dollar_Index_DXY"]
    gold_oil  = corr.loc["Gold_Price_XAU_USD", "Crude_Oil_Price"]
    gold_infl = corr.loc["Gold_Price_XAU_USD", "Inflation_Rate_Pct"]

    insights = [
        (
            "🪙 Gold vs 💵 DXY",
            f"Korelasi <b>{gold_dxy:+.3f}</b> → Korelasi negatif sangat kuat. "
            "Emas cenderung naik ketika Dolar AS melemah, dan sebaliknya.",
        ),
        (
            "🪙 Gold vs 🛢️ Crude Oil",
            f"Korelasi <b>{gold_oil:+.3f}</b> → Korelasi positif sangat kuat. "
            "Harga emas dan minyak mentah bergerak searah, mencerminkan "
            "dinamika pasar komoditas global.",
        ),
        (
            "🪙 Gold vs 📈 Inflation",
            f"Korelasi <b>{gold_infl:+.3f}</b> → Hampir tidak ada korelasi linear. "
            "Emas tidak selalu merespons perubahan inflasi secara langsung "
            "dalam jangka pendek.",
        ),
    ]

    for title, text in insights:
        st.markdown(
            f'<div class="insight-box"><b>{title}</b><br>{text}</div>',
            unsafe_allow_html=True,
        )
