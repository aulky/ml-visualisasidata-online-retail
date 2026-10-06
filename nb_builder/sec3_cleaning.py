import nbformat as nbf

def get_cells():
    cells = []
    
    # -------------------------------------------------------------
    # MD: BAGIAN 3 - DATA CLEANING RINGAN & REKAYASA FITUR
    # -------------------------------------------------------------
    md_clean_intro = """## Bagian 3: Data Cleaning Ringan & Rekayasa Fitur (Data Refinement)

### 3.1 Tujuan dan Metodologi Tahap Cleaning
Tujuan pembersihan data (*data cleaning*) ini adalah menyiapkan representasi data yang valid, bebas distorsi, dan siap dianalisis secara univariat, bivariat, multivariat, hingga reduksi dimensi (PCA).

Tahapan yang dilakukan meliputi:
1. **Deduplikasi Baris**: Menghapus 5.268 baris data duplikat murni.
2. **Penyaringan Transaksi Valid**: Mengisolasi transaksi penjualan aktual dengan memfilter `Quantity > 0` dan `UnitPrice > 0`. Hal ini secara otomatis menyingkirkan transaksi pembatalan (kode 'C') dan entri penyesuaian non-komersial.
3. **Penyesuaian Format Temporal**: Mengonversi `InvoiceDate` ke format `datetime64[ns]`.
4. **Rekayasa Fitur Level Transaksi (*Transaction-Level Feature Engineering*)**:
   * `TotalAmount`: Nilai bruto transaksi per item ($Quantity \times UnitPrice$).
   * `Hour`, `DayOfWeek`, `MonthYear`: Fitur temporal untuk membedah siklus belanja.
   * `MarketGroup`: Segmentasi geografis (*Domestik (UK)* vs *Internasional*).
5. **Rekayasa Fitur Level Pelanggan (*Customer-Level Feature Engineering*)**:
   Karena dataset ini merupakan log transaksi belanja per baris, maka untuk melakukan analisis multivariat dan **Principal Component Analysis (PCA)** yang bermakna bagi bisnis, data diagregasi ke level individu pelanggan terdaftar (`CustomerID`). Enam fitur kontinu murni diekstraksi:
   * **Recency (R)**: Jumlah hari sejak transaksi terakhir pelanggan hingga tanggal acuan (*snapshot date*).
   * **Frequency (F)**: Total transaksi unik yang dilakukan pelanggan.
   * **TotalQuantity**: Total akumulasi unit barang yang dipesan pelanggan.
   * **Monetary (M)**: Total akumulasi nilai pengeluaran belanja pelanggan (£).
   * **AvgUnitPrice**: Rata-rata harga satuan produk yang dipilih pelanggan.
   * **UniqueProducts**: Ragam variasi barang unik yang pernah dibeli.
6. **Segmentasi Pelanggan RFM Scoring**: Memetakan konsumen ke dalam 4 segmen strategis (*Champions*, *Loyal & Potential*, *Promising*, *At Risk*).
"""
    cells.append(nbf.v4.new_markdown_cell(md_clean_intro))

    # -------------------------------------------------------------
    # CODE: DATA CLEANING & REKAYASA FITUR
    # -------------------------------------------------------------
    code_cleaning = """# Salin dataset mentah
df_clean = df_raw.copy()

# 1. Hapus duplikasi baris identik
n_sebelum_dup = len(df_clean)
df_clean = df_clean.drop_duplicates()
print(f"1. Menghapus {n_sebelum_dup - len(df_clean):,} baris duplikat identik.")

# 2. Filter transaksi penjualan valid (Quantity > 0 dan UnitPrice > 0)
n_sebelum_filter = len(df_clean)
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)]
print(f"2. Menghapus {n_sebelum_filter - len(df_clean):,} baris transaksi pembatalan / harga non-positif.")

# 3. Konversi tipe data temporal
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'])

# 4. Rekayasa fitur level transaksi
df_clean['TotalAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']
df_clean['Hour'] = df_clean['InvoiceDate'].dt.hour
df_clean['DayOfWeek'] = df_clean['InvoiceDate'].dt.day_name()
df_clean['MonthYear'] = df_clean['InvoiceDate'].dt.to_period('M').astype(str)
df_clean['MarketGroup'] = np.where(df_clean['Country'] == 'United Kingdom', 'Domestik (UK)', 'Internasional')

print(f"Total baris transaksi bersih yang valid: {len(df_clean):,} baris (100% data transaksi bersih).")

# 5. Agregasi Level Pelanggan (Customer-Level Aggregation)
df_with_cust = df_clean[df_clean['CustomerID'].notnull()].copy()
df_with_cust['CustomerID'] = df_with_cust['CustomerID'].astype(int).astype(str)

# Tetapkan tanggal acuan (1 hari setelah transaksi paling mutakhir pada data)
snapshot_date = df_clean['InvoiceDate'].max() + pd.Timedelta(days=1)
print(f"Tanggal Acuan Analisis Pelanggan (Snapshot Date): {snapshot_date.strftime('%Y-%m-%d %H:%M:%S')}")

cust_df = df_with_cust.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'Quantity': 'sum',
    'TotalAmount': 'sum',
    'UnitPrice': 'mean',
    'StockCode': 'nunique'
}).reset_index()

# Penamaan kolom yang baku dan deskriptif
cust_df.columns = ['CustomerID', 'Recency', 'Frequency', 'TotalQuantity', 'Monetary', 'AvgUnitPrice', 'UniqueProducts']

# 6. Segmentasi Pelanggan Berbasis Skor Kuartil RFM
cust_df['R_Score'] = pd.qcut(cust_df['Recency'], 4, labels=[4, 3, 2, 1]).astype(int)
cust_df['F_Score'] = pd.qcut(cust_df['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4]).astype(int)
cust_df['M_Score'] = pd.qcut(cust_df['Monetary'], 4, labels=[1, 2, 3, 4]).astype(int)
cust_df['RFM_Total'] = cust_df['R_Score'] + cust_df['F_Score'] + cust_df['M_Score']

def petakan_segmen(total):
    if total >= 10:
        return 'Champions (Sangat Aktif & Loyal)'
    elif total >= 7:
        return 'Loyal & Potential (Potensial Tumbuh)'
    elif total >= 5:
        return 'Promising (Perlu Perhatian)'
    else:
        return 'At Risk (Beresiko Hilang / Dorman)'

cust_df['Segment'] = cust_df['RFM_Total'].apply(petakan_segmen)

print(f"Agregasi level pelanggan berhasil dibentuk: {len(cust_df):,} pelanggan unik.")
print("-" * 80)
print("5 Baris Sampel Data Pelanggan Hasil Rekayasa Fitur:")
display(cust_df.head())
"""
    cells.append(nbf.v4.new_code_cell(code_cleaning))

    # -------------------------------------------------------------
    # CODE: TABEL PERBANDINGAN SEBELUM & SESUDAH CLEANING
    # -------------------------------------------------------------
    code_eval_clean = """# Rangkuman perbandingan metrik sebelum dan sesudah pembersihan
summary_cleaning = pd.DataFrame({
    'Parameter Metrik': [
        'Total Baris Data',
        'Total Kolom / Fitur',
        'Missing Values (Total)',
        'Baris Duplikat',
        'Nilai Kuantitas Minimum',
        'Nilai Kuantitas Maksimum',
        'Nilai Harga Satuan Minimum (£)',
        'Nilai Harga Satuan Maksimum (£)'
    ],
    'Sebelum Cleaning (Data Mentah)': [
        f"{len(df_raw):,}",
        f"{df_raw.shape[1]}",
        f"{df_raw.isnull().sum().sum():,}",
        f"{duplicate_rows:,}",
        f"{df_raw['Quantity'].min():,}",
        f"{df_raw['Quantity'].max():,}",
        f"£{df_raw['UnitPrice'].min():,.2f}",
        f"£{df_raw['UnitPrice'].max():,.2f}"
    ],
    'Sesudah Cleaning (df_clean)': [
        f"{len(df_clean):,}",
        f"{df_clean.shape[1]}",
        f"{df_clean.isnull().sum().sum():,}",
        "0 (0.00%)",
        f"{df_clean['Quantity'].min():,}",
        f"{df_clean['Quantity'].max():,}",
        f"£{df_clean['UnitPrice'].min():,.2f}",
        f"£{df_clean['UnitPrice'].max():,.2f}"
    ]
})

print("Tabel Evaluasi Integritas Data Sebelum vs Sesudah Cleaning:")
display(summary_cleaning)
"""
    cells.append(nbf.v4.new_code_cell(code_eval_clean))

    # -------------------------------------------------------------
    # MD: JUSTIFIKASI HASIL DATA CLEANING
    # -------------------------------------------------------------
    md_clean_obs = """### 3.2 Justifikasi Metodologis dan Hasil Transformasi Data
1. **Penyusutan Data yang Rasional**:
   * Dataset transaksi bersih (`df_clean`) berkurang dari 541.909 menjadi **524.878 baris** (berkurang ~3,14%). Seluruh baris yang dibuang merupakan duplikat murni, pembatalan pesanan, atau entri penyesuaian inventaris sistem yang tidak memiliki nilai komersial valid.
   * Tingkat retensi data sebesar **96,86%** menjamin bahwa integritas populasi asli tetap terjaga dengan sangat baik.
2. **Ketersediaan Dua Lapisan Dataset untuk Analisis Mendalam**:
   * **Lapisan Transaksional (`df_clean`)**: Sebanyak 524.878 baris digunakan untuk membedah perilaku pembelian per produk, distribusi harga satuan, dinamika jam transaksi, dan sebaran geografis pasar ekspor.
   * **Lapisan Pelanggan (`cust_df`)**: Sebanyak **4.338 baris observasi pelanggan unik** dengan 6 variabel numerik kontinu murni (`Recency`, `Frequency`, `TotalQuantity`, `Monetary`, `AvgUnitPrice`, `UniqueProducts`) dan 1 variabel kategorikal (`Segment`). Lapisan ini memenuhi prasyarat analisis korelasi multivariat dan penerapan **Principal Component Analysis (PCA)** secara akademis dan kontekstual.
"""
    cells.append(nbf.v4.new_markdown_cell(md_clean_obs))

    return cells
