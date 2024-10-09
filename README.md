# Submission Dicoding "Belajar Analisis Data dengan Python"

## Analisis dengan Jupyter Notebook
Lihat detail analisis dan visualisasi ini pada buku catatan

## Menentukan Pertanyaan
- Pertanyaan 1: Pada Jam Berapa Jam Puncak dan Sepi Penyewaan Sepeda?
- Pertanyaan 2 : Bagaimana performa penjualan perusahaan selama beberapa tahun terakhir?
- Pertanyaan 3 : Lebih banyak orang yang mendaftar sebagai anggota atau lebih suka menyewa sepeda secara sekali pakai?

## Discussions and Results
1. Analisis data menunjukkan bahwa aktivitas penyewaan sepeda mencapai puncaknya pada sore hari pukul 17.00. Di sisi lain, dini hari pukul 04.00 menjadi periode dengan aktivitas penyewaan yang paling minim.
2. Grafik menunjukkan fluktuasi yang cukup signifikan dalam jumlah pesanan sepeda dari tahun ke tahun, dengan puncak tertinggi terjadi pada bulan September 2012 dan penurunan terendah pada bulan Januari 2011.
3. Sebagian besar pengguna layanan berbagi sepeda adalah pengguna terdaftar (registered riders) yang mencapai 81.2% dari total penggunaan, menunjukkan bahwa mayoritas pengguna lebih memilih untuk mendaftar sebelum menggunakan layanan. Sementara itu, hanya 18.8% pengguna yang termasuk dalam kategori casual riders, atau mereka yang belum mendaftar.

"Berdasarkan  analisis data penyewaan sepeda menunjukkan bahwa jam sibuk penyewaan terjadi pada pukul 17.00, sedangkan jam sepi pada pukul 04.00. Secara keseluruhan, terdapat fluktuasi jumlah penyewaan dari tahun ke tahun, dengan puncak tertinggi pada September 2012 dan titik terendah pada Januari 2011. Selain itu, sebagian besar pengguna adalah pelanggan terdaftar (registered riders), yang mencakup 81.2% dari total penyewaan, sementara 18.8% sisanya adalah penyewa kasual yang belum terdaftar."

## Project Analisis Data

Proyek ini berfokus pada analisis data dari Bike Sharing Dataset dengan tujuan akhir untuk mengungkap wawasan yang bermakna serta memberikan informasi yang dapat membantu pengambilan keputusan. Melalui eksplorasi dan analisis data ini, diharapkan dapat ditemukan pola-pola penting terkait penggunaan layanan berbagi sepeda, faktor-faktor yang mempengaruhi jumlah peminjaman sepeda, serta tren penggunaan berdasarkan waktu, cuaca, dan variabel lain. Hasil analisis ini diharapkan dapat memberikan kontribusi bagi perbaikan sistem layanan berbagi sepeda dan meningkatkan efisiensi operasional serta pengalaman pengguna.

## Struktur Direktori

- **/data**: Direktori ini berisi semua data mentah yang digunakan dalam proyek, umumnya dalam format .csv. Data ini mencakup informasi penting yang akan dianalisis, seperti catatan peminjaman sepeda, cuaca, dan data pendukung lainnya yang relevan dengan proyek.
- **/dashboard**: Direktori ini menyimpan file *main.py*, yang digunakan untuk membangun antarmuka visual atau dashboard interaktif. Dashboard ini berfungsi untuk menampilkan hasil analisis data secara dinamis, memungkinkan pengguna untuk memahami dan berinteraksi dengan informasi yang dihasilkan.
- **notebook.ipynb**: File ini berisi proses analisis data secara terperinci, mulai dari pembersihan data, eksplorasi, hingga visualisasi. Semua langkah analisis data dilakukan di sini, menggunakan *notebook* interaktif untuk mendokumentasikan serta menjalankan kode Python yang berhubungan dengan proyek.

## Instalasi

1. Clone repository ini ke komputer lokal Anda dengan menggunakan perintah berikut:

    ```shell
    git clone <URL_repository>
    ```

2. Setelah repository berhasil di-*clone*, pastikan bahwa Anda memiliki *library* Python yang diperlukan. Anda dapat menginstal semua pustaka yang dibutuhkan dengan menjalankan perintah berikut di terminal:

    ```shell
    pip install streamlit
    pip install -r requirements.txt
    ```

## Penggunaan

1. Setelah instalasi berhasil, masuk ke direktori proyek lokal dengan perintah berikut:

    ```shell
    cd bike-sharing/dashboard/
    ```

2. Jalankan aplikasi dashboard menggunakan *Streamlit* dengan menjalankan perintah berikut:

    ```shell
    streamlit run dashboard.py
    ```
Dashboard akan aktif, dan Anda dapat melihat hasil analisis data melalui antarmuka yang telah disiapkan.

![image](https://github.com/user-attachments/assets/40673a34-5565-4526-bef3-3502e0a088bb)

![image](https://github.com/user-attachments/assets/499d815b-ed32-4deb-8530-b9e960ae9dc0)

![image](https://github.com/user-attachments/assets/3a8ed7de-7f15-4382-9a90-47b382ceea52)

![image](https://github.com/user-attachments/assets/d1ac8a22-8715-41c3-93d0-3f352f284585)

![image](https://github.com/user-attachments/assets/08157a36-8028-4f53-b2f1-98166aab2011)








