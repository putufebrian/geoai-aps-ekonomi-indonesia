# geoai-aps-ekonomi-indonesia

**geoai-aps-ekonomi-indonesia** adalah platform **Spatial Decision Support System (SDSS)** berbasis Web GIS yang dibangun dengan Django. Sistem ini dirancang untuk menganalisis data pertumbuhan PDRB (Produk Domestik Regional Bruto) di 38 provinsi Indonesia dan memberikan rekomendasi kebijakan ekonomi secara otomatis.

## 🚀 Fitur Utama

- **Peta Interaktif**: Visualisasi spasial menggunakan Folium dengan tiles *CartoDB Positron*.
- **Sistem Pengambil Keputusan (SPK)**: Klasifikasi otomatis berbasis data untuk menentukan intervensi pemerintah yang paling sesuai.
- **Analisis Ekonomi Otomatis**: Menggunakan metode kuantil untuk membagi wilayah ke dalam kategori ekonomi Rendah, Sedang, dan Tinggi.
- **Integrasi GeoJSON**: Menggunakan data batas wilayah terbaru untuk seluruh provinsi di Indonesia.
- **Upload Dynamic Data**: Kemampuan memperbarui basis data keputusan melalui unggahan file Excel secara langsung.

## 🛠️ Tech Stack

- **Backend**: Python, Django 5.2.10
- **Geospatial**: GeoPandas, Folium, GeoJSON
- **Data Science**: Pandas, Jinja2
- **Database**: SQLite3

## ⚙️ Cara Instalasi & Penggunaan

1. **Clone Repositori**
   ```bash
   git clone https://github.com/putufebrian/geoai-aps-ekonomi-indonesia.git
   cd geoai-aps-ekonomi-indonesia

2. **Buat file requirements.txt**
   Buat file bernama \`requirements.txt\` dan isi dengan:
   ```text
   django==5.2.10
   pandas
   geopandas
   folium
   openpyxl
   jinja2

3. **Install Dependensi**
   ```bash
   pip install -r requirements.txt

4. **Migrasi Database & Jalankan Server**
   ```bash
   python manage.py migrate
   python manage.py runserver
  Akses aplikasi di: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📊 Sistem Pengambil Keputusan & Sumber Data

### Mekanisme Keputusan
Sistem menggunakan modul \`ModelKebijakanEkonomi\` untuk mengolah data pertumbuhan dengan skema berikut:

| Kategori | Logika Kuantil | Warna Peta | Rekomendasi Kebijakan (Output SPK) |
| :--- | :--- | :--- | :--- |
| **RENDAH** | 33% Terendah | Merah (\`#d73027\`) | **STIMULUS EKONOMI & UMKM** |
| **SEDANG** | 33% Menengah | Kuning (\`#fee08b\`) | **PENGUATAN INDUSTRI DAERAH** |
| **TINGGI** | 33% Tertinggi | Hijau (\`#1a9850\`) | **EKSPANSI & INVESTASI** |

### Sumber Data PDRB
Data dapat diperoleh melalui portal resmi **BPS (Badan Pusat Statistik)**:
👉 [Laju Pertumbuhan PDRB per Provinsi (BPS)](https://www.bps.go.id/id/statistics-table/3/WnpCcmNtcE1ibkF5VjFSelJHMUVhRE52WjNWSVp6MDkjMw==/laju-pertumbuhan-produk-domestik-regional-bruto-atas-dasar-harga-konstan-2010-menurut-provinsi--persen---2022.html?year=2024)

## 📝 Panduan Upload Data
Aplikasi mendukung otomasi keputusan melalui file Excel dengan format:
- **Kolom A**: Nama Provinsi (Contoh: "BALI", "JAWA BARAT")
- **Kolom B**: Nilai Pertumbuhan PDRB (Format angka/desimal)
