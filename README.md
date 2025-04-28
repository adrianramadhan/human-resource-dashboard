# Proyek Akhir: Menyelesaikan Permasalahan Human Resource Perusahaan Jaya Jaya Maju

## Business Understanding

### Latar Belakang Bisnis

Jaya Jaya Maju adalah perusahaan multinasional yang berdiri sejak tahun 2000 dengan lebih dari 1.000 karyawan tersebar di berbagai wilayah Indonesia. Pertumbuhan pesat perusahaan diikuti tantangan dalam mengelola SDM, terutama **tingkat attrition >10% per tahun**. Dampaknya meliputi:

- Biaya rekrutmen dan pelatihan yang tinggi.
- Gangguan operasional dan penurunan produktivitas tim.

### Permasalahan Bisnis

1. **Tingginya Attrition Rate**
   - Kehilangan talenta kritis dan biaya penggantian karyawan yang signifikan.
2. **Kurangnya Pemahaman Faktor Penyebab**
   - Belum teridentifikasi variabel kunci (gaji, kepuasan kerja, jarak rumah, job role) yang memengaruhi keputusan resign.
3. **Tidak Ada Sistem Monitoring Proaktif**
   - HR hanya bereaksi setelah karyawan mengundurkan diri tanpa alat prediksi risiko attrition.
4. **Inefisiensi Pengambilan Keputusan**
   - Program retensi sulit diukur efektivitasnya tanpa analisis data.

### Cakupan Proyek

1. **Data Understanding & EDA**
   - Eksplorasi data karyawan (demografi, pekerjaan, kompensasi, kepuasan) untuk identifikasi pola attrition.
2. **Data Preparation**
   - Pembersihan data, imputasi _missing values_, encoding, dan penanganan _class imbalance_.
3. **Modeling**
   - Membangun model prediksi attrition (Logistic Regression, Random Forest) dengan _hyperparameter tuning_.
4. **Evaluation**
   - Pengukuran performa model menggunakan ROC-AUC, precision, recall, dan F1-score.
5. **Business Dashboard**
   - Pengembangan dashboard interaktif di Metabase untuk memonitor risiko attrition dan rekomendasi retensi.
6. **Deployment Lokal**
   - Penyajian model dan dashboard dalam lingkungan lokal (container Metabase).

## Persiapan

Berikut tahapan singkat untuk menyiapkan environment dan menjalankan script prediksi:

- **Sumber data**:  
  https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

- **Setup environment (conda)**:
  1. Buka terminal/PowerShell
  2. Buat dan aktifkan env:
     ```bash
     conda create --name prediksi_attrition python=3.9
     conda activate prediksi_attrition
     ```
  3. Instal library yang dibutuhkan:
     ```bash
     pip install numpy==2.2.5 pandas==2.2.3 matplotlib==3.10.1 seaborn==0.13.2 scikit-learn==1.6.1 SQLAlchemy==2.0.40 python-dotenv psycopg2-binary joblib
     ```
  4. Jalankan Jupyter Notebook (atau VSCode):
     ```bash
     jupyter-notebook
     ```
- **Credential Supabase (untuk Metabase)**:

  - Host: `aws-0-ap-southeast-1.pooler.supabase.com`
  - Port: `6543`
  - Database: `postgres`
  - User: `postgres.yvfheuwphfzqfsppwybl`
  - Password: `<YOUR-PASSWORD>`
  - Pool mode: `transaction`

- **Menjalankan script prediksi**:

  1. Buka `prediksi_hardcode.py`
  2. Sesuaikan hard-coded input di variabel `data`
  3. Jalankan:
     ```bash
     python prediksi_hardcode.py
     ```
  4. Hasil prediksi (“Stay”/“Resign”) dan probabilitas akan dicetak di console.

- **Email dan password Metabase**:
  - Email: adrianramadhan881@gmail.com
  - Password: root123

## Business Dashboard

Dashboard “HR Attrition Insights” mencakup beberapa kartu visualisasi utama untuk membantu departemen HR memahami faktor-faktor yang mempengaruhi attrition, yaitu: Attrition Rate by Department, Top JobRoles with Highest Attrition, Overtime Impact on Attrition, Attrition Rate by Gender, Attrition Rate by EducationField, dan Average YearsAtCompany by Attrition. Masing-masing pertanyaan bisnis menggunakan jenis chart yang sesuai—bar chart, horizontal bar, dan line chart—sehingga memudahkan identifikasi departemen, role, demografi, dan durasi kerja yang paling berisiko.  

---

## Conclusion

Setelah melakukan rangkaian analisis data, pemodelan machine learning, dan pembuatan dashboard interaktif, kini kita memiliki gambaran menyeluruh mengenai faktor-faktor yang mendorong attrition di Jaya Jaya Maju. Dengan memadukan kekuatan model prediksi dan visualisasi data, tim HR dapat bergerak dari pendekatan reaktif menjadi proaktif dalam mempertahankan talenta. Berikut ringkasan performa model dan insight bisnis, serta rekomendasi langkah selanjutnya.

### Model Performance:

- **ROC-AUC**: ~0.82
- **Logistic Regression**:
  - Recall 75% _(baik untuk deteksi resign)_
- **Random Forest**:
  - Precision 82% _(baik untuk prediksi resign)_

### Insight Dashboard:

- Memudahkan identifikasi faktor risiko attrition berdasarkan:
  - Departemen
  - Job role
  - Karakteristik karyawan

---

## Rekomendasi Action Items

### 1. Dept R&D & Sales

- Lakukan exit interview mendalam
- Tinjau struktur bonus & career-path

### 2. Pria (Male) Lebih Sering Resign

- Program retensi "gender-aware"
- Sediakan:
  - Fleksibilitas cuti
  - Mentoring

### 3. Overtime >10 Jam/Bulan

- Batasi overtime maksimal **5-10 jam/bulan**
- Sediakan program kesejahteraan

### 4. Laboratory Technician & Sales Executive

- Review shift kerja laboratorium
- Tambahkan insentif retention untuk Sales Executive

### 5. Resign di Tahun ke-0-5

- Implementasi:
  - Onboarding & mid-term review
  - Program buddy system

### 6. Life Sciences & Medical Field

- Sediakan training lanjutan
- Buat forum cross-functional

### 7. Job Satisfaction Rendah

- Survey kepuasan triwulanan
- Program recognition untuk karyawan dengan skor rendah
