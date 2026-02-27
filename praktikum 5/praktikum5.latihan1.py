#==============================
# nama= Herbert Batubara
# nim= J0403251162
# kelas= Tpl A/2
#==============================
# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
 # Base case
    if n == 0:
        return 1
 # Recursive case
    return a * pangkat(a, n - 1)
print(pangkat(2, 4)) # Output: 16
 
# dimana a sebagai absis atau bilangan awal 2  n sebagai pangkat 4 
# jika n=0 dia akan mengalami perulangan sebanyak 1 kali 
# untuk mengelurkan hasil dia mengulang  dia mengulang  n sampai 1 dengan cara pengurangan