

# 📘 **Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju**

### 🏢 **Business Understanding**

**Latar Belakang Bisnis**

Jaya Jaya Maju merupakan perusahaan multinasional yang berdiri sejak tahun 2000, dengan lebih dari 1000 karyawan yang tersebar di berbagai wilayah Indonesia. Sebagai perusahaan yang sudah cukup matang dan memiliki jaringan besar, mereka terus berusaha menjaga efisiensi dan stabilitas operasional. Namun, dalam beberapa tahun terakhir, perusahaan menghadapi tantangan serius terkait **tingginya tingkat attrition** (keluar masuknya karyawan), yang telah mencapai lebih dari **10%**.  

Tingginya tingkat attrition berisiko mengganggu produktivitas, meningkatkan biaya rekrutmen dan pelatihan, serta merusak budaya kerja di perusahaan. Oleh karena itu, divisi HR ingin melakukan analisis data untuk memahami faktor-faktor utama yang menyebabkan karyawan keluar dari perusahaan, serta menyusun strategi preventif berbasis data.

---

### Permasalahan Bisnis

Permasalahan utama yang dihadapi meliputi:

* Tingkat attrition yang tinggi sehingga memengaruhi performa dan efisiensi organisasi secara keseluruhan.
* Belum tersedianya sistem monitoring yang handal untuk mengidentifikasi dan menganalisis faktor penyebab attrition.
* Kurangnya keputusan berbasis data dalam upaya meningkatkan retensi karyawan.

### Cakupan Proyek

Fokus proyek ini adalah melakukan analisis serta membangun model prediksi attrition karyawan berdasarkan atribut personal, pekerjaan, dan faktor organisasi. Lingkup pekerjaan meliputi:

* **Pemahaman Data (Data Understanding)**

  * Melakukan import dan eksplorasi awal terhadap dataset karyawan yang bersumber dari data terbuka.
  * Memeriksa struktur, jenis data, dan distribusi nilai setiap variabel.

* **Pembersihan dan Persiapan Data (Data Cleaning & Preparation)**

  * Menangani nilai hilang pada kolom Attrition.
  * Menghapus fitur yang tidak relevan dalam pemodelan.
  * Membersihkan data duplikat dan mengidentifikasi outlier dengan visualisasi boxplot.
  * Menyesuaikan tipe data dan melakukan encoding pada variabel kategori.

* **Eksplorasi Data (Exploratory Data Analysis / EDA)**

  * Memvisualisasikan distribusi variabel target Attrition.
  * Menganalisis hubungan antar fitur numerik menggunakan korelasi Pearson.
  * Membuat scatter plot antara TotalWorkingYears dan MonthlyIncome untuk mengamati pola.

* **Pemodelan Data (Modeling)**

  * Membangun beberapa model klasifikasi seperti K-Nearest Neighbors, Decision Tree, Random Forest, Support Vector Machine, dan Naive Bayes.
  * Melakukan pembagian data menjadi set pelatihan dan pengujian dengan train-test split.

* **Evaluasi Model (Evaluation)**

  * Mengukur kinerja model dengan metrik akurasi, presisi, recall, dan F1-score.
  * Menampilkan confusion matrix untuk mengevaluasi distribusi prediksi.

* **Pelaporan Hasil**

  * Menyajikan ringkasan hasil performa model dalam bentuk tabel.
  * Menentukan model dengan performa terbaik berdasarkan metrik evaluasi.

### Persiapan

Sumber data: [Employee Data Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

Setup lingkungan kerja:

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import joblib
```

## 📊 **Business Dashboard**

Dashboard yang dibuat bertujuan untuk memberikan gambaran menyeluruh mengenai **tingkat attrition (keluar masuk karyawan)** di perusahaan Jaya Jaya Maju. Visualisasi mencakup berbagai dimensi seperti:

* **Lama bekerja di perusahaan**
* **Rentang usia**
* **Jarak tempat tinggal dari kantor**
* **Pengaruh lembur (OverTime)**
* **Level jabatan**
* **Keterlibatan kerja (Job Involvement)**
* **Departemen kerja**

Dashboard ini memudahkan manajemen dan tim HR untuk **mengidentifikasi pola dan faktor utama** yang berkontribusi terhadap tingginya attrition. Dengan insight dari dashboard ini, keputusan strategis dapat dibuat secara **berbasis data (data-driven decision making)**.

> *(Link dashboard tidak tersedia karena berbentuk gambar. Namun, dapat diimplementasikan menggunakan tools seperti Power BI, Tableau, atau Google Data Studio berdasarkan struktur visual yang ditampilkan.)*

---

## **Conclusion**

Berdasarkan hasil visualisasi dan analisis data, ditemukan bahwa **tingginya tingkat attrition** di perusahaan Jaya Jaya Maju disebabkan oleh kombinasi beberapa faktor, di antaranya:

* Tingginya jumlah karyawan yang keluar pada **tahun-tahun awal bekerja (terutama tahun pertama)**
* Karyawan dengan usia muda (20–29 tahun) cenderung keluar lebih banyak
* Lembur yang berlebihan berkorelasi dengan tingkat keluar yang tinggi
* Level jabatan rendah (1 dan 2) menunjukkan tingkat attrition paling tinggi
* Departemen **Sales dan R\&D** menyumbang jumlah keluar terbanyak

Hal ini menunjukkan bahwa **perusahaan memiliki tantangan besar dalam mempertahankan karyawan muda dan level entry** yang kemungkinan besar belum merasa cukup terikat atau memiliki prospek karier yang jelas.

---

## **Rekomendasi Action Items**

### **Action Item 1: Implementasi Program Retensi Dini**

Fokus pada karyawan di tahun pertama dengan program seperti:

* Onboarding yang terstruktur
* Mentoring personal
* Evaluasi dan diskusi karier berkala di 3 dan 6 bulan pertama

### 🧭 **Action Item 2: Audit dan Reduksi Beban Lembur**

Lakukan audit beban kerja dan kebijakan lembur, terutama pada departemen yang memiliki tingkat attrition tinggi. Tinjau ulang sistem target atau insentif yang mungkin menyebabkan overwork.

### 👥 **Action Item 3: Program Keterlibatan Karyawan Muda**

Tawarkan program pengembangan karier jangka pendek, sertifikasi, atau pelatihan berbasis minat untuk usia 20–29 tahun agar mereka melihat prospek jangka panjang di perusahaan.

### 📊 **Action Item 4: Monitoring Rutin Melalui Dashboard**

Gunakan dashboard attrition ini sebagai alat **monitoring bulanan**. Update data secara berkala dan gunakan insight-nya untuk **early intervention** jika ditemukan tren negatif baru.