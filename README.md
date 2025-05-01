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

| No | Insight Utama                                    | Action Item                                                                                                                                                               | KPI / Target                               | Pemilik        | Waktu Implementasi |
|----|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|----------------|--------------------|
| 1  | Dept R&D & Sales paling tinggi attrition         | • Exit interview mendalam pada 100% karyawan yang resign di R&D & Sales selama 3 bulan terakhir<br>• Review & revise struktur gaji, bonus, career-path untuk kedua dept.    | Turun attrition R&D & Sales 20% dalam 6 bln | HR Manager     | Q3 2025            |
| 2  | Pria (Male) lebih sering resign                  | • Desain dan jalankan program retensi “gender-aware” (flexi-cuti, mentoring circle) khusus male employees<br>• Survey kepuasan khusus gender setiap kuartal               | Peningkatan engagement score male +10%     | HR Business Partner | Q2 2025        |
| 3  | Overtime = Yes memiliki attrition tinggi         | • Kebijakan batasi overtime max 5–10 jam/bulan<br>• Program well-being: sesi yoga mingguan, konseling triwulanan<br>• Kompensasi lembur transparan                           | Turun % overtime >10 jtm by 50%            | Ops Manager    | Mulai Mei 2025     |
| 4  | Laboratory Technician & Sales Executive riskan   | • For Lab Tech: optimasi shift & workflow lab (Lean workshop)<br>• For Sales Exec: skema retention bonus triwulanan & recognition awards                                     | Retensi Lab Tech +15%; Sales +10%          | Dept Heads     | Q3 2025            |
| 5  | Life Sciences & Medical field tinggi attrition   | • Buat jalur karier riset: sertifikasi, rotasi project setiap 6 bln<br>• Forum cross-functional bulanan untuk knowledge sharing                                              | Penurunan attrition LifeSci/Medical 15%    | L&D Team       | Q3 2025            |
| 6  | JobSatisfaction rendah (1–2) → attrition tinggi  | • Survey kepuasan triwulanan + focus group discussion<br>• Program recognition & reward (Employee of the Month, shout-outs)<br>• Action plan per feedback survey            | Meningkatkan satisfaction score ≥3         | HR Analytics   | Mulai Mei 2025     |
