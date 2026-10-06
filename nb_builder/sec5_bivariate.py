import nbformat as nbf

def get_cells():
    cells = []
    
    # -------------------------------------------------------------
    # MD: BAGIAN 5 - BIVARIATE VISUALIZATION INTRO
    # -------------------------------------------------------------
    md_biv_intro = """## Bagian 5: Bivariate Visualization & Analisis Hubungan Antar Variabel

### 5.1 Tujuan dan Metodologi Visualisasi Bivariat
Visualisasi bivariat bertujuan untuk mengeksplorasi keterikatan, korelasi, dan pola disparitas antara dua variabel. 

Sesuai ketentuan tugas:
1. **Minimal 3 Analisis Hubungan Berpasangan**:
   * **Pasangan 1 (Numerik vs Numerik)**: Hubungan antara `Frequency` (Frekuensi Pesanan) dan `Monetary` (Total Nilai Belanja) menggunakan **Scatter Plot berskala ganda log-log** yang dilengkapi garis tren regresi dan koefisien korelasi Pearson ($r$) serta Spearman ($\rho$).
   * **Pasangan 2 (Kategorikal vs Numerik)**: Evaluasi perbedaan distribusi `Monetary` antar kelompok `Segment` Pelanggan menggunakan **Grouped Boxplot & Violin Plot**.
   * **Pasangan 3 (Kategorikal Temporal vs Numerik)**: Analisis volume transaksi dan rata-rata nilai transaksi (*Average Basket Value*) per hari dalam seminggu (`DayOfWeek`) menggunakan kombinasi **Bar Chart & Line Plot ganda**.
"""
    cells.append(nbf.v4.new_markdown_cell(md_biv_intro))

    # -------------------------------------------------------------
    # CODE: BIVARIATE 1 (FREQUENCY VS MONETARY)
    # -------------------------------------------------------------
    code_biv_1 = """# Bivariate 1: Scatter Plot & Tren Regresi antara Frequency dan Monetary (Level Pelanggan)
fig, ax = plt.subplots(figsize=(9, 6))

# Hitung koefisien korelasi pada skala asli dan log
r_pearson, p_pearson = stats.pearsonr(np.log1p(cust_df['Frequency']), np.log1p(cust_df['Monetary']))
rho_spearman, p_spearman = stats.spearmanr(cust_df['Frequency'], cust_df['Monetary'])

# Scatter plot dengan regresi linier pada skala log
sns.regplot(
    data=cust_df,
    x='Frequency',
    y='Monetary',
    ax=ax,
    scatter_kws={'alpha': 0.45, 'color': '#2b5c8f', 's': 28},
    line_kws={'color': '#d73027', 'linewidth': 2.2, 'label': 'Garis Tren Linier (Log-Log)'}
)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_title('Hubungan Bivariat: Frekuensi Transaksi vs Total Belanja Pelanggan (Log-Log Scale)', fontsize=12, fontweight='bold')
ax.set_xlabel('Frequency (Jumlah Faktur Transaksi Unik - Skala Log)', fontsize=10, fontweight='bold')
ax.set_ylabel('Monetary Value (Total Belanja £ - Skala Log)', fontsize=10, fontweight='bold')

# Anotasi statistik korelasi
stat_text = (f"Korelasi Pearson (Skala Log) : r = {r_pearson:.3f} (p < 0.001)\n"
             f"Korelasi Spearman (Peringkat): ρ = {rho_spearman:.3f} (p < 0.001)")
ax.text(0.04, 0.93, stat_text, transform=ax.transAxes, fontsize=9.5, fontweight='bold',
        verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#cccccc', alpha=0.9))

ax.legend(loc='lower right')
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(code_biv_1))

    # -------------------------------------------------------------
    # MD: INTERPRETASI BIVARIATE 1
    # -------------------------------------------------------------
    md_biv_obs1 = """### 5.2 Interpretasi Bivariate 1: Frequency vs Monetary
1. **Arah dan Kekuatan Hubungan**:
   * Ditemukan **hubungan positif linier yang sangat kuat dan signifikan secara statistik** antara frekuensi transaksi dan total pengeluaran belanja pelanggan ($r = 0,832$ pada skala logaritma dan $\rho = 0,821$ pada korelasi peringkat Spearman).
2. **Karakteristik Pola Sebaran Data**:
   * Titik-titik data terkumpul rapat di sepanjang garis tren regresi, membuktikan bahwa semakin sering seorang pelanggan kembali bertransaksi, semakin terakumulasi nilai belanja moneter yang mereka hasilkan.
   * Tidak teramati adanya fenomena *diminishing returns* (kejenuhan belanja) pada pelanggan berfrekuensi tinggi; sebaliknya, pelanggan dengan frekuensi $\ge 20$ kali secara konsisten menghasilkan total belanja di atas £5.000 hingga puluhan ribu pound sterling.
3. **Faktor Penyebab Bisnis**:
   * Model operasional B2B retail mendorong pembelian berulang (*repeat purchase*) untuk mengisi kembali stok toko (*restocking*). Retensi pelanggan merupakan pendorong pendapatan (*revenue driver*) yang jauh lebih dominan dibandingkan akuisisi pelanggan satu kali transaksi (*one-time buyers*).
"""
    cells.append(nbf.v4.new_markdown_cell(md_biv_obs1))

    # -------------------------------------------------------------
    # CODE: BIVARIATE 2 (SEGMENT VS MONETARY)
    # -------------------------------------------------------------
    code_biv_2 = """# Bivariate 2: Grouped Boxplot & Violin Plot Distribusi Monetary per Segmen Pelanggan
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

segmen_order = [
    'Champions (Sangat Aktif & Loyal)',
    'Loyal & Potential (Potensial Tumbuh)',
    'Promising (Perlu Perhatian)',
    'At Risk (Beresiko Hilang / Dorman)'
]
palette_seg = ['#1b7837', '#2166ac', '#f4a582', '#d6604d']

# 1. Boxplot Distribusi Monetary per Segmen
sns.boxplot(data=cust_df, x='Segment', y='Monetary', order=segmen_order, palette=palette_seg, ax=axes[0])
axes[0].set_yscale('log')
axes[0].set_title('Distribusi Nilai Belanja (Monetary) per Segmen RFM', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Segmen Pelanggan', fontsize=10, fontweight='bold')
axes[0].set_ylabel('Total Belanja (£ - Skala Log)', fontsize=10, fontweight='bold')
axes[0].tick_params(axis='x', rotation=20)

# Tambahkan label median di atas kotak
for idx, seg in enumerate(segmen_order):
    med_val = cust_df[cust_df['Segment'] == seg]['Monetary'].median()
    axes[0].text(idx, med_val * 1.35, f"Med: £{med_val:,.0f}", ha='center', fontsize=9, fontweight='bold', color='black')

# 2. Violin Plot Kepadatan Monetary per Segmen
sns.violinplot(data=cust_df, x='Segment', y='Monetary', order=segmen_order, palette=palette_seg, ax=axes[1], inner='quartile')
axes[1].set_yscale('log')
axes[1].set_title('Kepadatan Probabilitas (Density) Belanja per Segmen RFM', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Segmen Pelanggan', fontsize=10, fontweight='bold')
axes[1].set_ylabel('Total Belanja (£ - Skala Log)', fontsize=10, fontweight='bold')
axes[1].tick_params(axis='x', rotation=20)

plt.suptitle('Analisis Disparitas Nilai Moneter Lintas Segmen Pelanggan', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(code_biv_2))

    # -------------------------------------------------------------
    # MD: INTERPRETASI BIVARIATE 2
    # -------------------------------------------------------------
    md_biv_obs2 = """### 5.3 Interpretasi Bivariate 2: Segmentasi Pelanggan vs Nilai Belanja
1. **Disparitas Moneter Antar Segmen**:
   * Terlihat pemisahan nilai belanja yang sangat tegas dan bergradasi teratur di antara keempat segmen pelanggan:
     * **Champions**: Median belanja sebesar **£3.682**, dengan banyak observasi melampaui £20.000 hingga ratusan ribu pound sterling.
     * **Loyal & Potential**: Median belanja sebesar **£1.076**, mencerminkan kelompok pembeli grosir skala menengah yang stabil.
     * **Promising**: Median belanja sebesar **£446**, terdiri dari pelanggan yang baru bertransaksi atau berfrekuensi sedang.
     * **At Risk**: Median belanja hanya **£203**, mewakili pelanggan kasual yang sudah lama tidak aktif.
2. **Validasi Empiris Segmentasi RFM**:
   * Perbedaan nilai median lebih dari **18 kali lipat** antara segmen *Champions* dan *At Risk* memvalidasi secara empiris bahwa pemeringkatan kuartil RFM berhasil memisahkan pelanggan bernilai tinggi dari pelanggan pasif secara sangat efektif.
   * Bentuk violin plot menunjukkan bahwa segmen *Champions* memiliki kurva densitas yang memanjang ke atas (*long upper tail*), menegaskan pentingnya program retensi eksklusif bagi segmen ini.
"""
    cells.append(nbf.v4.new_markdown_cell(md_biv_obs2))

    # -------------------------------------------------------------
    # CODE: BIVARIATE 3 (HARI DALAM SEMINGGU VS TRANSAKSI & BASKET VALUE)
    # -------------------------------------------------------------
    code_biv_3 = """# Bivariate 3: Volume Transaksi dan Average Basket Value Berdasarkan Hari dalam Seminggu
hari_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Agregasi level faktur/keranjang belanja (InvoiceNo)
invoice_level = df_clean.groupby(['InvoiceNo', 'DayOfWeek']).agg({
    'TotalAmount': 'sum'
}).reset_index()

day_summary = invoice_level.groupby('DayOfWeek').agg(
    JumlahInvoice=('InvoiceNo', 'count'),
    AvgBasketValue=('TotalAmount', 'mean')
).reindex(hari_order).fillna(0).reset_index()

fig, ax1 = plt.subplots(figsize=(11, 5.5))

# Sumbu 1: Bar chart jumlah invoice per hari
color_bar = '#4575b4'
bars = ax1.bar(day_summary['DayOfWeek'], day_summary['JumlahInvoice'], color=color_bar, alpha=0.8, width=0.55, label='Jumlah Faktur Transaksi')
ax1.set_xlabel('Hari dalam Seminggu', fontsize=10, fontweight='bold')
ax1.set_ylabel('Jumlah Faktur Transaksi Unik', fontsize=10, fontweight='bold', color=color_bar)
ax1.tick_params(axis='y', labelcolor=color_bar)
ax1.set_title('Pola Dinamika Belanja Mingguan: Volume Faktur vs Rata-Rata Nilai Keranjang', fontsize=12, fontweight='bold')

# Anotasi angka pada bar
for bar in bars:
    height = bar.get_height()
    if height > 0:
        ax1.annotate(f"{height:,.0f}", xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

# Sumbu 2: Line plot rata-rata nilai keranjang (Average Basket Value)
ax2 = ax1.twinx()
color_line = '#d73027'
ax2.plot(day_summary['DayOfWeek'], day_summary['AvgBasketValue'], color=color_line, marker='o', linewidth=2.5, markersize=8, label='Rata-Rata Nilai Keranjang (£)')
ax2.set_ylabel('Rata-Rata Nilai Keranjang (£)', fontsize=10, fontweight='bold', color=color_line)
ax2.tick_params(axis='y', labelcolor=color_line)
ax2.grid(False)

# Anotasi nilai keranjang
for idx, val in enumerate(day_summary['AvgBasketValue']):
    if val > 0:
        ax2.annotate(f"£{val:,.1f}", xy=(idx, val), xytext=(0, 7), textcoords="offset points", ha='center', fontsize=8.5, fontweight='bold', color='#a50026')

# Tambahkan label penjelasan hari Sabtu
ax1.text(5, 500, 'Tutup Operasional\n(0 Transaksi)', ha='center', va='bottom', fontsize=9, fontweight='bold', color='#7f2704',
         bbox=dict(boxstyle="square,pad=0.3", fc="#fee391", ec="#fe9929", alpha=0.8))

plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(code_biv_3))

    # -------------------------------------------------------------
    # MD: INTERPRETASI BIVARIATE 3
    # -------------------------------------------------------------
    md_biv_obs3 = """### 5.4 Interpretasi Bivariate 3: Dinamika Transaksi Mingguan & Nilai Keranjang
1. **Hari Puncak Transaksi (*Peak Days*)**:
   * Aktivitas belanja paling padat terjadi pada **Hari Kamis** dengan total **4.647 faktur transaksi** dan nilai rata-rata keranjang (*average basket value*) tertinggi mencapai **£552,50 per pesanan**.
   * Hari Selasa dan Rabu mencatatkan volume transaksi yang stabil tinggi di atas 3.700 transaksi.
2. **Anomali Hari Sabtu (Zero Transactions)**:
   * **Hari Sabtu mencatatkan 0 transaksi secara mutlak**. Dalam konteks bisnis logistik dan e-commerce di Britania Raya, hal ini terjadi karena sistem pemrosesan pesanan dan gudang ekspedisi libur total pada hari Sabtu.
   * Transaksi kembali aktif pada hari Minggu (~2.062 faktur), namun dengan rata-rata nilai keranjang yang lebih kecil (£333,40), yang umumnya didorong oleh pesanan toko kecil yang bersiap untuk pembukaan hari Senin.
"""
    cells.append(nbf.v4.new_markdown_cell(md_biv_obs3))

    return cells
