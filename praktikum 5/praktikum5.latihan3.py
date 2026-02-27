#==============================
# nama= Herbert Batubara
# nim= J0403251162
# kelas= Tpl A/2
#==============================
# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0): 
 # Recursive case
    maks_sisa = cari_maks(data, index + 1)
    
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))


# dalam logic ini dia melakukan dua tugas membandingkan pertama ia index dan mencari maks sisa 
# jika  data lebih kecil dari pada  maks akan mengalami perulangan data ,dan mencari lagi dimana maks harus 
# lebih besar dari data dan hasi akhrnya menenmuan angka yang besar