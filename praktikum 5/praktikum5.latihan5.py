#==============================
# nama= Herbert Batubara
# nim= J0403251162
# kelas= Tpl A/2
#==============================
# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)
buat_pin(3)

# #sama  dalam memproses kombinasi 3 angka dan jika hasil dan panjang sebanding
# dia akan mengambil angka setiap 1 dan menambahkan dua angka lain nya terlebih ada len yang membuat dia mengambil angka pertama 
