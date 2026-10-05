# Prediksi Tingkat Kepadatan Lalu Lintas - SDG 11

Project AI untuk mengklasifikasikan tingkat kepadatan lalu lintas menggunakan algoritma Decision Tree Classifier.

## Deskripsi Project

Project ini merupakan penerapan kecerdasan buatan (Artificial Intelligence) menggunakan algoritma Decision Tree Classifier untuk mengklasifikasikan tingkat kepadatan lalu lintas menjadi Rendah, Sedang, dan Tinggi.

Project ini berkaitan dengan Sustainable Development Goal (SDG) 11: Sustainable Cities and Communities, khususnya dalam pemanfaatan teknologi untuk membantu memahami kondisi transportasi perkotaan.

## Latar Belakang

Kepadatan lalu lintas merupakan salah satu permasalahan yang sering terjadi di wilayah perkotaan. Kondisi lalu lintas dapat dipengaruhi oleh beberapa faktor seperti waktu, hari, suhu, dan kondisi cuaca. Oleh karena itu, digunakan Machine Learning untuk mengklasifikasikan tingkat kepadatan lalu lintas menjadi tiga kategori, yaitu Rendah, Sedang, dan Tinggi.

## Anggota Kelompok

- Muhammad Fajar M — F1G125040
- Kallyn Renanda Putri — F1G125035
- Sindi Aulia — F1G125077

## Problem

1. Bagaimana mengklasifikasikan tingkat kepadatan lalu lintas menjadi Rendah, Sedang, dan Tinggi?
2. Bagaimana menerapkan algoritma Decision Tree Classifier?
3. Seberapa baik performa model dalam melakukan klasifikasi?

## Tujuan

1. Melakukan data cleaning.
2. Melakukan preprocessing dan transformasi data.
3. Membuat kategori tingkat kepadatan lalu lintas.
4. Membangun model Decision Tree Classifier.
5. Mengevaluasi performa model.
6. Melakukan prediksi terhadap data baru.

## Dataset

Dataset yang digunakan adalah **Metro Interstate Traffic Volume** dari UCI Machine Learning Repository.

Dataset awal memiliki **48.204 data**.

Dataset berisi data volume lalu lintas per jam beserta beberapa informasi pendukung, seperti:
* Waktu
* Hari
* Bulan
* Tahun
* Hari dalam minggu
* Suhu
* Curah hujan
* Salju
* Tutupan awan
* Kondisi cuaca
* Hari libur
* Volume lalu lintas

## Preprocessing Data

Tahapan preprocessing yang dilakukan:

1. Memasukkan dataset.
2. Memeriksa struktur data.
3. Menghapus data duplikat.
4. Menangani missing value.
5. Mengubah data tanggal dan waktu.
6. Membuat fitur waktu.
7. Mengubah suhu menjadi Celsius.
8. Melakukan encoding pada kondisi cuaca.

Setelah proses cleaning, diperoleh **48.187 data**.

## Kategori Tingkat Kepadatan

Volume lalu lintas diklasifikasikan menjadi tiga kategori menggunakan metode quantile:

- Rendah
- Sedang
- Tinggi

## Pembagian Data

Data dibagi menjadi:

- **80% data training:** 38.549 data
- **20% data testing:** 9.638 data

Pembagian data menggunakan `train_test_split` dengan stratifikasi.

## Algoritma

### Decision Tree Classifier

Decision Tree Classifier digunakan untuk melakukan klasifikasi tingkat kepadatan lalu lintas berdasarkan fitur-fitur yang tersedia.

## Hasil Pengujian

Model Decision Tree Classifier memperoleh **accuracy sebesar 91,18%** pada data testing.

### Classification Report

| Kategori | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Rendah | 0,95 | 0,95 | 0,95 |
| Sedang | 0,87 | 0,87 | 0,87 |
| Tinggi | 0,92 | 0,92 | 0,92 |

## Feature Importance

Fitur yang paling berpengaruh terhadap hasil klasifikasi adalah **Hour** dengan nilai importance sebesar **0,630248**.

## Prediksi Data Baru

Contoh data baru:

- Jam: 16:00
- Suhu: 28°C
- Curah hujan: 0 mm
- Salju: 0 mm
- Tutupan awan: 40%
- Kondisi cuaca: Clear

**Hasil prediksi: Tinggi**

## Hubungan dengan SDG 11

Project ini berkaitan dengan SDG 11 karena memanfaatkan teknologi Machine Learning untuk membantu memahami pola kepadatan lalu lintas di wilayah perkotaan.

Hasil klasifikasi dapat menjadi informasi untuk memahami kondisi transportasi dan mendukung pengembangan kota yang lebih berkelanjutan.

## Kesimpulan

Algoritma Decision Tree Classifier berhasil mengklasifikasikan tingkat kepadatan lalu lintas menjadi Rendah, Sedang, dan Tinggi dengan accuracy sebesar **91,18%**.

Fitur **Hour** menjadi fitur yang paling berpengaruh dalam proses klasifikasi. Project ini menunjukkan bahwa Machine Learning dapat digunakan untuk membantu memahami pola kepadatan lalu lintas dan mendukung SDG 11.

## Teknologi yang Digunakan

- Python
- Google Colab
- Pandas
- Scikit-learn
- Matplotlib
- UCI Machine Learning Repository
- GitHub

## File Project

- `Tingkat__Kepadatan__Lalu__Lintas.ipynb`

Notebook berisi proses data cleaning, preprocessing, feature engineering, klasifikasi, evaluasi model, feature importance, dan prediksi data baru.
