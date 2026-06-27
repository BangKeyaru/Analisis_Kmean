# =============================================================================
# pages/page_evaluasi.py
# Halaman 2: Evaluasi Model & K-Means Clustering
# =============================================================================

import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

from config import (
    FEATURES, CLUSTER_LABELS, CLUSTER_COLORS,
    CLUSTER_ICONS, CLUSTER_DESCRIPTIONS,
)
from utils.model import compute_evaluation_metrics


# ---------------------------------------------------------------------------
# Entry point halaman
# ---------------------------------------------------------------------------

def render(
    df_result: pd.DataFrame,
    X_scaled: np.ndarray,
    kmeans: KMeans,
    pca: PCA,
) -> None:
    """
    Menampilkan seluruh konten Halaman 2:
      - Metric cards evaluasi (Silhouette, DBI)
      - Grafik Elbow Method & Silhouette Score
      - Scatter Plot PCA 2D hasil clustering
      - Tabel rata-rata per cluster
      - Kartu interpretasi cluster

    Args:
        df_result : DataFrame lengkap dengan kolom Cluster, PC1, PC2.
        X_scaled  : Array data yang sudah distandarisasi.
        kmeans    : Model KMeans yang sudah di-fit.
        pca       : Model PCA yang sudah di-fit.
    """
    k_range, wcss_list, sil_list, dbi_list = compute_evaluation_metrics(X_scaled)

    _render_metric_cards(k_range, sil_list, dbi_list)
    _render_elbow_silhouette(k_range, wcss_list, sil_list)
    _render_pca_scatter(df_result, kmeans, pca)
    _render_cluster_table(df_result)
    _render_cluster_cards()


# ---------------------------------------------------------------------------
# Sub-fungsi private
# ---------------------------------------------------------------------------

def _render_metric_cards(
    k_range: list, sil_list: list, dbi_list: list
) -> None:
    """Menampilkan tiga metric card: k terpilih, silhouette, dan DBI."""
    st.markdown(
        '<p class="section-title" style="margin-top:0">📈 Evaluasi Model K-Means</p>',
        unsafe_allow_html=True,
    )
    idx_k3 = k_range.index(3)
    c1, c2, c3 = st.columns(3)
    c1.metric("Cluster Terpilih (k)",         "3")
    c2.metric("Silhouette Score (k=3)",        f"{sil_list[idx_k3]:.4f}")
    c3.metric("Davies-Bouldin Index (k=3)",    f"{dbi_list[idx_k3]:.4f}")


def _render_elbow_silhouette(
    k_range: list, wcss_list: list, sil_list: list
) -> None:
    """Menampilkan grafik garis Elbow Method dan Silhouette Score berdampingan."""
    st.markdown(
        '<p class="section-title">📉 Elbow Method & Silhouette Score</p>',
        unsafe_allow_html=True,
    )

    theme = st.session_state.get("theme", "dark")
    is_dark = (theme == "dark")
    
    fig_bg = "#121324" if is_dark else "#f8fafc"
    ax_bg = "#1a1d3a" if is_dark else "#ffffff"
    text_color = "#ffd700" if is_dark else "#b89600"
    label_color = "#94a3b8" if is_dark else "#475569"
    tick_color = "#cbd5e1" if is_dark else "#1e293b"
    legend_bg = "#252545" if is_dark else "#f1f5f9"
    spine_color = "#3a3a5a" if is_dark else "#cbd5e1"
    grid_color = "#2a2a4a" if is_dark else "#e2e8f0"

    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
    for ax in axes:
        ax.set_facecolor(ax_bg)
    fig.patch.set_facecolor(fig_bg)

    # -- Elbow (WCSS) --
    axes[0].plot(k_range, wcss_list, marker="o", color=text_color,
                 linewidth=2.2, markersize=7, markerfacecolor="#ff9900")
    axes[0].axvline(x=3, color="#E84393", linestyle="--",
                    linewidth=1.5, alpha=0.8, label="k=3 (terpilih)")
    axes[0].set_title("Elbow Method – WCSS",
                       color=text_color, fontsize=12, fontweight="bold")
    axes[0].set_xlabel("Jumlah Cluster (k)", color=label_color)
    axes[0].set_ylabel("Within-Cluster Sum of Squares", color=label_color)
    axes[0].tick_params(colors=tick_color)
    axes[0].legend(facecolor=legend_bg, labelcolor=tick_color)
    axes[0].spines[:].set_color(spine_color)
    axes[0].grid(axis="y", color=grid_color, linestyle="--", alpha=0.5)

    # -- Silhouette Score --
    axes[1].plot(k_range, sil_list, marker="s", color="#00C9A7",
                 linewidth=2.2, markersize=7, markerfacecolor="#00ffc8")
    axes[1].axvline(x=3, color="#E84393", linestyle="--",
                    linewidth=1.5, alpha=0.8, label="k=3 (terpilih)")
    axes[1].set_title("Silhouette Score",
                       color="#00C9A7", fontsize=12, fontweight="bold")
    axes[1].set_xlabel("Jumlah Cluster (k)", color=label_color)
    axes[1].set_ylabel("Silhouette Score",   color=label_color)
    axes[1].tick_params(colors=tick_color)
    axes[1].legend(facecolor=legend_bg, labelcolor=tick_color)
    axes[1].spines[:].set_color(spine_color)
    axes[1].grid(axis="y", color=grid_color, linestyle="--", alpha=0.5)

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)


def _render_pca_scatter(
    df_result: pd.DataFrame, kmeans: KMeans, pca: PCA
) -> None:
    """
    Menampilkan scatter plot 2D hasil proyeksi PCA,
    dengan titik diwarnai berdasarkan label cluster.
    """
    st.markdown(
        '<p class="section-title">🎯 Scatter Plot Cluster (PCA 2D)</p>',
        unsafe_allow_html=True,
    )

    explained = pca.explained_variance_ratio_ * 100

    theme = st.session_state.get("theme", "dark")
    is_dark = (theme == "dark")
    
    fig_bg = "#121324" if is_dark else "#f8fafc"
    ax_bg = "#1a1d3a" if is_dark else "#ffffff"
    label_color = "#94a3b8" if is_dark else "#475569"
    title_color = "#ffd700" if is_dark else "#b89600"
    tick_color = "#cbd5e1" if is_dark else "#1e293b"
    legend_bg = "#252545" if is_dark else "#f1f5f9"
    spine_color = "#3a3a5a" if is_dark else "#cbd5e1"
    grid_color = "#2a2a4a" if is_dark else "#e2e8f0"

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(fig_bg)
    ax.set_facecolor(ax_bg)

    for cid in sorted(df_result["Cluster"].unique()):
        mask = df_result["Cluster"] == cid
        ax.scatter(
            df_result.loc[mask, "PC1"],
            df_result.loc[mask, "PC2"],
            c=CLUSTER_COLORS[cid],
            label=f"Cluster {cid}: {CLUSTER_LABELS[cid]}",
            alpha=0.72,
            edgecolors="none",
            s=38,
        )

    # Centroid diproyeksikan ke ruang PCA
    centers_pca = pca.transform(kmeans.cluster_centers_)
    ax.scatter(
        centers_pca[:, 0], centers_pca[:, 1],
        marker="X", s=220, c="white",
        edgecolors=title_color, linewidths=1.5,
        zorder=5, label="Centroid",
    )

    ax.set_xlabel(f"PC1 ({explained[0]:.1f}% Variance)", color=label_color, fontsize=10)
    ax.set_ylabel(f"PC2 ({explained[1]:.1f}% Variance)", color=label_color, fontsize=10)
    ax.set_title(
        "Hasil K-Means Clustering (k=3) – Proyeksi PCA 2D",
        color=title_color, fontsize=13, fontweight="bold",
    )
    ax.tick_params(colors=tick_color)
    ax.spines[:].set_color(spine_color)
    ax.grid(color=grid_color, linestyle="--", alpha=0.4)
    ax.legend(facecolor=legend_bg, labelcolor=tick_color,
               fontsize=8.5, loc="upper right")

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    total_var = explained.sum()
    st.info(
        f"📐 PC1 menjelaskan **{explained[0]:.1f}%** variance dan "
        f"PC2 menjelaskan **{explained[1]:.1f}%** variance "
        f"(total **{total_var:.1f}%**)."
    )


def _render_cluster_table(df_result: pd.DataFrame) -> None:
    """Menampilkan tabel rata-rata nilai asli (non-scaled) per cluster."""
    st.markdown(
        '<p class="section-title">📌 Karakteristik & Interpretasi Cluster</p>',
        unsafe_allow_html=True,
    )

    stats = (
        df_result.groupby("Cluster")[FEATURES]
        .mean()
        .round(4)
        .rename(columns={
            "Gold_Price_XAU_USD": "Harga Emas (USD)",
            "US_Dollar_Index_DXY": "Indeks DXY",
            "Crude_Oil_Price":    "Harga Minyak",
            "Inflation_Rate_Pct": "Inflasi (%)",
        })
    )
    stats["Label"] = [CLUSTER_LABELS[i] for i in stats.index]

    st.dataframe(
        stats.style
            .format({
                "Harga Emas (USD)": "{:,.2f}",
                "Indeks DXY":       "{:.2f}",
                "Harga Minyak":     "{:.2f}",
                "Inflasi (%)":      "{:.4f}",
            })
            .background_gradient(cmap="YlOrBr", subset=["Harga Emas (USD)"]),
        use_container_width=True,
    )


def _render_cluster_cards() -> None:
    """Menampilkan kartu narasi interpretasi untuk setiap cluster."""
    for cid, (bg, border, title, desc) in CLUSTER_DESCRIPTIONS.items():
        st.markdown(
            f"""
            <div class="cluster-card" style="background:{bg}; border-color:{border}40;">
                <h4 style="color:{border};">{CLUSTER_ICONS[cid]} {title}</h4>
                <p>{desc}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
