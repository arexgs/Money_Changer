# **IMPLEMENTASI ALGORITMA GREEDY UNTUK OPTIMASI PENUKARAN IDR KE USD**

Proyek ini merupakan implementasi *Algoritma Greedy* untuk mengoptimalkan proses penukaran mata uang Rupiah (IDR) ke Dollar Amerika Serikat (USD). Program ditulis menggunakan Python dan dirancang untuk menghasilkan kombinasi pecahan USD yang paling efisien (jumlah lembar/keping minimal).  
Program ini juga menggunakan nilai tukar real-time melalui library `forex_python` dan menyediakan nilai cadangan (*fallback*) apabila pengambilan kurs gagal.

## **📋 Deskripsi Proyek**
Program ini dikembangkan sebagai tugas akhir mata kuliah *Desain dan Analisis Algoritma*. Aplikasi ini menggunakan pendekatan algoritma Greedy untuk menentukan kombinasi denominasi USD (uang kertas dan koin) yang optimal saat menukarkan sejumlah uang Rupiah.

## **🔧 Fitur Utama**
- Konversi real-time IDR ke USD menggunakan forex-python.
- Memiliki *fallback rate* jika pengambilan kurs gagal.
- Mengonversi nilai IDR ke USD dengan pembulatan dua desimal.
- Menggunakan *Algoritma Greedy* untuk menentukan kombinasi pecahan optimal.
- Menampilkan rincian jumlah lembar/keping USD yang digunakan.

## **📦 Library**
- **Bahasa:** Python
- **Library:** 'forex-python' dan 'decimal'

## **💵 Denominasi USD Yang Digunakan**
Program menggunakan pecahan USD: $100, $50, $20, $10, $5, $1, $0.50, $0.25, %0.10, $0.05, $0.01
Struktur ini kanonik sehingga Greedy bisa selalu optimal.

## **🧠 Penjelasan Algoritma Greedy**
Algoritma Greedy bekerja dengan prinsip:
1. Selalu memilih pecahan terbesar yang mungkin digunakan.
2. Mengurangi nilai USD secara bertahap.
3. Mengulang hingga seluruh nilai terkonversi.
Karena USD memiliki struktur denominasi yang kanonik, algoritma Greedy selalu menghasilkan solusi optimal untuk meminimalkan jumlah lembar/keping.

## **🎯 Tujuan Proyek**
- Menerapkan Algoritma Greedy pada kasus nyata penukaran mata uang.
- Menghasilkan kombinasi pecahan USD yang minimal dan efisien.
- Menguji efektivitas Greedy dalam optimasi penukaran uang.


## DISUSUN OLEH KELOMPOK 3 KELAS C:
- Fathoni Nugroho (L0124055)
- Vici Oase (L0124081)
- Aisyah Zahrotul Jannah (L0124086)
- Az Zahra Sam Putri (L0124089)
