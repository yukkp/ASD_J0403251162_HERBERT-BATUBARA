# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama : Herbert Elia Christanto Batubara
# NIM :J0403251162
# Kelas : TPL A/2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    stock_dict={}
    with open(NAMA_FILE,"r")as file:
        for baris in file:
            baris=baris.strip()
# TODO: Buka file dan baca seluruh baris
            kode_barang,nama_barang,stock=baris.split(",")
            stock_dict[kode_barang]={"nama":nama_barang,"stock":int(stock)}
    return stock_dict

# buka_data =baca_stok(NAMA_FILE)
print('jumlah Data Terbaca =',len(buka_data))

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):

    with open(nama_file, "w",) as f:
        for kode_barang in sorted(stok_dict.keys()):
            nama = stok_dict[kode_barang]["nama"]
            stok = stok_dict[kode_barang]["stock"]
            f.write(f"{kode_barang},{nama},{stok}\n")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
# TODO: Jika kosong, tampilkan pesan stok kosong
    if not stok_dict:
        print("\nStok barang kosong.")
        return
    print("\n=============Stock Warehouse=============")
    print(f"{'Nomor Barang':<15} | {'Barang':<15} | {"Jumlah":>6}")
    print("-"*42)
# TODO: Tampilkan dengan format rapi: kode | nama | stok

    for kode_barang in sorted(stok_dict.keys()): 
        nama_barang= stok_dict[kode_barang]["nama"]
        jumlah_barang= stok_dict[kode_barang]["stock"]
        print(f"{kode_barang:<15} | {nama_barang:<15}|{jumlah_barang:>6}")

# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------
def cari_barang(stok_dict):

    kode = input("Masukkan kode barang: ").strip()

    if kode in stok_dict:
        nama_barang= stok_dict[kode]["nama"]
        jumlah_barang= stok_dict[kode]["stock"]
# TODO: Cek apakah kode ada di dictionary
        print('=====Data Mahasiswa Ditemukan=====')
        print(f"Nomor Barang:{kode}")
        print(f"Nama :{nama_barang}")
        print(f"Jumlah:{jumlah_barang}")
# Jika ada: tampilkan detail barang
# Jika tidak ada: tampilkan 'Barang tidak ditemukan'
    else:
        print("Data tidak Di temukan")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------

def tambah_barang(stok_dict):
    kode = input("Masukkan kode barang baru: ").strip()
# TODO: Validasi kode tidak boleh duplikat   
    if kode in stok_dict:
        print("Kode sudah digunakan")
        return

    nama = input("Masukkan nama barang: ").strip()
    stok_awal = int(input("Masukkan stok awal: "))

#TODO: Input stok awal (integer)  
    stok_dict[kode] = {
        "nama": nama,
        "stock": stok_awal
    }
    print("Barang berhasil ditambahkan")
#TODO: Simpan ke dictionary

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

#TODO: Cek apakah kode ada di dictionary   
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan")
        return

    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Masukkan pilihan (1/2): ").strip()
# TODO: Input jumlah perubahan stok
    jumlah = int(input("Masukkan jumlah: "))

    stok_sekarang = stok_dict[kode]["stock"]

    if pilihan == "1":
        stok_dict[kode]["stock"] = stok_sekarang + jumlah

    elif pilihan == "2":
        if stok_sekarang - jumlah < 0:
            print("Error: stok tidak boleh kurang dari 0")
            return
        stok_dict[kode]["stock"] = stok_sekarang - jumlah

    else:
        print("Pilihan tidak valid")
        return

    print("\nData berhasil diperbarui dan disimpan")


# -------------------------------
# Program Utama
# -------------------------------
def main():

    stok_barang = baca_stok(NAMA_FILE)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()