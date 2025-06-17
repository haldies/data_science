# **Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech**

### **Business Understanding**

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

  * Membangun beberapa model klasifikasi seperti K-Nearest Neighbors, Random Forest dan xgboost.
  * Melakukan pembagian data menjadi set pelatihan dan pengujian dengan train-test split.

* **Evaluasi Model (Evaluation)**

  * Mengukur kinerja model dengan metrik akurasi, presisi, recall, dan F1-score.
  * Menampilkan confusion matrix untuk mengevaluasi distribusi prediksi.

* **Pelaporan Hasil**

  * Menyajikan ringkasan hasil performa model dalam bentuk tabel.
  * Menentukan model dengan performa terbaik berdasarkan metrik evaluasi.

### Persiapan

Sumber data: [Employee Data Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)


---
#### **1. Setup Lingkungan Kerja (Conda Environment)**

##### 🔹 Buat Environment Baru

```bash
conda create -n attrition_analysis python=3.11.13 -y
conda activate attrition_analysis
```

##### 🔹 Instalasi dari `requirements.txt`

Jika environment sudah dibuat:

```bash
pip install -r requirements.txt
```

---

#### **2. Setup Dashboard Metabase (Docker)**

##### 🔹 Jalankan Metabase di Docker

```powershell
docker run -d -p 3000:3000 `
  -v "${PWD}:/metabase-data" `
  -e "MB_DB_FILE=/metabase-data/metabase.db" `
  --name metabase metabase/metabase
```

> ⚠️ Untuk pengguna **Linux/Mac**, gunakan tanda `\` untuk line break atau tulis satu baris.

---

##### 🔹 Kredensial Metabase (Default Login)

| Item          | Value                                          |
| ------------- | ---------------------------------------------- |
| **URL Akses** | [http://localhost:3000](http://localhost:3000) |
| **Email**     | `root@mail.com`                                |
| **Password**  | `root123`                                      |
| **Port**      | 3000                                           |

### **Business Dashboard**

Dashboard yang dibangun tidak hanya menampilkan visualisasi pola attrition, tetapi juga menyertakan modul prediksi yang memungkinkan HR untuk menginput data karyawan dan memperoleh probabilitas risiko attrition secara real-time. Dengan demikian, dashboard ini menjadi alat bantu komprehensif yang menggabungkan analisis historis dan prediktif untuk mendukung pengambilan keputusan yang lebih cepat dan tepat sasaran.

**Komponen Utama Dashboard:**

* **Distribusi Karyawan Bertahan vs. Keluar:** Memberikan gambaran persentase karyawan yang masih aktif dan yang telah meninggalkan perusahaan.
* **Tren Attrition Berdasarkan Lama Bekerja:** Menunjukkan bagaimana tingkat *attrition* bervariasi seiring dengan masa kerja karyawan, menyoroti periode kritis di mana karyawan cenderung keluar.
* **Tren Attrition Berdasarkan Rentang Usia:** Mengidentifikasi kelompok usia mana yang memiliki tingkat *attrition* tertinggi.
* **Attrition per Departemen:** Memperlihatkan departemen mana yang paling terpengaruh oleh *attrition*, membantu dalam penargetan intervensi.
* **Attrition Berdasarkan Jarak (distance\_group):** Menganalisis dampak jarak tempuh karyawan dari rumah ke kantor terhadap keputusan untuk berhenti.
* **Pengaruh OverTime:** Menilai korelasi antara jam kerja lembur dan tingkat *attrition*.
* **Attrition Level Jabatan (JobLevel):** Menjelaskan bagaimana *attrition* berbeda di berbagai tingkatan jabatan dalam organisasi.
* **Attrition Berdasarkan Keterlibatan Kerja (Job Involvement):** Mengungkap hubungan antara tingkat keterlibatan karyawan dengan kemungkinan mereka untuk keluar.

---

### **Conclusion**
Berdasarkan hasil analisis data dan visualisasi dashboard "Attrition Overview", dapat disimpulkan bahwa permasalahan *attrition* di perusahaan Jaya Jaya Maju disebabkan oleh sejumlah pola dan faktor yang jelas, bukan oleh satu penyebab tunggal.Selain itu, saya juga **mengembangkan model machine learning menggunakan algoritma XGBoost yang dapat memprediksi** kemungkinan seorang karyawan akan keluar dari perusahaan berdasarkan data historis karyawan. Model ini berfungsi sebagai alat bantu proaktif bagi HR untuk mengidentifikasi karyawan yang berisiko tinggi keluar, sehingga dapat dilakukan intervensi lebih awal dan tepat sasaran. Dengan akurasi sekitar 85%, model ini membantu memprioritaskan upaya retensi secara efisien dan mengurangi potensi kehilangan talenta penting. Temuan-temuan utama yang menjawab permasalahan HR antara lain:

* **Kelompok usia 20-29 tahun menunjukkan tingkat *attrition* tertinggi.** Hal ini terlihat jelas pada grafik "Tren by Rentang Usia" di mana kelompok usia 20-29 memiliki "Rate yang keluar" (Rate of Exit) tertinggi, mencapai 61. Ini menunjukkan bahwa karyawan muda cenderung meninggalkan perusahaan lebih cepat.

* **Karyawan dengan Job Level 1 dan 2 memiliki angka *attrition* tertinggi.** Grafik "Attrition Level Jabatan" menunjukkan "Keluar" (Exit) tertinggi pada Job Level 1 (27.41%) dan Job Level 2 (19.16%). Hal ini mengindikasikan bahwa posisi staf atau entry-level memiliki tingkat keluar yang lebih tinggi.

* **Departemen Research & Development dan Sales memiliki angka *attrition* tertinggi.** Pada grafik "Attrition per Departemen", Research & Development menunjukkan jumlah "Keluar" (Exit) tertinggi dengan 101 karyawan, diikuti oleh Sales dengan 96 karyawan. Human Resources juga menunjukkan angka yang signifikan dengan 38 karyawan. Ini menunjukkan bahwa beban kerja dan kondisi spesifik di departemen ini mungkin menjadi pemicu utama keluarnya karyawan.

* **Karyawan dengan jam lembur tinggi (OverTime) memiliki probabilitas *attrition* yang signifikan lebih tinggi.** Grafik "Pengaruh OverTime" dengan jelas menunjukkan bahwa karyawan yang sering lembur ("Yes") memiliki jumlah "Keluar" (Exit) yang jauh lebih tinggi (98 orang) dibandingkan mereka yang tidak lembur ("No") (81 orang). Persentase keluar untuk karyawan lembur juga lebih tinggi (21.92%). Ini menandakan bahwa beban kerja yang berlebihan dapat menjadi penyebab utama keluarnya karyawan.

* **Jarak tempat tinggal karyawan dari kantor (Distance from Home) memiliki pola attrition yang bervariasi, tidak sepenuhnya berbanding lurus dengan jarak**. Jumlah karyawan yang keluar lebih tinggi pada jarak dekat (1–3 km), karena memang lebih banyak karyawan yang tinggal dekat kantor. Namun, persentase keluar di jarak menengah hingga jauh (15–29 km) cenderung lebih tinggi, misalnya pada jarak 24–25 km, tingkat keluar mencapai 28–33%. Ini menunjukkan bahwa jarak jauh tetap berisiko terhadap attrition, walaupun jumlah kasusnya lebih kecil secara absolut

* **Tingkat *attrition* cenderung tinggi pada masa kerja awal (0–2 tahun).** Data menunjukkan bahwa pada tahun ke-0, ke-1, dan ke-2, tingkat keluar masing-masing adalah 35.48%, 34.38%, dan 21.59%. Ini menandakan bahwa masa kerja awal merupakan periode paling kritis bagi retensi karyawan. Setelah tahun ke-3, persentase *attrition* cenderung menurun secara signifikan, dengan angka di bawah 20% dan bahkan turun hingga mendekati nol di beberapa tahun berikutnya.

Melalui pemahaman mendalam atas pola-pola ini, departemen HR kini memiliki dasar data yang kuat untuk merancang strategi retensi yang lebih efektif dan tertarget, seperti:

* Fokus pada intervensi terhadap karyawan muda, terutama di Job Level 1 dan 2.
* Menganalisis dan mengelola beban kerja, khususnya di departemen Research & Development dan Sales, serta meninjau kebijakan lembur.
* Menyediakan fleksibilitas kerja atau dukungan transportasi bagi karyawan dengan jarak tempuh jauh.
* Memperkuat program *onboarding* dan pembinaan bagi karyawan baru di masa kerja awal.


### **Rekomendasi Action Items (Optional)**

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

