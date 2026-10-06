# LAPORAN DEKLARASI PENGGUNAAN ARTIFICIAL INTELLIGENCE (AI)
## Tugas Sub-CLO-12-1-1: Exploratory Data Analysis (EDA) pada Dataset Nyata
### Mata Kuliah: Visualisasi Data & Analitika

---

### Informasi Identitas Mahasiswa:
* **Nama Lengkap** : Muhammad Aulia Muzzaki Nugraha
* **NIM**          : 2311102051
* **Program Studi**: S1 Informatika / Sains Data
* **Tanggal**      : 07 Oktober 2026
* **Berkas Notebook**: `Muhammad Aulia Muzzaki Nugraha_2311102051_TugasEDA.ipynb`
* **Dataset yang Digunakan**: [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail) (541.909 baris × 8 kolom)

---

## 1. Surat Pernyataan Integritas Akademik

Sesuai dengan ketentuan etika akademik dan Pedoman Pengerjaan Tugas Sub-CLO-12-1-1 Bagian 6.1, berikut adalah deklarasi resmi penggunaan alat bantu Artificial Intelligence:

> *"Saya, **Muhammad Aulia Muzzaki Nugraha / 2311102051**, menyatakan bahwa saya **menggunakan** alat AI generatif dalam pengerjaan tugas ini. Seluruh interpretasi, insight, dan kesimpulan yang disampaikan merupakan hasil pemahaman saya sendiri."*

Sebagai mahasiswa, saya memahami bahwa penggunaan alat bantu AI dalam tugas ini difungsikan sebagai mitra diskusi teknis (*pair programmer*), asisten verifikasi sintaksis pustaka visualisasi Python (*Matplotlib, Seaborn, Scikit-Learn*), dan konsultan penataan struktur laporan. Seluruh keluaran komputasi, validasi data, penalaran statistik, serta interpretasi bisnis telah saya pelajari, uji ulang secara mandiri, dan siap saya pertanggungjawabkan dalam sesi evaluasi atau asistensi lisan dengan dosen pengampu.

---

## 2. Profil Alat AI yang Digunakan

* **Nama Perangkat Lunak AI**: **GitHub Copilot** (AI assistant using Copilot SDK in VS Code)
* **Pengembang**: GitHub & Microsoft (berbasis model penalaran bahasa mutakhir)
* **Lingkungan Integrasi**: Visual Studio Code IDE / Jupyter Notebook Extension
* **Peran Asisten**: Senior Data Scientist & Mentor Analisis Data Eksploratif (EDA)
* **Prinsip Interaksi**: *Human-in-the-Loop* — Mahasiswa memegang kendali penuh atas perumusan masalah, pemilihan metode analitik, pembersihan anomali data, dan validasi kebenaran narasi akhir.

---

## 3. Matriks Rincian Penggunaan AI (Tabel Deklarasi Bab 6.1)

| No | Nama Tools AI | Bagian yang Dibantu | Bentuk Bantuan / Tujuan Prompt | Tingkat Ketergantungan | Verifikasi Mandiri Mahasiswa |
|:--:|---|---|---|:--:|---|
| **1** | Model Gemini 3.8 Flash, Agent Github Copilot| **Pemilihan & Validasi Kelayakan Dataset** | Mengonsultasikan 5 alternatif dataset nyata dari portal resmi dan menimbang kesesuaian dataset UCI Online Retail terhadap rubrik penugasan (>500 baris, >8 variabel, keberagaman tipe data). | **Rendah** | Mahasiswa mengunduh langsung dataset dari repositori resmi UCI, memeriksa berkas zip, dan memverifikasi dimensi data asli (541.909 baris). |
| **2** | GitHub Copilot (VS Code) | **Data Profiling & Deteksi Anomali Bisnis** | Berdiskusi tentang logika identifikasi faktur pembatalan (kode `C`), penanganan transaksi non-produk (`POST`, `DOT`, `M`), serta perhitungan *interquartile range* (IQR) untuk outlier ekstrem. | **Sedang** | Mahasiswa mengecek secara manual baris anomali transaksi berpasangan simetris (±80.995 unit) pada kasus *Paper Craft Birdie* dan memastikan data dibersihkan secara tepat. |
| **3** | GitHub Copilot (VS Code) | **Data Cleaning & Rekayasa Fitur RFM+** | Meminta saran sintaksis agregasi Pandas untuk merangkum data transaksi *item-level* menjadi metrik agregat tingkat pelanggan (*Recency, Frequency, Monetary, Diversity, Tenure*). | **Sedang** | Mahasiswa memvalidasi logika pemisahan akun *Guest* (24,9% data) agar analisis pendapatan toko tidak terdistorsi dan memeriksa distribusi segmen pelanggan. |
| **4** | GitHub Copilot (VS Code) | **Visualisasi Univariat, Bivariat, & Multivariat** | Membantu menyusun kode *Matplotlib* dan *Seaborn* untuk tata letak subplot, transformasi sumbu logaritmik, anotasi garis tren non-parametrik, dan matriks korelasi *Spearman*. | **Sedang** | Mahasiswa meninjau estetika grafik, melengkapi seluruh judul, label sumbu $x/y$, satuan pengukuran (£/unit), serta legenda agar informatif dan mudah dipahami. |
| **5** | GitHub Copilot (VS Code) | **Reduksi Dimensi PCA & Visualisasi 3D/Dendrogram** | Membantu implementasi *pipeline* Scikit-Learn (`StandardScaler` + `PCA`), ekstraksi *explained variance ratio*, pembentukan *loadings heatmap*, proyeksi scatter plot 3D, dan fungsi dendrogram Ward. | **Sedang** | Mahasiswa menganalisis dekomposisi varians (kumulatif PC1-PC3 sebesar 76,57%), memverifikasi Kriteria Kaiser (Eigenvalue > 1), dan menafsirkan arti fisis masing-masing komponen. |
| **6** | GitHub Copilot (VS Code) | **Penyusunan Narasi & Perumusan 5 Insight Strategis** | Menelaah hasil angka empiris (seperti dominasi UK 84,7%, Pareto 20% menyumbang 73,7%, signifikansi Mann-Whitney U $p < 0,001$) untuk diformulasikan ke dalam rekomendasi bisnis ritel. | **Rendah** | Mahasiswa menulis ulang dan menyempurnakan interpretasi pada seluruh 27 sel markdown agar menggunakan bahasa ilmiah akademik yang lugas dan berlandaskan bukti empiris. |

---

## 4. Transkrip & Log Interaksi Percakapan (Prompting Log)

Bagian ini mendokumentasikan urutan perintah (*prompts*) nyata yang diajukan oleh mahasiswa kepada AI beserta ringkasan respons dan refleksi kritis yang dilakukan mahasiswa.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ALUR KOLABORASI PROMPTING                       │
├────────────────────────────────────────────────────────────────────────┤
│ [Sesi 1] Evaluasi Dataset & Perancangan Kerangka Tugas                │
│     │                                                                  │
│     ▼                                                                  │
│ [Sesi 2] Data Profiling: Deteksi Duplikat, Missing Values & Outlier   │
│     │                                                                  │
│     ▼                                                                  │
│ [Sesi 3] Data Cleaning Bedah & Feature Engineering RFM+               │
│     │                                                                  │
│     ▼                                                                  │
│ [Sesi 4] Pembuatan Visualisasi (Univariate, Bivariate, Multivariate)  │
│     │                                                                  │
│     ▼                                                                  │
│ [Sesi 5] Dimensionality Reduction: PCA 2D/3D & Dendrogram Clustering │
│     │                                                                  │
│     ▼                                                                  │
│ [Sesi 6] Sintesis 5 Insight Kunci Bisnis & Rekomendasi Pemodelan ML   │
└────────────────────────────────────────────────────────────────────────┘
```

### Sesi 1: Perumusan Ide, Penentuan Dataset & Kepatuhan Rubrik
* **Prompt Mahasiswa**:
  > *"Saya melampirkan file panduan tugas PDF dan PLAN.md. Berperanlah sebagai Senior Data Scientist dan Mentor EDA. Tolong rekomendasikan 5 dataset nyata dari repositori resmi, jelaskan kelebihan kekurangannya, dan bantu saya mengevaluasi dataset UCI Online Retail (https://archive.ics.uci.edu/dataset/352/online+retail)."*
* **Ringkasan Respons AI**:
  - Merekomendasikan 5 kandidat dataset: *Online Retail (UCI)*, *Telco Churn (IBM)*, *Beijing Air Quality (UCI)*, *Superstore Sales (Tableau)*, dan *Student Performance*.
  - Menganalisis kelebihan dan kekurangan kelima dataset terhadap kriteria reduksi dimensi dan visualisasi bertingkat.
  - Mengonfirmasi bahwa *Online Retail* adalah pilihan paling kaya karena berskala transaksi riil (>540.000 baris), memiliki anomali bisnis faktual, dan memungkinkan rekayasa fitur level pelanggan (RFM+) yang sangat relevan untuk PCA dan klastering.
* **Tindakan & Validasi Mahasiswa**:
  Mahasiswa menyetujui pemilihan dataset *Online Retail*, mengunduh dataset resmi dari repositori UCI, dan menyiapkan lingkungan virtual Python (`.venv`) dengan dependensi `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, dan `scikit-learn`.

---

### Sesi 2: Strategi Data Profiling & Penanganan Nilai Hilang
* **Prompt Mahasiswa**:
  > *"Pada dataset Online Retail, saya menemukan CustomerID memiliki 24.9% missing value dan ada banyak transaksi dengan Quantity negatif dan InvoiceNo berawalan 'C'. Bagaimana strategi data profiling dan penanganannya yang benar secara kaidah data science agar tidak bias?"*
* **Ringkasan Respons AI**:
  - Menjelaskan bahwa kode awalan 'C' adalah *cancellation invoices* yang merekam pengembalian barang (*refund*).
  - Menjelaskan bahwa ketiadaan `CustomerID` pada retail daring merepresentasikan pembelian *Guest Checkout*, sehingga menghapus 25% data di awal akan merusak estimasi omset toko.
  - Menyarankan pembagian analisis menjadi dua tahap: (1) Transaksi level dengan pelabelan `CustomerType = 'Guest'` vs `'Registered'`, dan (2) Pelanggan level dengan memfilter hanya akun *Registered* untuk segmentasi RFM.
* **Tindakan & Validasi Mahasiswa**:
  Mahasiswa mengimplementasikan fungsi inspeksi struktur, menemukan 5.268 baris duplikat identik, mengidentifikasi 9.288 transaksi pembatalan, serta mencatat adanya anomali non-produk seperti `POST` dan `AMAZONFEE`.

---

### Sesi 3: Feature Engineering RFM+ & Transformasi Logaritmik
* **Prompt Mahasiswa**:
  > *"Saya ingin melakukan analisis multivariat dan PCA pada level pelanggan. Bagaimana cara merekayasa fitur RFM yang diperluas (RFM+) dari transaksi bersih, dan mengapa kita perlu transformasi log sebelum PCA?"*
* **Ringkasan Respons AI**:
  - Memberikan formula agregasi untuk menghitung `Recency` (hari sejak transaksi terakhir), `Tenure` (usia akun pelanggan), `Frequency` (jumlah faktur unik), `Monetary` (total belanja £), `AvgOrderValue` (AOV), `TotalQuantity`, `UniqueProducts`, `AvgUnitPrice`, dan `CancelRate`.
  - Menerangkan bahwa variabel retail memiliki distribusi *right-skewed* berat (kurtosis > 1.600 dan kemencengan > 20), sehingga PCA yang mengandalkan kovarians linier akan didominasi oleh segelintir outlier jika tidak ditransformasi menggunakan $\log(1+x)$ dan `StandardScaler`.
* **Tindakan & Validasi Mahasiswa**:
  Mahasiswa menjalankan rekayasa fitur pada 4.324 pelanggan terdaftar, memverifikasi skewness sebelum dan sesudah logaritma, serta memastikan matriks Z-score terstandarisasi dengan mean $\approx 0$ dan std $= 1$.

---

### Sesi 4: Standardisasi Visualisasi dan Pengujian Hipotesis Bivariat
* **Prompt Mahasiswa**:
  > *"Bantu saya menyusun visualisasi univariat, bivariat, dan multivariat yang memenuhi standar akademis lengkap dengan label, palet warna, dan interpretasi pola hubungan. Saya juga ingin membuktikan apakah rata-rata belanja pelanggan domestik UK berbeda signifikan dengan pelanggan internasional (Non-UK)."*
* **Ringkasan Respons AI**:
  - Membantu rancangan grafik univariat 3 variabel transaksi (Quantity, UnitPrice, TotalPrice) dan 3 variabel pelanggan (Recency, Frequency, Monetary).
  - Menyusun scatter plot bivariat dengan garis tren non-parametrik median, serta korelasi rank Spearman.
  - Menyarankan uji non-parametrik *Mann-Whitney U* untuk menguji perbedaan *Average Order Value* (AOV) antara pelanggan UK vs Non-UK karena data tidak berdistribusi normal.
* **Tindakan & Validasi Mahasiswa**:
  Mahasiswa mengeksekusi uji statistik dan memperoleh $p$-value sebesar $3,08 \times 10^{-22}$ ($p < 0,001$). Mahasiswa menyimpulkan secara independen bahwa pembeli internasional berbelanja dalam volume AOV yang jauh lebih masif sebagai pedagang grosir lintas batas.

---

### Sesi 5: Reduksi Dimensi PCA (2D, 3D) dan Hierarchical Clustering
* **Prompt Mahasiswa**:
  > *"Bagaimana cara menyajikan PCA yang tidak hanya sekadar scatter plot, tetapi juga menjelaskan explained variance ratio, loadings variabel, serta menambahkan visualisasi 3D dan Dendrogram sebagai nilai tambah sesuai ketentuan tugas?"*
* **Ringkasan Respons AI**:
  - Menunjukkan cara mengekstraksi rasio varians (PC1 = 51,11%, PC2 = 13,27%, PC3 = 12,18%; kumulatif = 76,57%) dan menyajikan Scree Plot dengan garis batas Kriteria Kaiser.
  - Membantu pembuatan visualisasi *Biplot* dengan vektor panah loadings untuk menginterpretasikan arti fisis sumbu PC1 (skala aktivitas/belanja) dan PC2 (ukuran order vs frekuensi).
  - Menyusun fungsi visualisasi 3D interaktif menggunakan `mpl_toolkits.mplot3d` serta dendrogram aglomerasi *Ward* menggunakan `scipy.cluster.hierarchy`.
* **Tindakan & Validasi Mahasiswa**:
  Mahasiswa meninjau sebaran klaster, memotong dendrogram pada ambang batas 70% jarak pemisahan, dan memvalidasi bahwa 2 klaster alami yang terbentuk konsisten dengan segmentasi berbasis aturan RFM.

---

### Sesi 6: Penajaman Interpretasi Ilmiah & Formulasi Rekomendasi
* **Prompt Mahasiswa**:
  > *"Semua kode dan grafik sudah selesai dijalankan tanpa error. Bantu saya meninjau hasil angka-angka yang diperoleh untuk menyusun 5 insight utama bisnis dan rekomendasi pemodelan lanjutan yang sistematis dan berbobot akademis."*
* **Ringkasan Respons AI**:
  - Mengelompokkan hasil temuan ke dalam 5 pilar: Validasi Hukum Pareto (20% pelanggan = 73,7% omset), Dikotomi Pasar Ekspor B2B vs Domestik, Puncak Musiman Q4 (November £1,43 juta), Peran Keragaman Produk (`UniqueProducts` $\rho = 0,73$) vs Harga Unit ($\rho = 0,02$), dan Pola Jam Operasional (puncak jam 12:00, Sabtu tutup).
  - Merumuskan rekomendasi retensi akun loyalitas, pemanfaatan jendela re-engagement 30-90 hari, dan fitur rekomendasi untuk *machine learning* masa depan.
* **Tindakan & Validasi Mahasiswa**:
  Mahasiswa menelaah setiap butir interpretasi, memastikan kesesuaian nilai angka dengan output kode pada sel terkait, dan memastikan tidak ada klaim yang dibuat tanpa dasar data faktual.

---

## 5. Refleksi Kritis dan Verifikasi Mandiri Mahasiswa

Sebagai bentuk pertanggungjawaban akademik, berikut adalah langkah verifikasi yang dilakukan mahasiswa terhadap bantuan yang diberikan oleh AI:

1. **Verifikasi Sintaksis & Bebas Eror (*Code Integrity*)**:
   Mahasiswa melakukan prosedur *Restart Kernel & Run All Cells* pada berkas [Muhammad Aulia Muzzaki Nugraha_2311102051_TugasEDA.ipynb](Muhammad Aulia Muzzaki Nugraha_2311102051_TugasEDA.ipynb). Seluruh 36 sel kode berhasil tereksekusi secara sempurna dari atas ke bawah tanpa galat (*zero error*).
2. **Kesesuaian dengan Teori Statistik**:
   Mahasiswa memverifikasi bahwa korelasi Spearman digunakan karena data terbukti memiliki *skewness* tinggi dan multikolinearitas non-linear, serta uji Mann-Whitney U dipilih karena asumsi normalitas untuk uji-t parametrik terlanggar.
3. **Pemberian Makna Fisis pada PCA**:
   Mahasiswa tidak hanya menerima grafik PCA secara visual, tetapi secara mandiri menelaah dekomposisi matriks *loadings*: memahami mengapa `Monetary` dan `Frequency` berbobot positif pada PC1, serta mengapa `AvgOrderValue` memiliki kontribusi dominan (+0,68) pada PC2.
4. **Orisinalitas Pemikiran Bisnis**:
   Rekomendasi strategis (seperti penyiapan stok Q4 sejak bulan Agustus untuk mengantisipasi lonjakan omset 2x lipat dan strategi konversi *Guest Checkout*) merupakan hasil sintesis nalar mahasiswa atas konteks industri retail cinderamata daring.

---
