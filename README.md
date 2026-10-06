# Exploratory Data Analysis (EDA) — Online Retail Dataset

Proyek analisis data eksploratif untuk memenuhi **Tugas Sub-CLO-12-1-1: Visualisasi Data & Analitika**. Proyek ini menganalisis dataset transaksi nyata e-commerce ritel daring berbasis di Britania Raya (*United Kingdom*) periode 2010–2011 dari *UCI Machine Learning Repository*.

---

## Identitas Mahasiswa
* **Nama Lengkap** : Muhammad Aulia Muzzaki Nugraha
* **NIM**          : 2311102051
* **Mata Kuliah**  : Visualisasi Data & Analitika
* **Dataset Resmi**: [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail) (541.909 baris × 8 kolom)

---

## Struktur Repositori

```text
├── Muhammad Aulia Muzzaki Nugraha_2311102051_TugasEDA.ipynb  # Notebook utama (analisis, grafik & interpretasi)
├── DEKLARASI_PENGGUNAAN_AI.md                                 # Deklarasi resmi etika AI & transkrip prompting
├── Muhammad Aulia Muzzaki Nugraha_2311102051_ScreenshotAI.png # Bukti tangkapan layar penggunaan AI
├── data/
│   └── online_retail.csv                                     # Dataset transaksi UCI Online Retail
├── Tugas Sub-CLO-12-1-1 - Visualisasi Data.pdf               # Panduan resmi penugasan
├── pyproject.toml / uv.lock                                  # Manajemen dependensi lingkungan kerja Python
└── README.md                                                 # Ringkasan proyek
```

---

## Alur Analisis (EDA Pipeline)

1. **Data Profiling & Validasi Data**: Pemeriksaan 541.909 baris data mentah, deteksi 5.268 duplikat identik, identifikasi 24,9% *guest checkout*, serta deteksi anomali faktur pembatalan (kode 'C') dan *outlier* berpasangan simetris (±80.995 unit).
2. **Data Cleaning & Rekayasa Fitur**: Retensi 519.699 baris data bersih (95,9%) dan pembentukan tabel analitik 4.324 pelanggan terdaftar dengan metrik **RFM+** (*Recency, Frequency, Monetary, Average Order Value, Diversity, Tenure*).
3. **Univariate Visualization**: Analisis distribusi log-normal pada transaksi dan validasi empiris Hukum Pareto (20% pelanggan menyumbang 73,7% omset).
4. **Bivariate Visualization**: Korelasi rank Spearman $\rho = 0,814$ (Frequency vs Monetary), kurva non-parametrik Recency, dan uji signifikansi Mann-Whitney U pada AOV ekspor ($p = 3,08 \times 10^{-22}$).
5. **Multivariate Visualization**: Matriks korelasi Pearson vs Spearman serta Scatterplot Matrix (*Pairplot*) dengan skala logaritmik.
6. **Dimensionality Reduction (PCA & Nilai Tambah)**: Reduksi dimensi berbasis PCA (kumulatif PC1–PC3 sebesar 76,57%), visualisasi Biplot 2D, proyeksi 3D, serta Dendrogram *Hierarchical Clustering* (metode Ward).
7. **Insight & Rekomendasi Bisnis**: Sintesis 5 temuan strategis retail e-commerce dan rekomendasi fitur untuk pemodelan *Machine Learning* lanjutan.

---

## Cara Menjalankan Notebook

1. **Prasyarat**: Python 3.10+ (disarankan Python 3.12)
2. **Instalasi Dependensi**:
   ```bash
   pip install numpy pandas matplotlib seaborn scipy scikit-learn
   ```
   *atau jika menggunakan `uv`:*
   ```bash
   uv sync
   ```
3. **Menjalankan Analisis**:
   Buka berkas `Muhammad Aulia Muzzaki Nugraha_2311102051_TugasEDA.ipynb` pada Jupyter Notebook atau VS Code, lalu jalankan seluruh sel (**Run All**). Seluruh sel kode dirancang deterministik dan bebas galat.
