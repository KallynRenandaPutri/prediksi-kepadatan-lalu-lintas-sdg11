# Prediksi Tingkat Kepadatan Lalu Lintas - SDG 11

Project AI untuk mengklasifikasikan tingkat kepadatan lalu lintas menggunakan algoritma Decision Tree Classifier.

## Deskripsi Project

Project ini merupakan penerapan kecerdasan buatan (Artificial Intelligence) menggunakan algoritma **Decision Tree Classifier** untuk mengklasifikasikan tingkat kepadatan lalu lintas menjadi Rendah, Sedang, dan Tinggi.

Project ini berkaitan dengan** Sustainable Development Goal (SDG) 11: Sustainable Cities and Communities**, khususnya dalam pemanfaatan teknologi untuk membantu memahami kondisi transportasi perkotaan.

## Latar Belakang

Kepadatan lalu lintas merupakan salah satu permasalahan yang sering terjadi di wilayah perkotaan. Kondisi lalu lintas dapat dipengaruhi oleh beberapa faktor seperti waktu, hari, suhu, dan kondisi cuaca. Oleh karena itu, digunakan Machine Learning untuk mengklasifikasikan tingkat kepadatan lalu lintas menjadi tiga kategori, yaitu:
- Rendah
- Sedang
- Tinggi 

## Anggota Kelompok (Kelompok 11)

| No. | Nama | NIM |
|---|---|---|
| 1 | Muhammad Fajar M | F1G125040 |
| 2 | Kallyn Renanda Putri | F1G125035 |
| 3 | Sindi Aulia | F1G125077 |

## Problem

1. Bagaimana mengklasifikasikan tingkat kepadatan lalu lintas menjadi Rendah, Sedang, dan Tinggi?
2. Bagaimana menerapkan algoritma Decision Tree Classifier?
3. Seberapa baik performa model dalam melakukan klasifikasi?

## Tujuan

1. Melakukan data cleaning.
2. Melakukan preprocessing dan transformasi data.
3. Membuat kategori tingkat kepadatan lalu lintas.
4. Membangun model menggunakan Decision Tree Classifier.
5. Mengevaluasi performa model.
6. Melakukan prediksi terhadap data baru.

## Dataset

Dataset yang digunakan adalah **Metro Interstate Traffic Volume**
Sumber: UCI Machine Learning Repository. 
https://doi.org/10.24432/C5X60B.

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

Tahapan preprocessing data yang dilakukan:

1. Memasukkan dataset CSV.
2. Memeriksa struktur dan kondisi awal data.
3. Menghapus data duplikat.
4. Menangani nilai kosong.
5. Mengubah format tanggal dan waktu.
6. Membuat fitur waktu seperti jam, hari, bulan, tahun, dan hari dalam minggu.
7. Mengubah suhu menjadi Celsius.
8. Melakukan encoding pada kondisi cuaca

Setelah proses cleaning, diperoleh **48.187 data**.

## Kategori Tingkat Kepadatan

Volume lalu lintas diklasifikasikan menjadi tiga kategori menggunakan metode quantile:

- Rendah
- Sedang
- Tinggi
  
Kategori tersebut digunakan sebagai target atau label yang akan diprediksi oleh model.

## Pembagian Data

Data dibagi menjadi:

- **80% data training:** 38.549 data
- **20% data testing:** 9.638 data

Pembagian data menggunakan `train_test_split` dengan stratifikasi agar proporsi setiap kategori tetap terjaga.

## Algoritma

### Decision Tree Classifier

Decision Tree merupakan algoritma Machine Learning yang menggunakan struktur pohon untuk mengambil keputusan berdasarkan fitur yang tersedia.

Dalam project ini, Decision Tree digunakan untuk menentukan apakah kondisi lalu lintas termasuk Rendah, Sedang, atau Tinggi.

## Hasil pengujian model:

| Model | Accuracy |
|---|---|
| Decision Tree Classifier | 91,18% |

Model berhasil memperoleh akurasi sebesar 91,18% pada data testing.

### Classification Report

| Kategori | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Rendah | 0,95 | 0,95 | 0,95 |
| Sedang | 0,87 | 0,87 | 0,87 |
| Tinggi | 0,92 | 0,92 | 0,92 |

Hasil tersebut menunjukkan bahwa model dapat melakukan klasifikasi dengan performa yang cukup baik pada ketiga kategori.

## Feature Importance

Fitur yang paling berpengaruh terhadap hasil klasifikasi adalah:

1. Hour → 0,630248
2. Day of Week → 0,147220
3. Temp C → 0,071312
4. Day → 0,050348
5. Month → 0,037515

Fitur **hour** menjadi fitur yang paling dominan dalam menentukan klasifikasi tingkat kepadatan lalu lintas.

## Prediksi Data Baru

Model juga diuji menggunakan data baru dengan kondisi tertentu.

Contoh data baru:

- Jam: 16:00
- Suhu: 28°C
- Curah hujan: 0 mm
- Salju: 0 mm
- Tutupan awan: 40%
- Kondisi cuaca: Clear

Hasil prediksi: 
Tingkat kepadatan lalu lintas → **Tinggi**

## Hubungan dengan SDG 11

Project ini berkaitan dengan **SDG 11 – Sustainable Cities and Communities**  karena membahas permasalahan transportasi di kawasan perkotaan.

Pemanfaatan Machine Learning dapat menjadi contoh penggunaan teknologi berbasis data untuk memahami pola kepadatan lalu lintas dan mendukung pengelolaan transportasi yang lebih efektif.

Project ini merupakan project pembelajaran, sehingga hasil prediksi belum digunakan sebagai sistem pengaturan lalu lintas secara langsung.

## Kesimpulan

Project ini berhasil menerapkan **Decision Tree Classifier** untuk mengklasifikasikan tingkat kepadatan lalu lintas menjadi tiga kategori, yaitu Rendah, Sedang, dan Tinggi.

Model memperoleh akurasi sebesar **91,18%** pada data testing. Fitur yang paling berpengaruh adalah jam (hour) dengan nilai feature importance sebesar **0,630248**.

Hasil project menunjukkan bahwa Machine Learning dapat digunakan untuk membantu memahami pola kepadatan lalu lintas berdasarkan data waktu dan kondisi cuaca.

Project ini juga mendukung **pembahasan SDG 11** melalui pemanfaatan teknologi untuk permasalahan transportasi perkotaan.

## Teknologi yang Digunakan

- Python
- Google Colab
- Pandas
- Scikit-learn
- Matplotlib
- UCI Machine Learning Repository
- GitHub

## File Project

- `Tingkat__Kepadatan__Lalu__Lintas.ipynb` merupakan notebook yang berisi proses:

* Pengumpulan data
* Data cleaning
* Preprocessing
* Feature engineering
* Pembuatan kategori
* Training model
* Evaluasi model
* Feature importance
* Prediksi data baru
* Kesimpulan
