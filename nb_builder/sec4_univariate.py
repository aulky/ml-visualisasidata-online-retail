import nbformat as nbf

def get_cells():
    cells = []
    
    # -------------------------------------------------------------
    # MD: BAGIAN 4 - UNIVARIATE VISUALIZATION INTRO
    # -------------------------------------------------------------
    md_univ_intro = """## Bagian 4: Univariate Visualization & Analisis Distribusi

### 4.1 Tujuan dan Metodologi Visualisasi Univariat
Visualisasi univariat bertujuan untuk menganalisis karakteristik distribusi setiap variabel secara individual tanpa mempertimbangkan keterhubungannya dengan variabel lain. 

Sesuai ketentuan pedoman tugas:
1. **Minimal 3 Variabel Numerik**: Dianalisis menggunakan kombinasi **Histogram, Kernel Density Estimation (KDE), dan Boxplot**. Pada analisis ini, dieksplorasi 4 variabel numerik representatif dari level transaksi dan level pelanggan:
   * `Quantity` (Kuantitas per transaksi)
   * `UnitPrice` (Harga satuan barang)
   * `Recency` (Jeda waktu keaktifan pelanggan dalam hari)
   * `Monetary` (Total akumulasi nilai belanja pelanggan dalam £)
2. **Minimal 2 Variabel Kategorikal**: Dianalisis menggunakan **Bar Chart berurutan** dengan anotasi frekuensi dan proporsi persentase:
   * `Country` (Top 10 Destinasi Ekspor Pasar Internasional)
   * `Hour` (Pola Distribusi Jam Transaksi dalam Sehari)
"""
    cells.append(nbf.v4.new_markdown_cell(md_univ_intro))

    # -------------------------------------------------------------
    # CODE: UNIVARIATE NUMERIK 1 & 2 (QUANTITY & UNITPRICE)
    # -------------------------------------------------------------
    code_num_1_2 = """# Visualisasi Univariat Numerik 1 & 2: Distribusi Quantity dan UnitPrice pada Level Transaksi
fig, axes = plt.subplots(2, 2, figsize=(14, 9))

# 1. Histogram & KDE: Quantity (Skala Logaritmik)
sns.histplot(df_clean['Quantity'], bins=50, kde=True, ax=axes[0, 0], color='#2b5c8f', log_scale=True)
median_q = df_clean['Quantity'].median()
mean_q = df_clean['Quantity'].mean()
axes[0, 0].axvline(median_q, color='red', linestyle='--', linewidth=2, label=f'Median = {median_q:.0f}')
axes[0, 0].axvline(mean_q, color='gold', linestyle='-', linewidth=2, label=f'Mean = {mean_q:.2f}')
axes[0, 0].set_title('Distribusi Kuantitas Barang per Transaksi (Log Scale)', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Kuantitas Barang (Unit - Skala Log)', fontsize=10, fontweight='bold')
axes[0, 0].set_ylabel('Frekuensi Transaksi', fontsize=10, fontweight='bold')
axes[0, 0].legend(loc='upper right')

# 2. Boxplot: Quantity (Skala Logaritmik)
sns.boxplot(x=df_clean['Quantity'], ax=axes[0, 1], color='#6baed6', fliersize=3)
axes[0, 1].set_xscale('log')
axes[0, 1].axvline(median_q, color='red', linestyle='--', linewidth=2, label=f'Median = {median_q:.0f}')
axes[0, 1].set_title('Boxplot Kuantitas Barang per Transaksi (Log Scale)', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Kuantitas Barang (Unit - Skala Log)', fontsize=10, fontweight='bold')
axes[0, 1].legend(loc='upper right')

# 3. Histogram & KDE: UnitPrice (Skala Logaritmik)
sns.histplot(df_clean['UnitPrice'], bins=50, kde=True, ax=axes[1, 0], color='#238b45', log_scale=True)
median_p = df_clean['UnitPrice'].median()
mean_p = df_clean['UnitPrice'].mean()
axes[1, 0].axvline(median_p, color='red', linestyle='--', linewidth=2, label=f'Median = £{median_p:.2f}')
axes[1, 0].axvline(mean_p, color='gold', linestyle='-', linewidth=2, label=f'Mean = £{mean_p:.2f}')
axes[1, 0].set_title('Distribusi Harga Satuan Barang per Transaksi (Log Scale)', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Harga Satuan (£ - Skala Log)', fontsize=10, fontweight='bold')
axes[1, 0].set_ylabel('Frekuensi Transaksi', fontsize=10, fontweight='bold')
axes[1, 0].legend(loc='upper right')

# 4. Boxplot: UnitPrice (Skala Logaritmik)
sns.boxplot(x=df_clean['UnitPrice'], ax=axes[1, 1], color='#74c476', fliersize=3)
axes[1, 1].set_xscale('log')
axes[1, 1].axvline(median_p, color='red', linestyle='--', linewidth=2, label=f'Median = £{median_p:.2f}')
axes[1, 1].set_title('Boxplot Harga Satuan Barang per Transaksi (Log Scale)', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Harga Satuan (£ - Skala Log)', fontsize=10, fontweight='bold')
axes[1, 1].legend(loc='upper right')

plt.suptitle('Eksplorasi Univariat Variabel Transaksional: Quantity & UnitPrice', fontsize=14, fontweight='bold', y=0.99)
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(code_num_1_2))

    # -------------------------------------------------------------
    # MD: INTERPRETASI NUMERIK 1 & 2
    # -------------------------------------------------------------
    md_univ_obs1 = """### 4.2 Interpretasi Univariat Variabel Transaksional (Quantity & UnitPrice)
1. **Distribusi dan Derajat Kecondongan (*Skewness*)**:
   * Baik variabel `Quantity` maupun `UnitPrice` memperlihatkan pola distribusi yang sangat condong ke kanan (*extremely right-skewed / positive skewness*).
   * Nilai mean ($Mean_Q = 10,61$; $Mean_P = £3,86$) secara konsisten jauh lebih besar daripada median ($Median_Q = 3$; $Median_P = £2,08$). Hal ini membuktikan bahwa nilai rata-rata ditarik oleh sebagian kecil observasi dengan nilai yang sangat masif.
2. **Karakteristik Modus & Tendensi Sentral**:
   * Pada visualisasi berskala log, kurva mendekati bentuk unimodal yang terpusat pada nilai 1 hingga 12 unit untuk `Quantity`, dan £1,25 hingga £4,13 untuk `UnitPrice`. Ini mengindikasikan bahwa produk yang paling laris merupakan cenderamata dengan harga terjangkau (*affordable giftware*).
3. **Analisis Outlier & Pola Menarik**:
   * Boxplot logaritmik menunjukkan sebaran titik outlier di sisi kanan rentang batas atas. Nilai kuantitas ekstrem (misal 1.000 hingga 80.995 unit) dan harga satuan tinggi merefleksikan transaksi borongan grosir B2B (*bulk business-to-business purchase*), yang menjadi pilar pendapatan utama perusahaan.
"""
    cells.append(nbf.v4.new_markdown_cell(md_univ_obs1))

    # -------------------------------------------------------------
    # CODE: UNIVARIATE NUMERIK 3 & 4 (RECENCY & MONETARY)
    # -------------------------------------------------------------
    code_num_3_4 = """# Visualisasi Univariat Numerik 3 & 4: Distribusi Recency dan Monetary pada Level Pelanggan
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 1. Histogram & KDE: Recency (Skala Alami)
sns.histplot(cust_df['Recency'], bins=40, kde=True, ax=axes[0], color='#d95f02')
med_r = cust_df['Recency'].median()
mean_r = cust_df['Recency'].mean()
axes[0].axvline(med_r, color='black', linestyle='--', linewidth=2, label=f'Median = {med_r:.0f} hari')
axes[0].axvline(mean_r, color='blue', linestyle='-', linewidth=2, label=f'Mean = {mean_r:.1f} hari')
axes[0].set_title('Distribusi Jeda Waktu Transaksi Pelanggan (Recency)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Recency (Jumlah Hari Sejak Transaksi Terakhir)', fontsize=10, fontweight='bold')
axes[0].set_ylabel('Jumlah Pelanggan', fontsize=10, fontweight='bold')
axes[0].legend(loc='upper right')

# 2. Histogram & KDE: Monetary (Skala Logaritmik)
sns.histplot(cust_df['Monetary'], bins=40, kde=True, ax=axes[1], color='#7570b3', log_scale=True)
med_m = cust_df['Monetary'].median()
mean_m = cust_df['Monetary'].mean()
axes[1].axvline(med_m, color='black', linestyle='--', linewidth=2, label=f'Median = £{med_m:,.2f}')
axes[1].axvline(mean_m, color='red', linestyle='-', linewidth=2, label=f'Mean = £{mean_m:,.2f}')
axes[1].set_title('Distribusi Total Pengeluaran Belanja Pelanggan (Monetary - Log Scale)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Monetary Value (£ - Skala Log)', fontsize=10, fontweight='bold')
axes[1].set_ylabel('Jumlah Pelanggan', fontsize=10, fontweight='bold')
axes[1].legend(loc='upper right')

plt.suptitle('Eksplorasi Univariat Variabel Level Pelanggan: Recency & Monetary Value', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(code_num_3_4))

    # -------------------------------------------------------------
    # MD: INTERPRETASI NUMERIK 3 & 4
    # -------------------------------------------------------------
    md_univ_obs2 = """### 4.3 Interpretasi Univariat Variabel Level Pelanggan (Recency & Monetary)
1. **Karakteristik Distribusi `Recency`**:
   * Distribusi `Recency` memiliki pola *right-skewed* dengan konsentrasi massa data tertinggi berada pada rentang **0 hingga 30 hari** ($Median = 51$ hari, $Mean = 92,5$ hari).
   * Konsentrasi tinggi pada recency rendah menandakan bahwa proporsi pelanggan yang aktif bertransaksi menjelang akhir tahun 2011 cukup besar. Penurunan frekuensi terjadi secara bertahap menuju 374 hari, mencerminkan adanya kohor pelanggan dorman yang belum bertransaksi kembali selama hampir setahun.
2. **Karakteristik Distribusi `Monetary`**:
   * Pada skala logaritmik, distribusi `Monetary` mengikuti kurva lonceng simetris (*log-normal distribution*).
   * Median total belanja per pelanggan adalah **£648,10**, sementara rata-rata belanja mencapai **£1.909,11**. Kesenjangan yang hampir 3 kali lipat ini membuktikan berlakunya **Hukum Pareto (Prinsip 80/20)**, di mana sebagian kecil pelanggan bernilai tinggi (*high-value whales*) menyumbang porsi pendapatan bisnis yang luar biasa besar.
"""
    cells.append(nbf.v4.new_markdown_cell(md_univ_obs2))

    # -------------------------------------------------------------
    # CODE: UNIVARIATE KATEGORIKAL 1 & 2 (NEGARA & JAM)
    # -------------------------------------------------------------
    code_cat_1_2 = """# Visualisasi Univariat Kategorikal 1 & 2: Top Pasar Internasional & Pola Jam Transaksi
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# 1. Bar Chart: Top 10 Pasar Internasional (Di luar United Kingdom)
intl_df = df_clean[df_clean['Country'] != 'United Kingdom']
top_intl = intl_df['Country'].value_counts().head(10).reset_index()
top_intl.columns = ['Country', 'TransactionCount']
total_intl = intl_df.shape[0]
top_intl['Percentage'] = (top_intl['TransactionCount'] / total_intl) * 100

bars1 = sns.barplot(data=top_intl, x='TransactionCount', y='Country', ax=axes[0], palette='Blues_r')
axes[0].set_title('Top 10 Negara Destinasi Ekspor Internasional (Non-UK)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Jumlah Baris Transaksi', fontsize=10, fontweight='bold')
axes[0].set_ylabel('Negara Destinasi', fontsize=10, fontweight='bold')

# Anotasi angka dan persentase di ujung batang
for idx, row in top_intl.iterrows():
    axes[0].text(row['TransactionCount'] + 150, idx, f"{row['TransactionCount']:,} ({row['Percentage']:.1f}%)", 
                 va='center', fontsize=9, fontweight='bold')
axes[0].set_xlim(0, top_intl['TransactionCount'].max() * 1.25)

# 2. Bar Chart: Distribusi Transaksi Berdasarkan Jam dalam Sehari (Hour)
hour_counts = df_clean['Hour'].value_counts().sort_index().reset_index()
hour_counts.columns = ['Hour', 'TransactionCount']
total_tx = df_clean.shape[0]
hour_counts['Percentage'] = (hour_counts['TransactionCount'] / total_tx) * 100

# Pewarnaan khusus: beri highlight pada jam puncak (12:00)
colors_hour = ['#d73027' if h == 12 else '#4575b4' for h in hour_counts['Hour']]
bars2 = sns.barplot(data=hour_counts, x='Hour', y='TransactionCount', ax=axes[1], palette=colors_hour)
axes[1].set_title('Distribusi Volume Transaksi Berdasarkan Jam Transaksi (Hour of Day)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Jam Transaksi (Format 24 Jam)', fontsize=10, fontweight='bold')
axes[1].set_ylabel('Jumlah Baris Transaksi', fontsize=10, fontweight='bold')

# Anotasi jam puncak
max_hour_val = hour_counts['TransactionCount'].max()
axes[1].annotate(f'Puncak: Jam 12:00\n{max_hour_val:,} tx', xy=(12 - hour_counts['Hour'].min(), max_hour_val), 
                 xytext=(12 - hour_counts['Hour'].min() + 1.5, max_hour_val * 0.9),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
                 fontsize=9, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.5))

plt.suptitle('Eksplorasi Univariat Variabel Kategorikal: Geografis Pasar & Jam Transaksi', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(code_cat_1_2))

    # -------------------------------------------------------------
    # MD: INTERPRETASI KATEGORIKAL 1 & 2
    # -------------------------------------------------------------
    md_univ_obs3 = """### 4.4 Interpretasi Univariat Variabel Kategorikal (Geografis Pasar & Jam Transaksi)
1. **Sebaran Pasar Ekspor Internasional**:
   * Dari total transaksi internasional di luar Britania Raya, tiga negara teratas mendominasi lebih dari tiga perempat pasar: **Jerman (28,4%)**, **Prancis (26,2%)**, dan **EIRE / Irlandia (22,8%)**. Ketiga negara ini membentuk klaster ekspor utama di kawasan Eropa Barat.
   * Negara di luar Eropa seperti Australia juga masuk dalam daftar 10 besar, menunjukkan jangkauan perdagangan global peritel ini.
2. **Pola Ritme Operasional Belanja Harian**:
   * Distribusi transaksi per jam membentuk kurva lonceng simetris (*bell-shaped curve*) yang dimulai dari pukul 06:00, meningkat drastis menjelang tengah hari, dan mencapai **puncak tepat pada pukul 12:00 siang (77.000+ transaksi)**.
   * Aktivitas menurun tajam setelah pukul 16:00 dan berhenti sepenuhnya pada pukul 20:00 (sama sekali tidak ada transaksi pada tengah malam pukul 21:00 hingga 05:00).
   * Karakteristik ini memperkuat konfirmasi bisnis bahwa pembeli mayoritas beroperasi pada jam kerja formal kantoran (*business operating hours*), yang sangat khas bagi pembeli grosir B2B dan pedagang toko fisik.
"""
    cells.append(nbf.v4.new_markdown_cell(md_univ_obs3))

    return cells
