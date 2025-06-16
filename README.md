# 📘 **Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech**

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

### **Conclusion**
Berdasarkan hasil analisis data dan visualisasi dashboard "Attrition Overview", dapat disimpulkan bahwa permasalahan *attrition* di perusahaan **Jaya Jaya Maju** disebabkan oleh sejumlah pola dan faktor yang jelas, bukan oleh satu penyebab tunggal. Temuan-temuan utama yang menjawab permasalahan HR antara lain:

1. **Kelompok usia 20–24 tahun menunjukkan tingkat attrition tertinggi**, terutama bagi mereka yang berada di Job Level 1 dan memiliki masa kerja di bawah 2 tahun. Hal ini menunjukkan bahwa karyawan muda dengan pengalaman kerja awal cenderung meninggalkan perusahaan lebih cepat, terutama bila tidak mendapatkan pembinaan atau jalur karir yang jelas.

2. **Karyawan dengan tingkat kepuasan kerja rendah dan keterlibatan kerja (Job Involvement) rendah memiliki probabilitas attrition yang signifikan lebih tinggi** dibandingkan mereka yang merasa puas dan terlibat secara aktif dalam pekerjaan. Ini menandakan bahwa persepsi positif terhadap pekerjaan menjadi indikator kuat terhadap retensi karyawan.

3. **Departemen Sales memiliki angka attrition tertinggi dibandingkan departemen lain**, terutama pada posisi dengan jam lembur tinggi (OverTime). Ini menunjukkan bahwa beban kerja dan tekanan operasional di departemen ini menjadi pemicu utama keluarnya karyawan.

4. **Jarak tempat tinggal karyawan dari kantor (distance from home) berbanding lurus dengan kemungkinan keluar dari perusahaan.** Karyawan yang tinggal lebih dari 15 km dari kantor memiliki tingkat attrition lebih tinggi dibandingkan mereka yang tinggal lebih dekat. Jarak ini tampaknya memengaruhi work-life balance dan kelelahan harian.

5. **Karyawan dengan penghasilan bulanan (MonthlyIncome) yang relatif rendah cenderung lebih cepat keluar**, terutama jika dikombinasikan dengan faktor seperti lembur tinggi dan keterlibatan rendah. Ini mengindikasikan pentingnya insentif yang kompetitif dalam mempertahankan tenaga kerja.

6. **Attrition cenderung tinggi pada masa kerja 1–3 tahun pertama**, yang merupakan masa kritis adaptasi dan pembentukan loyalitas. Tanpa adanya program onboarding dan pendampingan yang kuat, karyawan dalam fase ini lebih berisiko keluar.

Melalui pemahaman mendalam atas pola-pola ini, departemen HR kini memiliki dasar data yang kuat untuk merancang strategi retensi yang lebih efektif dan tertarget, seperti:

* Fokus pada intervensi terhadap karyawan muda dan baru.
* Meningkatkan kepuasan kerja dan keterlibatan karyawan melalui program keterlibatan.
* Menyediakan fleksibilitas kerja bagi karyawan dengan jarak tempuh jauh.
* Meninjau ulang struktur kompensasi dan beban kerja di departemen yang memiliki tingkat attrition tinggi.


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

