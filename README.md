

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

### **Business Dashboard**

Dashboard "Attrition Overview Dashboard" adalah alat visualisasi data yang komprehensif, dirancang untuk memberikan pemahaman mendalam mengenai pola dan faktor-faktor yang berkontribusi terhadap tingkat *attrition* (keluar masuknya karyawan) di perusahaan Jaya Jaya Maju. Dashboard ini menyajikan berbagai metrik kunci melalui grafik dan bagan yang intuitif, memungkinkan divisi HR dan manajemen untuk dengan cepat mengidentifikasi area masalah dan membuat keputusan berbasis data.

**Komponen Utama Dashboard:**

* **Distribusi Karyawan Bertahan vs. Keluar:** Memberikan gambaran persentase karyawan yang masih aktif dan yang telah meninggalkan perusahaan.
* **Tren Attrition Berdasarkan Lama Bekerja:** Menunjukkan bagaimana tingkat *attrition* bervariasi seiring dengan masa kerja karyawan, menyoroti periode kritis di mana karyawan cenderung keluar.
* **Tren Attrition Berdasarkan Rentang Usia:** Mengidentifikasi kelompok usia mana yang memiliki tingkat *attrition* tertinggi.
* **Attrition per Departemen:** Memperlihatkan departemen mana yang paling terpengaruh oleh *attrition*, membantu dalam penargetan intervensi.
* **Attrition Berdasarkan Jarak (distance\_group):** Menganalisis dampak jarak tempuh karyawan dari rumah ke kantor terhadap keputusan untuk berhenti.
* **Pengaruh OverTime:** Menilai korelasi antara jam kerja lembur dan tingkat *attrition*.
* **Attrition Level Jabatan (JobLevel):** Menjelaskan bagaimana *attrition* berbeda di berbagai tingkatan jabatan dalam organisasi.
* **Attrition Berdasarkan Keterlibatan Kerja (Job Involvement):** Mengungkap hubungan antara tingkat keterlibatan karyawan dengan kemungkinan mereka untuk keluar.

### **Conclusion**

Proyek analisis *attrition* menggunakan "Attrition Overview Dashboard" telah menghasilkan beberapa kesimpulan kunci mengenai permasalahan tinggi tingkat keluar masuknya karyawan di Jaya Jaya Maju:

1.  **Karyawan Muda dan Baru Sangat Rentan:** Tingkat *attrition* tertinggi ditemukan pada karyawan dengan masa kerja di bawah 5 tahun dan kelompok usia 20-39 tahun, khususnya di Job Level 1 dan 2. Ini menunjukkan adanya tantangan serius dalam fase awal adaptasi dan pengembangan karir karyawan.
2.  **Overtime adalah Pemicu Utama:** Karyawan yang sering melakukan kerja lembur (Overtime: Ya) menunjukkan tingkat *attrition* yang jauh lebih tinggi dibandingkan dengan yang tidak. Hal ini mengindikasikan bahwa beban kerja berlebihan atau kurangnya *work-life balance* menjadi faktor signifikan.
3.  **Keterlibatan Kerja Berpengaruh:** Karyawan dengan tingkat keterlibatan kerja "Rendah" dan "Sedang" memiliki kecenderungan lebih tinggi untuk keluar, menyoroti pentingnya kepuasan dan koneksi karyawan terhadap pekerjaan mereka.
4.  **Variasi Attrition Antar Departemen dan Jarak:** Departemen Sales dan HR menunjukkan pola *attrition* yang perlu perhatian, sementara faktor jarak tempuh (baik sangat dekat maupun sangat jauh) juga berkorelasi dengan tingkat *attrition*.

Secara keseluruhan, konklusi proyek ini adalah bahwa *attrition* di Jaya Jaya Maju bukan disebabkan oleh satu faktor tunggal, melainkan kombinasi dari masa kerja yang pendek, beban kerja lembur, kurangnya keterlibatan, dan faktor spesifik departemen/jarak. Untuk mengatasi masalah ini secara efektif, perusahaan perlu menerapkan pendekatan multi-faceted yang menargetkan akar masalah yang teridentifikasi.

### **Rekomendasi Action Items**

Berikut adalah beberapa rekomendasi *action items* yang harus dilakukan perusahaan guna menyelesaikan permasalahan *attrition* yang tinggi dan mencapai target retensi karyawan:

**Action Item 1: Inisiatif Retensi Karyawan Baru & Pengembangan Karir Awal**

* **Deskripsi:** Menerapkan program *mentorship* atau *buddy system* terstruktur untuk semua karyawan baru (Job Level 1 & 2) selama 6-12 bulan pertama. Bersamaan dengan itu, kembangkan dan komunikasikan jalur karir yang jelas serta sediakan pelatihan keterampilan (baik *soft skill* maupun *hard skill*) yang relevan untuk mendukung pertumbuhan mereka. Ini bertujuan untuk meningkatkan keterikatan dan mengurangi rasa ketidakpastian di awal karir mereka di perusahaan.
* **Tanggung Jawab:** Departemen HR (Talent Acquisition & Learning & Development), Manajer Departemen.
* **Metrik Keberhasilan:** Penurunan tingkat *attrition* pada 1 tahun pertama masa kerja (misalnya, target penurunan 5%), peningkatan skor kepuasan karyawan baru dalam survei *onboarding* (misalnya, target 10% peningkatan).
* **Timeline:** Perencanaan & Desain (Q3 2025), Implementasi Pilot Program (Q4 2025).

**Action Item 2: Pengelolaan Overtime dan Promosi Work-Life Balance**

* **Deskripsi:** Lakukan audit menyeluruh terhadap beban kerja dan jam kerja lembur di departemen-departemen kunci (terutama Sales), identifikasi penyebab utamanya (misalnya, kurangnya staf, inefisiensi proses). Berdasarkan audit, tetapkan batasan jam kerja lembur yang realistis dan terapkan kebijakan *overtime* yang lebih ketat, atau pertimbangkan penambahan staf jika diperlukan. Edukasi manajer tentang pentingnya *work-life balance* dan berikan mereka alat untuk mengelola beban kerja tim secara efektif.
* **Tanggung Jawab:** Manajemen Senior, Departemen HR (HR Business Partner), Kepala Departemen terkait.
* **Metrik Keberhasilan:** Penurunan rata-rata jam *overtime* per karyawan (misalnya, target 20% penurunan), penurunan *attrition* pada kelompok karyawan yang sebelumnya sering *overtime* (misalnya, target 15% penurunan), peningkatan persepsi karyawan terhadap *work-life balance* melalui survei (misalnya, target 10% peningkatan).
* **Timeline:** Audit & Rekomendasi (Q3 2025), Implementasi Kebijakan & Solusi (Q4 2025).