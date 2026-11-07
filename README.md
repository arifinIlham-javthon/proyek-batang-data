# 📊 Analisis Ketimpangan Gender & Dashboard IPG Jawa Tengah 2025

**End-to-End Data Science Project | Data Extraction | Data Cleaning | Exploratory Data Analysis | Interactive Dashboard**

Repositori ini merupakan proyek Data Science yang berfokus pada analisis **Indeks Pembangunan Gender (IPG)** dan perbandingan Indeks Pembangunan Manusia (IPM) berdasarkan gender di seluruh kabupaten/kota Provinsi Jawa Tengah tahun 2025.

Proyek ini mencakup seluruh tahapan pengolahan data, mulai dari ekstraksi data publikasi Badan Pusat Statistik (BPS), pembersihan data, Exploratory Data Analysis (EDA), hingga implementasi dashboard web interaktif menggunakan Streamlit.

Salah satu fokus utama analisis adalah melihat posisi **Kabupaten Batang** dibandingkan dengan 34 kabupaten/kota lainnya di Jawa Tengah.

## 🔗 Live Demo

Dashboard interaktif dapat diakses melalui tautan berikut:

👉 **[Dashboard IPG Jawa Tengah 2025](https://proyek-batang-data-n7gzgh6ga9m7mwxcwrrprd.streamlit.app/)**

## 📌 Latar Belakang

Data statistik pembangunan gender dan pembangunan manusia yang dipublikasikan oleh BPS sering kali tersedia dalam format PDF. Format tersebut kurang fleksibel untuk keperluan pengolahan, eksplorasi, dan visualisasi data lebih lanjut.

Proyek ini bertujuan untuk mengatasi permasalahan tersebut melalui proses ekstraksi tabel PDF secara terstruktur, pembersihan data, serta analisis statistik untuk memperoleh informasi yang lebih mudah dipahami.

Melalui proyek ini, dilakukan analisis untuk mengetahui:

- Perbandingan nilai IPG antar kabupaten/kota di Jawa Tengah.
- Perbedaan capaian IPM antara laki-laki dan perempuan.
- Posisi Kabupaten Batang dalam pembangunan gender.
- Daerah dengan kesenjangan pembangunan manusia berdasarkan gender terbesar maupun terkecil.

Hasil analisis kemudian disajikan dalam bentuk dashboard interaktif agar informasi dapat diakses dan dieksplorasi dengan lebih mudah.

## 🎯 Tujuan Proyek

1. Mengotomatisasi proses ekstraksi data statistik dari publikasi PDF BPS.
2. Melakukan data cleaning dan preprocessing untuk menghasilkan dataset yang siap dianalisis.
3. Mengidentifikasi pola dan ketimpangan pembangunan manusia berdasarkan gender.
4. Membandingkan kondisi Kabupaten Batang dengan kabupaten/kota lainnya di Jawa Tengah.
5. Menyajikan hasil analisis melalui dashboard interaktif.

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|---|---|
| **Python 3.14** | Bahasa pemrograman utama |
| **pdfplumber** | Ekstraksi tabel dari dokumen PDF BPS |
| **Pandas** | Manipulasi, pembersihan, dan pengolahan data |
| **NumPy** | Operasi numerik dan pengolahan data |
| **Matplotlib** | Visualisasi data |
| **Seaborn** | Visualisasi statistik pada tahap EDA |
| **Jupyter Notebook** | Eksperimen dan dokumentasi analisis data |
| **Streamlit** | Pengembangan dashboard web interaktif |
| **uv & venv** | Manajemen dependensi dan virtual environment |

## ⚙️ Alur Kerja Proyek (Workflow)

Proyek ini menggunakan pendekatan end-to-end Data Science dengan tahapan sebagai berikut:

1. **Data Collection**  
   Mengumpulkan publikasi statistik BPS yang memuat informasi IPG dan IPM berdasarkan gender.

2. **Data Extraction**  
   Mengekstrak tabel dari dokumen PDF menggunakan library `pdfplumber` dan mengubahnya menjadi format CSV.

3. **Data Cleaning & Preprocessing**  
   Membersihkan data, menangani nilai kosong (*missing values*), serta memastikan format dan struktur dataset konsisten.

4. **Exploratory Data Analysis (EDA)**  
   Melakukan eksplorasi data untuk menemukan pola, tren, perbandingan, dan kesenjangan pembangunan manusia berdasarkan gender.

5. **Data Visualization**  
   Menyajikan hasil eksplorasi menggunakan visualisasi statistik.

6. **Dashboard Development**  
   Mengimplementasikan hasil pengolahan dan analisis data ke dalam dashboard interaktif menggunakan Streamlit.

## 📂 Struktur Repositori

```text
proyek-batang-data/
│
├── data/
│   ├── raw/                       # Dokumen PDF asli dari BPS
│   └── processed/                 # Dataset CSV hasil preprocessing
│
├── notebooks/
│   ├── 01_pdf_extraction.ipynb    # Ekstraksi PDF menjadi CSV
│   ├── 02_data_cleaning.ipynb     # Data cleaning dan handling missing values
│   └── 03_eda.ipynb               # Exploratory Data Analysis dan visualisasi
│
├── app.py                         # Aplikasi utama Streamlit
├── requirements.txt               # Daftar dependensi Python
└── README.md                      # Dokumentasi proyek
```

## 💡 Insight Utama (Temuan Analisis)

Berdasarkan hasil pengolahan dan analisis data, diperoleh beberapa temuan utama:

### 1. Posisi Kabupaten Batang

Kabupaten Batang berada pada peringkat ke-20 dari 35 kabupaten/kota di Jawa Tengah dengan nilai IPG sebesar **93,22**.

Selisih nilai IPM antara laki-laki dan perempuan relatif kecil, yaitu sekitar 5 poin. Hal ini menunjukkan adanya kesenjangan capaian pembangunan manusia berdasarkan gender yang perlu terus diperhatikan.

### 2. Anomali Positif: Klaten dan Karanganyar

Kabupaten Klaten dan Karanganyar menunjukkan kondisi menarik, yaitu nilai IPM perempuan yang lebih tinggi dibandingkan laki-laki.

Temuan ini memperlihatkan bahwa capaian pembangunan manusia perempuan di kedua daerah tersebut relatif lebih baik berdasarkan indikator yang digunakan.

### 3. Tantangan Pembangunan: Grobogan dan Cilacap

Kabupaten Grobogan dan Cilacap memiliki selisih IPM antara laki-laki dan perempuan yang relatif besar, yaitu di atas 10 poin.

Kondisi tersebut menunjukkan adanya kesenjangan capaian pembangunan manusia berdasarkan gender yang perlu mendapatkan perhatian lebih lanjut.

> Catatan: Interpretasi penyebab kesenjangan memerlukan analisis indikator yang lebih spesifik, seperti pendidikan, kesehatan, dan ekonomi. Nilai IPM saja belum cukup untuk menyimpulkan penyebab ketimpangan.

## 🚀 Menjalankan Proyek Secara Lokal

Ikuti langkah-langkah berikut untuk menjalankan proyek di komputer lokal.

### 1. Clone Repository

```bash
git clone https://github.com/arifinIlham-javthon/proyek-batang-data.git

cd proyek-batang-data
```

### 2. Membuat Virtual Environment

Menggunakan Python:

```bash
python -m venv .venv
```

### 3. Mengaktifkan Virtual Environment

**Windows (Command Prompt / PowerShell):**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Menginstal Dependensi

```bash
pip install -r requirements.txt
```

### 5. Menjalankan Dashboard

```bash
streamlit run app.py
```

Setelah berhasil dijalankan, Streamlit akan menyediakan alamat lokal untuk membuka dashboard melalui browser.

## 📈 Hasil Akhir

Hasil akhir dari proyek ini adalah sebuah dashboard interaktif yang memungkinkan pengguna untuk mengeksplorasi data pembangunan gender di Jawa Tengah, membandingkan capaian antarwilayah, serta mengamati posisi Kabupaten Batang berdasarkan indikator yang dianalisis.

**Dashboard:** [IPG Jawa Tengah 2025](https://proyek-batang-data-n7gzgh6ga9m7mwxcwrrprd.streamlit.app/)

---

**Author:** [Arifin Ilham](https://github.com/arifinIlham-javthon)

**GitHub Repository:** [proyek-batang-data](https://github.com/arifinIlham-javthon/proyek-batang-data)