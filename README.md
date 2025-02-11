# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan internasional yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

## Permasalahan Bisnis

Jaya Jaya Institut menghadapi permasalahan tingginya angka dropout, yaitu 32,1%, yang mengindikasikan adanya masalah dalam mempertahankan mahasiswa agar dapat menyelesaikan studi mereka dengan baik. Oleh karena itu, penting bagi Jaya jaya institut untuk mendeteksi mahasiswa yang berisiko dropout lebih dini dan memberikan penanganan yang tepat untuk mengurangi angka tersebut.

## Cakupan Proyek

Proyek ini bertujuan untuk mengidentifikasi faktor yang mempengaruhi mahasiswa mengalami dropout, menganalisa data terkait dengan status akademik, usia saat pendaftaran, GDP, serta status beasiswa. Dengan memahami pola atau _anomali_ ini, Jaya Jaya Institut dapat memberikan perhatian khusus kepada mahasiswa yang berisiko dropout dan menerapkan kebijakan yang lebih efektif dalam mendukung kelulusan mereka.

Beberapa analisis yang dilakukan antara lain:
- Pengaruh jumlah *circular units* pada semester pertama dan kedua terhadap risiko dropout.
- Hubungan antara GDP mahasiswa dengan kemungkinan mereka untuk dropout.
- Analisis distribusi usia mahasiswa pada saat pendaftaran dan kaitannya dengan angka kelulusan.
- Peran status beasiswa dalam mempengaruhi tingkat dropout mahasiswa.

## Persiapan

Sumber data: 
```
https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance
```

Dashboard: 
```
https://lookerstudio.google.com/reporting/818c16d2-96d7-4745-8b48-5206f939ea7d
```

### Setup Environment

- Pastikan Python sudah terinstal di sistem. Jika belum,  bisa di download dari python.org
- Buat folder baru khusus untuk proyek ini
- Membuat Virtual Environtment
    - Buka cmd, lalu masukkan kode berikut,
    - `cd <path_file_proyek>`   (Berfungsi untuk masuk ke dalam file proyeknya)
    - `python -m venv .env`    (Install Environtment)
    - `.env\Scripts\activate`   (Mengaktifkan Virtual Environment)
- Install Dependencies
    - `pip install -r requirement.txt`

## Menjalankan Sistem Machine Learning

* **Marital Status**: Status pernikahan (Single = Belum menikah, Married = Menikah, Widower = Janda/Duda, Divorced = Cerai, Facto Union = Pernikahan tidak resmi, Legally Separated = Perceraian resmi)'
* **Nacionality**: Negara asal (Portugal, Jerman, Spanyol, Italia, Belanda, Inggris, Lituania, Angola, Kap Verde, Guinea, Mozambik, Sao Tomean, Turki, Brasil, Rumania, Moldova-Republik, Meksiko, Ukraina, Rusia, Kuba, Kolombia)'
* **Admission Grade**: Nilai masuk (0-200)'
* **Displaced**: Apakah siswa berasal dari keluarga kurang mampu?'
* **Educational Special Needs**: Apakah siswa memiliki kebutuhan khusus pendidikan?'
* **Debtor**: Apakah siswa memiliki tanggungan hutang?'
* **Tuition Fees**: Apakah siswa sudah melunasi pembayaran terkini?'
* **Scholarship Holder**: Apakah siswa mendapatkan beasiswa?'
* **Gender**: Jenis kelamin (Man = Laki-laki, Woman = Perempuan)'
* **Age At Enrollment**: Usia siswa saat melakukan enrollment'
* **International**: Apakah siswa berasal dari luar negeri?'
* **Unemployment Rate**: Tingkat pengangguran di daerah mahasiswa'
* **Inflation Rate**: Tingkat inflasi di daerah mahasiswa'
* **GDP (Gross Domestic Product**): Tingkat GDP di daerah mahasiswa'
* **Curriculum Unit**: Jumlah Curriculum yang dikreditkan, dienrollment, disetujui, dan nilainya. Baik pada semester 1 maupun semester 2'

```
https://proyekakhir-permasalahaninstitusipendidikan.streamlit.app/
```

## Conclusion

Berdasarkan analisis yang dilakukan, ditemukan beberapa faktor signifikan yang berkontribusi terhadap tingginya angka dropout:
1. **Jumlah Circular Units**: Mahasiswa yang mengambil kurang dari 5 unit per semester memiliki kecenderungan lebih tinggi untuk mengalami dropout.
2. **GDP Rendah**: Mahasiswa dengan GDP rendah lebih rentan untuk mengalami dropout, sementara mereka dengan GDP lebih tinggi memiliki peluang lebih besar untuk lulus.
3. **Usia Pendaftaran**: Mahasiswa berusia 18 tahun mendominasi populasi pendaftar.
4. **Status Beasiswa**: Mahasiswa yang tidak menerima beasiswa lebih sering mengalami dropout dibandingkan mereka yang menerima beasiswa.

## Rekomendasi Action Items

Berdasarkan temuan-temuan di atas, berikut adalah beberapa rekomendasi yang dapat diambil oleh Jaya Jaya Institut untuk mengurangi angka dropout dan meningkatkan tingkat kelulusan:

1. **Fokus pada Mahasiswa dengan Circular Units Rendah**: Mahasiswa yang mengambil kurang dari 5 unit per semester perlu mendapatkan perhatian khusus dan bimbingan intensif agar mereka dapat menyelesaikan pendidikan mereka dengan baik.
   
2. **Peningkatan Program Pembinaan untuk Mahasiswa dengan GDP Rendah**: Mahasiswa dengan GDP rendah harus diberikan dukungan ekstra, seperti tutor tambahan atau program remedial, bantuan dana melalui beasiswa, yang dimana bertujuan untuk meningkatkan kinerja akademik mereka.

3. **Dukungan untuk Mahasiswa yang Tidak Memiliki Beasiswa**: Menyediakan lebih banyak kesempatan beasiswa atau bantuan finansial bagi mahasiswa yang tidak memiliki beasiswa agar mereka dapat fokus pada studi mereka tanpa terbebani masalah keuangan.

4. **Pelatihan dan Konseling untuk Mahasiswa Baru**: Mengadakan program orientasi dan konseling yang lebih intensif untuk mahasiswa baru, terutama yang berusia 18 tahun, agar mereka dapat lebih siap menghadapi tantangan di perkuliahan dan mengurangi kemungkinan mereka keluar sebelum lulus.

5. **Pemantauan Berkala terhadap Mahasiswa Berisiko**: Melakukan pemantauan berkala terhadap mahasiswa yang berisiko tinggi untuk dropout, dengan menggunakan data seperti performa akademik, status beasiswa, dan jumlah unit yang diambil, sehingga dapat memberikan dukungan yang lebih cepat dan tepat sasaran.

Dengan langkah-langkah ini, Jaya Jaya Institut dapat lebih efektif dalam menurunkan angka dropout dan meningkatkan tingkat kelulusan mahasiswa, sehingga dapat mempertahankan reputasi sebagai institusi pendidikan berkualitas internasional.
