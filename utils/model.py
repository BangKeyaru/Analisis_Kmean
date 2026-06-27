# =============================================================================
# utils/model.py
# Bertanggung jawab untuk: pelatihan pipeline ML (Scaler → KMeans → PCA)
# dan kalkulasi metrik evaluasi (WCSS, Silhouette, DBI).
# =============================================================================

import io
import numpy as np
import pandas as pd
import streamlit as st

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, davies_bouldin_score

from config import FEATURES, CLUSTER_LABELS


# ---------------------------------------------------------------------------
# Pipeline Utama: Standarisasi → KMeans → PCA
# ---------------------------------------------------------------------------

@st.cache_resource(show_spinner="⚙️ Melatih model K-Means …")
def train_pipeline(csv_bytes: bytes):
    """
    Melatih pipeline lengkap dari bytes CSV:
      1. Parse CSV
      2. Standarisasi Z-Score (StandardScaler)
      3. K-Means Clustering (k=3, Euclidean Distance)
      4. PCA 2D untuk visualisasi

    Menggunakan @st.cache_resource agar model hanya dilatih sekali
    selama sesi berlangsung (tidak diulang saat interaksi UI).

    Args:
        csv_bytes: Isi file CSV dalam bentuk bytes.

    Returns:
        df_raw    – DataFrame asli
        X_scaled  – Array numpy setelah standarisasi
        scaler    – StandardScaler yang sudah di-fit
        kmeans    – KMeans model yang sudah di-fit
        pca       – PCA model yang sudah di-fit
        df_result – DataFrame dengan kolom Cluster, PC1, PC2
    """
    # 1. Baca data
    df = pd.read_csv(io.BytesIO(csv_bytes), parse_dates=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    # 2. Standarisasi Z-Score: Z = (X - μ) / σ
    scaler   = StandardScaler()
    X_scaled = scaler.fit_transform(df[FEATURES])

    # 3. K-Means Clustering (k=3, init k-means++, Euclidean Distance)
    kmeans = KMeans(
        n_clusters=3,
        init="k-means++",
        n_init=20,
        max_iter=300,
        random_state=42,
    )
    labels = kmeans.fit_predict(X_scaled)

    # 4. PCA → 2 komponen untuk visualisasi scatter plot
    pca        = PCA(n_components=2, random_state=42)
    pca_coords = pca.fit_transform(X_scaled)

    # 5. Gabungkan hasil ke DataFrame
    df_result            = df.copy()
    df_result["Cluster"] = labels
    df_result["PC1"]     = pca_coords[:, 0]
    df_result["PC2"]     = pca_coords[:, 1]

    return df, X_scaled, scaler, kmeans, pca, df_result


# ---------------------------------------------------------------------------
# Metrik Evaluasi: WCSS (Elbow), Silhouette, Davies-Bouldin Index
# ---------------------------------------------------------------------------

@st.cache_data(show_spinner="📐 Menghitung metrik evaluasi …")
def compute_evaluation_metrics(_X_scaled: np.ndarray):
    """
    Menghitung tiga metrik evaluasi untuk k = 2 hingga 10.

    Underscore prefix pada _X_scaled menonaktifkan hashing cache
    Streamlit untuk array numpy (numpy arrays tidak hashable secara default).

    Args:
        _X_scaled: Array data yang sudah distandarisasi.

    Returns:
        k_range   – list nilai k
        wcss_list – list WCSS per k (Elbow Method)
        sil_list  – list Silhouette Score per k
        dbi_list  – list Davies-Bouldin Index per k
    """
    k_range   = range(2, 11)
    wcss_list, sil_list, dbi_list = [], [], []

    for k in k_range:
        km    = KMeans(n_clusters=k, init="k-means++", n_init=10,
                       max_iter=300, random_state=42)
        preds = km.fit_predict(_X_scaled)
        wcss_list.append(km.inertia_)
        sil_list.append(silhouette_score(_X_scaled, preds))
        dbi_list.append(davies_bouldin_score(_X_scaled, preds))

    return list(k_range), wcss_list, sil_list, dbi_list
