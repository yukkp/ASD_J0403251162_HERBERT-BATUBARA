#==============================
# nama= Herbert Batubara
# nim= J0403251162
# kelas= Tpl A/2
#==============================
# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================
def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)

    countdown(n - 1)

    print("Keluar:", n)
countdown(3)

# memasukan nilai n yang berupa 3 perta ma menghasilkan output"masuk ;n"
# dan akan mengalami perulangan sampai jika dalam logic n =0 maka ia selesai 