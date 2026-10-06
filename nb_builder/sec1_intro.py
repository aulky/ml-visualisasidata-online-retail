import nbformat as nbf

def get_cells():
    cells = []
    
    # -------------------------------------------------------------
    # CELL 1: COVER & IDENTITAS MAHASISWA
    # -------------------------------------------------------------
    md_cover = """# LAPORAN TUGAS SUB-CLO-12-1-1
## EXPLORATORY DATA ANALYSIS (EDA) PADA DATASET NYATA
### Studi Kasus: Analisis Perilaku Transaksi dan Segmentasi Pelanggan E-Commerce (UCI Online Retail)

---

### Informasi Identitas Mahasiswa:
* **Nama Lengkap** : [Nama Lengkap Mahasiswa]
* **NIM**          : [NIM Mahasiswa]
* **Kelas**        : [Kelas Mahasiswa, contoh: IF-45-01 / DS-01]
* **Mata Kuliah**  : Visualisasi Data & Analitika
* **Dosen Pengampu**: [Nama Dosen Pengampu]
* **Tanggal Pengerjaan**: 07 Oktober 2026
* **Lingkungan Komputasi**: Python 3.12 (Jupyter Notebook / VS Code)

---

### Ringkasan Eksekutif (Executive Summary)
Laporan ini memuat proses **Exploratory Data Analysis (EDA)** secara menyeluruh pada dataset transaksi nyata **Online Retail** yang dipublikasikan oleh *UCI Machine Learning Repository*. Dataset ini merekam lebih dari 540.000 riwayat transaksi perdagangan daring (*online retail*) dari peritel transnasional yang berbasis di Britania Raya (*United Kingdom*) sepanjang rentang 1 Desember 2010 hingga 9 Desember 2011.

Melalui pendekatan berbasis bukti empiris (*evidence-based data exploration*), analisis dilakukan secara terstruktur mencakup:
1. **Data Profiling & Validasi Data**: Pemeriksaan integritas data, anomali harga/kuantitas negatif, identifikasi missing values, dan deteksi dini outlier.
2. **Data Cleaning Ringan**: Penanganan transaksi pembatalan, pembersihan duplikasi, penyesuaian tipe data, dan rekayasa fitur bertingkat (*transaction-level* dan *customer-level RFM*).
3. **Univariate Visualization**: Analisis distribusi, tendensi sentral, derajat kecondongan (*skewness*), dan dispersi nilai variabel kunci.
4. **Bivariate Visualization**: Eksplorasi hubungan antar variabel numerik-numerik, kategorikal-numerik, dan temporal.
5. **Multivariate Visualization**: Pemetaan matriks korelasi (*correlation heatmap*) dan analisis interaksi multivariat (*pairplot matrix*) dengan pengelompokan segmen konsumen.
6. **Dimensionality Reduction (PCA & Nilai Tambah)**: Reduksi dimensi berbasis Principal Component Analysis (PCA) 2D, dekomposisi *loadings*, rasio varians, serta nilai tambah visualisasi 3D dan *Dendrogram Hierarchical Clustering*.
7. **Insight Kunci, Kesimpulan & Rekomendasi**: Sintesis 5 temuan strategis berbasis data, rekomendasi bisnis, potensi fitur untuk machine learning masa depan, dan tantangan kualitas data.
8. **Lembar Deklarasi AI**: Dokumentasi kepatuhan etika akademik penggunaan AI sesuai pedoman tugas Bab 6.1.
"""
    cells.append(nbf.v4.new_markdown_cell(md_cover))

    # -------------------------------------------------------------
    # CELL 2: BAGIAN 1 - DESKRIPSI DATASET & TUJUAN ANALISIS
    # -------------------------------------------------------------
    md_dataset = """## Bagian 1: Deskripsi Dataset, Konteks Bisnis, dan Tujuan Analisis

### 1.1 Metadata Dataset Resmi
* **Nama Dataset** : Online Retail Dataset
* **Penyedia Resmi**: UCI Machine Learning Repository
* **Tautan Sumber Asli**: [https://archive.ics.uci.edu/dataset/352/online+retail](https://archive.ics.uci.edu/dataset/352/online+retail)
* **Pencipta / Donatur**: Dr. Daqing Chen (School of Engineering, London South Bank University)
* **Domain Industri**: *E-Commerce*, *Wholesale & Retail Trade*, *Customer Analytics*
* **Karakteristik Data**: Multivariat, Data Sekuensial Transaksional (*Transaction Log*)
* **Jumlah Observasi Awal**: 541.909 baris data
* **Jumlah Variabel Awal**: 8 variabel (gabungan numerik kontinu, kategorikal, temporal, dan identifikasi unik)

### 1.2 Konteks Bisnis Dataset
Entitas bisnis yang dianalisis merupakan perusahaan ritel daring non-toko (*non-store online retail*) yang berkedudukan di Inggris (*United Kingdom*). Perusahaan ini memiliki spesialisasi dalam menjual barang-barang hadiah unik (*all-occasion gifts*), pernak-pernik pesta, dan dekorasi rumah.

Karakteristik operasional bisnis:
* Mayoritas pelanggan perusahaan adalah **pedagang grosir (*wholesalers*)**, toko ritel fisik skala kecil-menengah, dan pembeli borongan dari berbagai negara di Eropa dan global, di samping konsumen langsung (*end-consumers*).
* Model perdagangan mencakup transaksi domestik (*United Kingdom*) dan ekspor transnasional (Jerman, Prancis, EIRE/Irlandia, Spanyol, Belanda, Australia, dll.).

### 1.3 Kamus Data (Data Dictionary)
| No | Nama Kolom | Tipe Data Awal | Tipe Data Analisis | Deskripsi Kontekstual |
|:--:|:---|:---|:---|:---|
| 1 | `InvoiceNo` | Object / String | Nominal | Nomor faktur transaksi 6-digit. Jika diawali huruf **'C'**, menandakan pembatalan (*cancellation* / kredit). |
| 2 | `StockCode` | Object / String | Nominal | Kode unik inventaris produk/barang dagang. |
| 3 | `Description` | Object / String | Nominal | Nama deskriptif produk/barang dagang. |
| 4 | `Quantity` | Integer | Numerik Diskrit | Kuantitas unit produk per baris transaksi. Nilai negatif menunjukkan pembatalan/pengembalian barang. |
| 5 | `InvoiceDate` | Object / String | Datetime | Tanggal dan waktu tepat saat transaksi diterbitkan. |
| 6 | `UnitPrice` | Float | Numerik Kontinu | Harga satuan produk per unit dalam mata uang Pound Sterling (£). |
| 7 | `CustomerID` | Float | Nominal | Nomor identitas unik pelanggan 5-digit integer. Bernilai NaN untuk pembeli tanpa akun (*guest*). |
| 8 | `Country` | Object / String | Kategorikal | Negara domisili pelanggan atau destinasi pengiriman barang. |

### 1.4 Rumusan Masalah dan Tujuan Analisis
Analisis eksploratif ini diarahkan untuk menjawab empat pertanyaan analitis kunci:
1. **Integritas & Kualitas Data Transaksi**: Berapa proporsi transaksi pembatalan, entri dengan harga/kuantitas anomali, data duplikat, dan *missing values* pada `CustomerID`?
2. **Karakteristik Distribusi Penjualan**: Bagaimana profil volume pemesanan (`Quantity`) dan harga produk (`UnitPrice`)? Apakah perilaku belanja mencerminkan pembelian ritel perorangan atau pembelian borongan grosir?
3. **Pola Temporal & Geografis Transaksi**: Pada jam dan hari apa aktivitas pemesanan mencapai puncak (*peak hours/days*), dan bagaimana penetrasi pasar ekspor di luar Britania Raya?
4. **Segmentasi & Reduksi Dimensi Konsumen**: Bagaimana karakteristik konsumen jika diagregasi ke dalam metrik *Recency, Frequency, Monetary, Total Quantity, Average Unit Price, dan Unique Products*? Seberapa efektif **Principal Component Analysis (PCA)** dalam memadatkan varians data multi-dimensi tersebut ke dalam representasi 2D dan 3D yang dapat diinterpretasikan secara intuitif?
"""
    cells.append(nbf.v4.new_markdown_cell(md_dataset))

    return cells
