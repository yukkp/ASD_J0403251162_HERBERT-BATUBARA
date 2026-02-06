# ===============================================================
# Praktikum 2 : Konsep ADT dan file Handling (STUDI KASUS)
# Latihan Dasar 1 : Membuat Fungsi Load Data
# ===============================================================


nama_file="data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict={}
    with open(nama_file,"r")as file:
        for baris in file:
            baris= baris.strip()
            nim,nama,nilai = baris.split(",")
            data_dict[nim]={"nama":nama,"nilai":int (nilai)}
    return data_dict

buka_data = baca_data(nama_file)
# print('Jumlah Data Terbaca',len(buka_data))


# ===============================================================
# Praktikum 2 : Konsep ADT dan file Handling (STUDI KASUS)
# Latihan Dasar 2 : Membuat Fungsi header Tabel
# ===============================================================

def tampilkan_data(data_dict):
    #membuat header tabel
    print("\n====DAFTAR MAHASISWA====")
    print(f"{'NIM':<10} | {'NAMA':<12} | {"Nilai":>5}")
    print("-"*35)

    for nim in sorted(data_dict.keys()): 
        nama= data_dict[nim]["nama"]
        nilai= data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")
    
# tampilkan_data(buka_data)

# ===============================================================
# Praktikum 2 : Konsep ADT dan file Handling (STUDI KASUS)
# Latihan Dasar 3 : Membuat Fungsi mencari data
# ===============================================================

def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai mana key dictionary
    # membuat input nim mahasiswa yang ingin dicari
    nim_cari=input("masukan nim mahasiswa yang ingin dicari:").strip()

    if nim_cari in data_dict:
        nama= data_dict[nim_cari]['nama']
        nilai=data_dict[nim_cari]['nilai']

        print('=====Data Mahasiswa Ditemukan=====')
        print(f"NIM  :{nim_cari}")
        print(f"Nama :{nama}")
        print(f"Nilai:{nilai}")
    else:
        print("Data tidak Di temukan")

#memanggil fungsi cari data
# cari_data(buka_data)

# ===============================================================
# Praktikum 2 : Konsep ADT dan file Handling (STUDI KASUS)
# Latihan Dasar 4: Membuat Fungsi Update data
# ===============================================================

def ubah_data(data_dict):

    #awali duku dengan mencari nim/data mahasiswa  yang ingin di tentukan 
    nim= input("masukan nim mahasiswa yang pengen di ubah:").strip()
    if nim not in data_dict:
        print('Nim tidak di temukan.Update dibatalkan')
        return
    
    try:
        nilai_baru=int(input('masukan nilai baru 0-100:').strip())
    except ValueError:
        print('Nilai Harus berupa angka.Update di batalkan')
        return
    
    if nilai_baru<0 or nilai_baru>100:
        print('nilai harus antar 0-100.Update diBatalkan')
    
    nilai_lama=data_dict[nim]['nilai']
    data_dict[nim]['nilai']=nilai_baru

    print(f'Update berhasil.Nilai{nim}berubah dari {nilai_lama}menjadi{nilai_baru}')

#memangil fungsi ubah data
# ubah_data(buka_data)

# ===============================================================
# Praktikum 2 : Konsep ADT dan file Handling (STUDI KASUS)
# Latihan Dasar 5: Membuat Fungsi Simpan Data
# ===============================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file,"r")as file:
        for nim in sorted(data_dict.keys()):
            nama= data_dict[nim]['nama']
            nilai= data_dict[nim]['nilai']
            file.write(f'{nim},{nama},{nilai}\n')

#memangil fungsi simpan data
# simpan_data(nama_file,buka_data)
print('\nData Berhasil Disimpan ke file: ', nama_file)

# ===============================================================
# Praktikum 2 : Konsep ADT dan file Handling (STUDI KASUS)
# Latihan Dasar 6: Membuat Menu Interaktif
# ===============================================================

def main():
    #load data otomatis program saat program di mulai 
    buku_data=baca_data(nama_file)

    while True:
        print('\n====MENU DATA MAHASISWA====')
        print('1.tampilkan Data Mahasiswa ')
        print('2.Cari data berdasarkan NIM')
        print('3. ubah nilai Mahasiswa')
        print('4.simpan Data ke Dalam File')
        print('0.keluar')

        pilihan= input('Pilihan menu:').strip()

        if pilihan=='1':
            tampilkan_data(buka_data)
        elif pilihan=='2':
            cari_data(buka_data)
        elif pilihan=='3':
            ubah_data(buka_data)
        elif pilihan=='4':
            simpan_data(buka_data)
        elif pilihan=='0':
            print('program selesai')
            break
        else:
            print('pilihan tidak valid')
main()