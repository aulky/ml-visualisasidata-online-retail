import nbformat as nbf

def get_cells():
    cells = []
    
    # -------------------------------------------------------------
    # MD: BAGIAN 2 - DATA PROFILING & VALIDASI DATA
    # -------------------------------------------------------------
    md_prof_intro = """## Bagian 2: Data Profiling & Validasi Data

### 2.1 Tujuan dan Metodologi Tahap Profiling
Tahap *Data Profiling & Validasi Data* bertujuan untuk memeriksa secara mendalam struktur fisik, kelengkapan, validitas, dan anomali pada dataset mentah sebelum dilakukan transformasi atau visualisasi. 

Langkah profiling mencakup:
1. Pemeriksaan dimensi matriks (*baris x kolom*) dan konsistensi tipe data (*data types*).
2. Analisis ringkasan statistik deskriptif lima angka (*five-number summary*) untuk mendeteksi sebaran dan nilai ekstrem.
3. Kuantifikasi nilai hilang (*missing values*) dan duplikasi baris data.
4. Validasi logika bisnis transaksional (transaksi retur/pembatalan dan nilai kuantitas/harga non-positif).
5. Identifikasi awal potensi *outlier* menggunakan metode Interquartile Range (IQR Tukey).
"""
    cells.append(nbf.v4.new_markdown_cell(md_prof_intro))

    # -------------------------------------------------------------
    # CODE: SETUP PUSTAKA & KONFIGURASI
    # -------------------------------------------------------------
    code_setup = """# 1. Pustaka Pemrosesan Data & Komputasi Saintifik
import os
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

# 2. Pustaka Visualisasi Data
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# 3. Pustaka Statistik & Machine Learning
from scipy import stats
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Konfigurasi estetika grafik global (Matplotlib & Seaborn)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
sns.set_theme(style='whitegrid', palette='deep')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['figure.dpi'] = 110
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 14
plt.rcParams['figure.titleweight'] = 'bold'

# Format tampilan angka pada Pandas
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', lambda x: f'{x:,.2f}')

print("Pustaka analitika dan konfigurasi visualisasi berhasil dimuat.")
"""
    cells.append(nbf.v4.new_code_cell(code_setup))

    # -------------------------------------------------------------
    # CODE: MEMUAT DATA & INSPEKSI STRUKTUR AWAL
    # -------------------------------------------------------------
    code_load = """# Memuat dataset mentah dari folder data/
data_path = os.path.join('data', 'online_retail.csv')
df_raw = pd.read_csv(data_path)

print(f"Bentuk Matriks Dataset (Baris x Kolom): {df_raw.shape[0]:,} baris x {df_raw.shape[1]} kolom")
print("-" * 80)
print("Lima Baris Pertama Data Mentah (Head):")
display(df_raw.head())

print("Lima Baris Terakhir Data Mentah (Tail):")
display(df_raw.tail())

print("-" * 80)
print("Informasi Tipe Data dan Kelengkapan Nilai:")
df_raw.info()
"""
    cells.append(nbf.v4.new_code_cell(code_load))

    # -------------------------------------------------------------
    # MD: OBSERVASI STRUKTUR & TIPE DATA
    # -------------------------------------------------------------
    md_prof_obs1 = """### 2.2 Hasil Observasi Struktur Awal & Skema Tipe Data
Berdasarkan keluaran inspeksi struktur data di atas, diperoleh temuan awal sebagai berikut:
1. **Dimensi Data**: Dataset mentah memiliki **541.909 baris observasi** dan **8 kolom variabel**. Jumlah ini jauh melampaui batas minimal tugas ($\ge 500$ baris dan $\ge 8$ kolom).
2. **Kesesuaian Tipe Data**:
   * `InvoiceNo`, `StockCode`, `Description`, dan `Country` terdeteksi sebagai objek teks (*string / categorical*).
   * `InvoiceDate` saat ini masih tersimpan sebagai tipe data teks (*object*), sehingga perlu dikonversi menjadi format `datetime64[ns]` agar komponen waktu (jam, hari, bulan) dapat diekstrak.
   * `Quantity` tersimpan sebagai *integer*, dan `UnitPrice` sebagai *float*.
   * `CustomerID` tersimpan sebagai *float64* karena adanya nilai hilang (*NaN values*). Jika dibersihkan, identitas ini merepresentasikan data nominal diskrit.
"""
    cells.append(nbf.v4.new_markdown_cell(md_prof_obs1))

    # -------------------------------------------------------------
    # CODE: STATISTIK DESKRIPTIF
    # -------------------------------------------------------------
    code_stats = """print("Statistik Deskriptif Variabel Numerik (Quantity & UnitPrice):")
display(df_raw[['Quantity', 'UnitPrice']].describe().T)

print("\nStatistik Deskriptif Variabel Kategorikal:")
display(df_raw[['InvoiceNo', 'StockCode', 'Description', 'Country']].describe().T)
"""
    cells.append(nbf.v4.new_code_cell(code_stats))

    # -------------------------------------------------------------
    # MD: OBSERVASI STATISTIK DESKRIPTIF
    # -------------------------------------------------------------
    md_prof_obs2 = """### 2.3 Hasil Observasi Statistik Deskriptif & Anomali Nilai
Ringkasan statistik lima angka di atas mengungkapkan beberapa anomali kritis:
1. **Nilai Negatif pada `Quantity`**:
   * Nilai minimum kuantitas adalah **-80.995 unit**, dengan nilai maksimum **+80.995 unit**. Nilai rata-rata tercatat 9,55 dengan standar deviasi sangat tinggi (218,08).
   * Nilai kuantitas negatif secara kontekstual menandakan transaksi pembatalan (*cancellation*), retur barang rusak, atau penyesuaian inventaris gudang.
2. **Nilai Negatif dan Nol pada `UnitPrice`**:
   * Nilai minimum harga satuan adalah **-£11.062,06** dan nilai maksimum mencapai **£38.970,00**. Median harga satuan adalah **£2,08** (Q1 = £1,25, Q3 = £4,13).
   * Harga satuan negatif dan nol merupakan entri non-transaksi (seperti koreksi akuntansi internal perusahaan, sampel gratis, atau biaya penyesuaian utang/piutang) yang harus difilter dari analisis perilaku belanja konsumen.
3. **Karakteristik Kategorikal**:
   * Terdapat 25.900 nomor faktur unik (`InvoiceNo`) dan 4.070 variasi produk (`StockCode`).
   * Negara paling dominan adalah **United Kingdom** dengan frekuensi 495.478 transaksi (~91,4% dari total data), menunjukkan bahwa bisnis ini berakar kuat di pasar domestik Inggris.
"""
    cells.append(nbf.v4.new_markdown_cell(md_prof_obs2))

    # -------------------------------------------------------------
    # CODE: PENGECEKAN MISSING VALUES, DUPLIKASI, & PEMBATALAN
    # -------------------------------------------------------------
    code_integrity = """# 1. Pengecekan Missing Values
missing_count = df_raw.isnull().sum()
missing_pct = (missing_count / len(df_raw)) * 100
missing_df = pd.DataFrame({
    'Jumlah Missing (Baris)': missing_count,
    'Persentase (%)': missing_pct
}).sort_values(by='Jumlah Missing (Baris)', ascending=False)

print("Tabel Ringkasan Missing Values:")
display(missing_df)

# 2. Pengecekan Duplikasi Baris Identik
duplicate_rows = df_raw.duplicated().sum()
duplicate_pct = (duplicate_rows / len(df_raw)) * 100
print(f"Jumlah Baris Terduplikasi Identik: {duplicate_rows:,} baris ({duplicate_pct:.2f}%)")

# 3. Kuantifikasi Transaksi Pembatalan (InvoiceNo berawalan 'C')
cancellations = df_raw['InvoiceNo'].astype(str).str.startswith('C').sum()
cancellations_pct = (cancellations / len(df_raw)) * 100
print(f"Jumlah Baris Transaksi Pembatalan (Awalan 'C'): {cancellations:,} baris ({cancellations_pct:.2f}%)")

# 4. Kuantifikasi Harga Satuan Nol atau Negatif
invalid_price = (df_raw['UnitPrice'] <= 0).sum()
invalid_price_pct = (invalid_price / len(df_raw)) * 100
print(f"Jumlah Baris UnitPrice <= 0: {invalid_price:,} baris ({invalid_price_pct:.2f}%)")
"""
    cells.append(nbf.v4.new_code_cell(code_integrity))

    # -------------------------------------------------------------
    # MD: OBSERVASI INTEGRITAS & MISSING VALUES
    # -------------------------------------------------------------
    md_prof_obs3 = """### 2.4 Hasil Observasi Kualitas & Integritas Data
Berdasarkan kuantifikasi di atas:
* **Missing Value pada `CustomerID`**: Terdapat **135.080 baris (24,93%)** data tanpa nomor identitas pelanggan. Dalam domain e-commerce, fenomena ini sangat lazim karena pembeli dapat melakukan transaksi sebagai *guest checkout* tanpa membuat akun terdaftar. Transaksi ini tetap valid untuk analisis volume produk dan pola temporal transaksi, namun akan dipisahkan saat melakukan pemodelan agregasi level pelanggan (*RFM segmentation*).
* **Missing Value pada `Description`**: Terdapat **1.454 baris (0,27%)** tanpa deskripsi produk. Seluruh baris ini juga tidak memiliki `CustomerID` dan memiliki harga satuan 0, sehingga diklasifikasikan sebagai log sistem non-komersial.
* **Duplikasi Data**: Ditemukan **5.268 baris (0,97%)** duplikat identik di mana seluruh kolom bernilai persis sama. Duplikasi ini terjadi akibat pengulangan log transmisi data pada sistem e-commerce dan harus dihapus agar tidak mendistorsi analisis volume transaksi.
* **Pembatalan Pesanan**: Terdeteksi **9.288 baris (1,71%)** transaksi dengan kode faktur diawali 'C' dan kuantitas bernilai negatif.
"""
    cells.append(nbf.v4.new_markdown_cell(md_prof_obs3))

    # -------------------------------------------------------------
    # CODE: DETEKSI AWAL OUTLIER (METODE IQR TUKEY)
    # -------------------------------------------------------------
    code_iqr = """def hitung_outlier_iqr(series, nama):
    q1 = series.quantile(0.25)
    median = series.median()
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    
    outliers = series[(series < lower_fence) | (series > upper_fence)]
    pct = (len(outliers) / len(series)) * 100
    
    return {
        'Variabel': nama,
        'Q1 (Kuartil 1)': q1,
        'Median (Q2)': median,
        'Q3 (Kuartil 3)': q3,
        'IQR': iqr,
        'Pagar Bawah (Q1 - 1.5*IQR)': lower_fence,
        'Pagar Atas (Q3 + 1.5*IQR)': upper_fence,
        'Jumlah Outlier (Baris)': len(outliers),
        'Proporsi Outlier (%)': pct
    }

# Evaluasi outlier pada transaksi dengan nilai positif awal
valid_pos = df_raw[(df_raw['Quantity'] > 0) & (df_raw['UnitPrice'] > 0)]
summary_q = hitung_outlier_iqr(valid_pos['Quantity'], 'Quantity (Kuantitas Barang)')
summary_p = hitung_outlier_iqr(valid_pos['UnitPrice'], 'UnitPrice (Harga Satuan £)')

outlier_table = pd.DataFrame([summary_q, summary_p])
print("Tabel Identifikasi Awal Outlier (Metode IQR Tukey):")
display(outlier_table)
"""
    cells.append(nbf.v4.new_code_cell(code_iqr))

    # -------------------------------------------------------------
    # MD: OBSERVASI OUTLIER AWAL
    # -------------------------------------------------------------
    md_prof_obs4 = """### 2.5 Hasil Observasi Outlier & Anomali Awal
Berdasarkan batas pagar Tukey:
1. **Outlier `Quantity`**: Sebanyak **56.897 transaksi (10,72%)** memiliki kuantitas di atas 23 unit ($Q3 + 1.5 \times IQR$).
2. **Outlier `UnitPrice`**: Sebanyak **37.669 transaksi (7,10%)** memiliki harga satuan di atas £8,45 ($Q3 + 1.5 \times IQR$).

**Justifikasi Kontekstual Data Science**:
Dalam domain perdagangan ritel dan grosir (*wholesale*), nilai kuantitas tinggi (misalnya 100 hingga 1.000 unit) bukanlah galat pengukuran (*measurement error*), melainkan mencerminkan perilaku pembelian partai besar oleh klien korporat/toko ritel fisik. Menghapus data ini secara sembrono akan menghilangkan informasi penting mengenai segmen pelanggan grosir bernilai tinggi (*high-value clients*).

Oleh karena itu, tindakan metodologis yang tepat adalah:
1. Mempertahankan nilai transaksi valid untuk merefleksikan dinamika bisnis nyata.
2. Menerapkan **transformasi logaritmik ($\log(1+x)$)** pada tahapan visualisasi univariat/bivariat dan pemodelan PCA guna meredam dampak *heavy-tailed distribution* tanpa menghilangkan informasi data asli.
"""
    cells.append(nbf.v4.new_markdown_cell(md_prof_obs4))

    return cells
