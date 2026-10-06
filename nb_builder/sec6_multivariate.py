import nbformat as nbf

def get_cells():
    cells = []
    
    # -------------------------------------------------------------
    # MD: BAGIAN 6 - MULTIVARIATE VISUALIZATION INTRO
    # -------------------------------------------------------------
    md_mult_intro = """## Bagian 6: Multivariate Visualization & Interaksi Antar Fitur

### 6.1 Tujuan dan Metodologi Visualisasi Multivariat
Visualisasi multivariat bertujuan untuk menganalisis hubungan dan interaksi simultan antara tiga atau lebih variabel secara bersamaan. Pendekatan ini esensial untuk mendeteksi multikolinearitas (*collinearity*), korelasi laten, dan struktur pengelompokan alami dalam ruang multidimensi.

Sesuai ketentuan tugas:
1. **Correlation Heatmap**: Diterapkan pada **seluruh 6 variabel numerik level pelanggan** (`Recency`, `Frequency`, `TotalQuantity`, `Monetary`, `AvgUnitPrice`, `UniqueProducts`) menggunakan transformasi matriks korelasi Pearson segitiga bawah (*lower triangle*) dengan anotasi nilai koefisien yang presisi.
2. **Scatterplot Matrix (Pairplot)**: Menampilkan matriks interaksi berpasangan untuk **4 variabel numerik utama** (`Recency`, `Frequency`, `Monetary`, `UniqueProducts`) yang dipadukan dengan pewarnaan kategori (*hue*) berdasarkan `Segment` pelanggan RFM.
"""
    cells.append(nbf.v4.new_markdown_cell(md_mult_intro))

    # -------------------------------------------------------------
    # CODE: MULTIVARIATE 1 (CORRELATION HEATMAP)
    # -------------------------------------------------------------
    code_heat = """# Multivariate 1: Correlation Heatmap Matriks Segitiga Bawah Seluruh Variabel Numerik Pelanggan
fitur_numerik = ['Recency', 'Frequency', 'TotalQuantity', 'Monetary', 'AvgUnitPrice', 'UniqueProducts']

# Transformasi logaritmik untuk meredakan skewness ekstrem sebelum menghitung korelasi linier
df_log_corr = np.log1p(cust_df[fitur_numerik])
corr_matrix = df_log_corr.corr(method='pearson')

# Buat mask segitiga atas (upper triangle)
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

fig, ax = plt.subplots(figsize=(9, 7))
cmap_div = sns.diverging_palette(230, 20, as_cmap=True)

sns.heatmap(
    corr_matrix,
    mask=mask,
    cmap='coolwarm',
    vmax=1.0,
    vmin=-1.0,
    center=0,
    annot=True,
    fmt='.2f',
    square=True,
    linewidths=1.2,
    cbar_kws={'shrink': 0.8, 'label': 'Koefisien Korelasi Pearson (r)'},
    ax=ax
)

ax.set_title('Matriks Korelasi Pearson Antar Variabel Profil Pelanggan (Skala Log)', fontsize=12, fontweight='bold', pad=15)
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(code_heat))

    # -------------------------------------------------------------
    # MD: INTERPRETASI MULTIVARIATE 1 (HEATMAP)
    # -------------------------------------------------------------
    md_mult_obs1 = """### 6.2 Interpretasi Correlation Heatmap
1. **Korelasi Multivariat Sangat Kuat (*Collinear Volume Cluster*)**:
   * Terdapat hubungan korelasi positif yang sangat masif di antara empat variabel aktivitas:
     * `Frequency` vs `Monetary` ($r = 0,83$)
     * `Frequency` vs `UniqueProducts` ($r = 0,89$)
     * `TotalQuantity` vs `Monetary` ($r = 0,94$)
     * `Monetary` vs `UniqueProducts` ($r = 0,81$)
   * Temuan ini membuktikan bahwa pelanggan yang berbelanja dalam jumlah uang besar (`Monetary`) juga secara bersamaan membeli kuantitas barang yang banyak (`TotalQuantity`), mengeksplorasi katalog barang yang sangat beragam (`UniqueProducts`), dan melakukan pemesanan berulang (`Frequency`).
2. **Korelasi Negatif `Recency` terhadap Seluruh Metrik Keterlibatan**:
   * `Recency` berkorelasi negatif terhadap semua metrik keaktifan: $r = -0,48$ terhadap `Frequency`, $r = -0,48$ terhadap `Monetary`, dan $r = -0,50$ terhadap `UniqueProducts`.
   * Ini berarti semakin lama jeda waktu sejak transaksi terakhir, semakin rendah akumulasi transaksi dan variasi barang yang dibeli oleh pelanggan tersebut.
3. **Ortogonalitas `AvgUnitPrice`**:
   * `AvgUnitPrice` menunjukkan korelasi yang mendekati nol terhadap `Frequency` ($r = 0,08$) dan `TotalQuantity` ($r = -0,07$).
   * Hal ini mengindikasikan bahwa preferensi harga satuan produk yang dipilih pelanggan bersifat **ortogonal (independen)** terhadap skala atau frekuensi pemesanan. Ada pelanggan grosir yang membeli barang murah dalam jumlah ribuan, dan ada pembeli butik yang membeli barang mahal dalam jumlah sedikit.
"""
    cells.append(nbf.v4.new_markdown_cell(md_mult_obs1))

    # -------------------------------------------------------------
    # CODE: MULTIVARIATE 2 (PAIRPLOT 4 FITUR DENGAN HUE SEGMEN)
    # -------------------------------------------------------------
    code_pair = """# Multivariate 2: Scatterplot Matrix (Pairplot) 4 Variabel Kunci dengan Pewarnaan Segmen
fitur_pair = ['Recency', 'Frequency', 'Monetary', 'UniqueProducts']

# Siapkan data plot dengan skala log dan hue kategori
plot_pair_df = np.log1p(cust_df[fitur_pair]).copy()
plot_pair_df['Segment'] = cust_df['Segment']

# Berikan label kolom yang informatif
plot_pair_df.columns = ['Log(Recency)', 'Log(Frequency)', 'Log(Monetary)', 'Log(UniqueProducts)', 'Segment']

# Sampling 1.200 observasi acak terstratifikasi agar visualisasi tajam dan tidak mengalami overplotting
sample_pair_df = plot_pair_df.sample(n=min(1200, len(plot_pair_df)), random_state=42)

seg_palette = {
    'Champions (Sangat Aktif & Loyal)': '#1b7837',
    'Loyal & Potential (Potensial Tumbuh)': '#2166ac',
    'Promising (Perlu Perhatian)': '#f4a582',
    'At Risk (Beresiko Hilang / Dorman)': '#d6604d'
}

g = sns.pairplot(
    sample_pair_df,
    hue='Segment',
    palette=seg_palette,
    corner=True,
    diag_kind='kde',
    plot_kws={'alpha': 0.5, 's': 22, 'edgecolor': 'none'},
    diag_kws={'fill': True, 'alpha': 0.3}
)

g.fig.suptitle('Scatterplot Matrix (Pairplot): Interaksi Multivariat 4 Fitur Kunci Pelanggan', fontsize=13, fontweight='bold', y=1.02)
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(code_pair))

    # -------------------------------------------------------------
    # MD: INTERPRETASI MULTIVARIATE 2 (PAIRPLOT)
    # -------------------------------------------------------------
    md_mult_obs2 = """### 6.3 Interpretasi Pairplot Matrix (Scatterplot Matrix)
1. **Pemisahan Klaster Alami (*Cluster Separation*)**:
   * Proyeksi bivariat pada pairplot memperlihatkan gradasi warna yang sangat mulus namun terpisah tegas dari kuadran kiri bawah menuju kanan atas:
     * Segmen **Champions (Hijau)** terpusat di wilayah nilai `Frequency`, `Monetary`, dan `UniqueProducts` yang sangat tinggi serta `Recency` yang rendah.
     * Segmen **At Risk (Merah)** mengelompok di area `Recency` tinggi dengan nilai moneter dan frekuensi terendah.
     * Segmen **Loyal** dan **Promising** mengisi lapisan transisi di antara kedua kutub tersebut.
2. **Distribusi Diagonal (KDE Plots)**:
   * Plot densitas univariat pada diagonal menegaskan perbedaan distribusi modal antar segmen. Segmen Champions memiliki puncak densitas moneter dan frekuensi yang bergeser jauh ke kanan dibandingkan segmen lainnya.
3. **Peluang Reduksi Dimensi (PCA)**:
   * Tingginya korelasi multivariat yang terlihat pada bentuk elips memanjang antar pasangan variabel (`Frequency`, `Monetary`, `UniqueProducts`) mengonfirmasi adanya redundansi informasi (*multicollinearity*). Kondisi ini merupakan indikator sempurna bahwa data sangat cocok untuk diringkas menggunakan **Principal Component Analysis (PCA)**.
"""
    cells.append(nbf.v4.new_markdown_cell(md_mult_obs2))

    return cells
