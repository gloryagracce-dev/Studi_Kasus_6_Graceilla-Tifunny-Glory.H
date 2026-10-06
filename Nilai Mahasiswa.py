import json

# ===== Fungsi Baca Data =====
def baca_data():
    with open("data_nilai.json", "r", encoding="utf-8") as f:
        return json.load(f)

# ===== Fungsi Simpan Data =====
def simpan_data(data):
    with open("data_nilai.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# ===== Fungsi Tampilkan Semua Data =====
def tampilkan_semua():
    data = baca_data()
    if len(data) == 0:
        print("\nBelum ada data nilai.")
        return
    
    print("\n" + "="*60)
    print(f"{'No':<4} {'Nama':<15} {'NIM':<14} {'Mata Kuliah':<20} {'Nilai':<6} {'Status'}")
    print("-"*60)
    for i, mhs in enumerate(data, start=1):
        print(f"{i:<4} {mhs['nama']:<15} {mhs['nim']:<14} {mhs['mata_kuliah']:<20} {mhs['nilai']:<6} {mhs['keterangan']}")
    print("="*60)

# ===== Fungsi Tambah Data Baru =====
def tambah_nilai():
    print("\n--- Tambah Data Nilai Baru ---")
    nama = input("Masukkan Nama Mahasiswa : ").strip()
    nim = input("Masukkan NIM Mahasiswa    : ").strip()
    mata_kuliah = input("Masukkan Mata Kuliah      : ").strip()
    
    while True:
        try:
            nilai = float(input("Masukkan Nilai (0-100)    : "))
            if 0 <= nilai <= 100:
                break
            else:
                print("Nilai harus 0 sampai 100!")
        except ValueError:
            print("Masukkan angka saja!")
    
    keterangan = "Lulus" if nilai >= 75 else "Belum Lulus"
    
    data_baru = {
        "nama": nama,
        "nim": nim,
        "mata_kuliah": mata_kuliah,
        "nilai": nilai,
        "keterangan": keterangan
    }
    
    data = baca_data()
    data.append(data_baru)
    simpan_data(data)
    print(f"Berhasil ditambahkan! Status: {keterangan}")

# ===== Menu Utama =====
def menu():
    while True:
        print("\n" + "="*40)
        print("   SISTEM PENCATATAN NILAI MAHASISWA")
        print("="*40)
        print(" 1. Lihat Semua Data Nilai")
        print(" 2. Tambah Data Nilai Baru")
        print(" 3. Keluar")
        print("="*40)
        
        pilih = input("Pilih menu [1-3]: ")
        
        if pilih == "1":
            tampilkan_semua()
        elif pilih == "2":
            tambah_nilai()
        elif pilih == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak ada! Coba lagi.")

# ===== Jalankan Program =====
if __name__ == "__main__":
    menu()