# Studi_Kasus_6_Graceilla-Tifunny-Glory.H

NAMA : Graceilla Tifunny Glory Hutagalung

NIM : 2609116079

Kelas : B

STUDI KASUS 6 (NIM Ganjil)

PENJELASAN KODE:

1. import json

   kode ini untuk memanggil pustaka atau bantuan yang namanya json, agar bisas membaca dan menyimpan data ke file.json. Tanpa baris ini, program tidak bisa baca atau siimpan data ke file.

2. baca_data()

   bagian ini fungsinya membuaka file dan mengambil data yang sudah tersimpan. Caranya, Membuka file yang sama data_nilai.json untuk dibaca saja. yang kedua bisa mengambil semua isi data di dalamnya, lalu mengembalikan data itu ke bagian yang memangillnya supaya bisa dipakai. Kalau di dalam file sudah ada nama-nama mahasiswa, semua akan diambil dan ditampilkan. singkatnya "Ambil data dari penyimpanan ke program".

3. simpan_data(data)

   Bagian ini kebalikan dari baca data. fungsinya menyimpan data ke dalam file. Caranya, membuka file data_nilai.json untuk ditulis, Memasukkan semua data yang ada saat ini ke dalam file. Lalu untuk mengatur tulisannya supaya rapi dan mudah dibaca. Setelah di simpan, data itu tetap ada walau program dimatikan atau keluar. Singkatnya "Taruh data ke penyimpanan agar tidak hilang".

4. tampilkan_semua()

   Bagian ini fungsinya menunjukkan semua data ke layar. Langkah kerjanya pertama, panggil fungsi baca_data() untuk ambil data baru. dan cek apakah datanya kosong? Kalau kosong tampil tulisan "Belum ada data nilai" lalu berhenti. Kalaun sudah ada isinya, tampilkan garis pembatas supaya rapi, Tampilkan judul kolom (NO, Nama, NIM, Mata Kuliah, Nilai, Status). Tampilkan data satu per satu berurutan, Setiap data ditampilkan sesuai urutan nomor dari 1. singkatnya, "Tunjukkan semua yang sudah tersimpan di layar".

5. tambah_nilai()

   Bagian ini bagian yang paling lengkap, Fungsinya memasukkan data baru ke dalam daftar. Langkah kerjanya.
   - Meminta data dari pengguna dari (Nama Mahasiswa, NIM, Matkul, Nilai).
     
   - Lalu cek nilai apakah bener, Pastikan yang diketik itu angka, bukan huruf, dan angkanya pastikan dari 0-100 kalau salah, suruh ketik ulang sampai bener.
  
   - Tentukan status, Kalau nilai 75 atau lebih akan otomatis jadi "Lulus". Kalau di bawah 75 akan otomatis jadi "Tidak Lulus"
  
   - Susun data baru, Semua informasi tadi disatukan dalam satu. Pakai bentuk yang disebut Dictionary agar setiap info punya nama dan isinya.
  
   - Tambahkan ke daftar lama, Ambil daftar lama dari file, Lalu masukkan data baru ke bagian paling bawah. Dan simpan daftar yang sudah bertambah itu ke file.
  
   - Kasih tau berhasil atau tidak, tampilkan tulisan "Berhasil ditambahkan!" beserta statusnya. Singkatnya "Terima data baru lalu periksa bener atau salah, lalu simpan permanen.

6. menu()

   ini adalah tetap menampilkan menu berulang-ulang sampai pilih keluar.

   - Tampilkan judul program dan daftar pilihannya
  
     1) Lihat semua data
    
     2) Tambah data baru
    
     3) Keluar dari program

   - Mana yang mau dipilih.
  
   - Menjalankan fungsi sesuai pilihan:
  
     1) Jalankan fungsi tampil data
    
     2) Jalankan fungsi tambah data
    
     3) Pamit lalu berhenti total

    - Setelah selesai satu pekerjaan, menu muncul lagi untuk pilihan berikutnya.
Singkatnya "Pintu masuk program, pilih mau butuh apa, jalan terus sampai pilih keluar".

7. if__name__ == "__main__": Menu()

   ini perintah terakhir, Artinya: saat membuka dan menjalankan file ini, langsung jalankan fungsi menu(). Tampa baris ini, program tidak akan muncul apa-apa saat dibuka. singkatnya "Nyalakan program"


   HASIL OUTPUT PROGRAM:

   <img width="960" height="600" alt="Screenshot 2026-10-06 192553" src="https://github.com/user-attachments/assets/78f14648-3664-441c-a30c-1a60167b995c" />

  
   <img width="960" height="600" alt="Screenshot 2026-10-06 192607" src="https://github.com/user-attachments/assets/0b68d24b-2eea-4c37-b22e-451d759b2e28" />


   HASIL DATA BARU TETAP TERSIMPAN:

    <img width="960" height="600" alt="Screenshot 2026-10-06 192654" src="https://github.com/user-attachments/assets/0421030f-835d-4146-b3f3-a9385c49d6d9" />
