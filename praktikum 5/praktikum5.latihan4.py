#==============================
# nama= Herbert Batubara
# nim= J0403251162
# kelas= Tpl A/2
#==============================
# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")
kombinasi(2)

# #  dua variable penambahan string  yang menghasilkan kominasi dua angka
# yang akan berbeda pada seyiap hasilnya 