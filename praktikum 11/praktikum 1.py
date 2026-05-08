# ==========================================
# Nama: Herbert Batubara
# NIM: J0403251162
# TPL A/2
# ==========================================

# Matriks ketetanggaan (adjacency matrix)
matrix = [
# 0  1  2  3
 [0, 1, 1, 0],  # Baris 0
 [1, 0, 0, 1],  # Baris 1
 [1, 0, 0, 1],  # Baris 2
 [0, 1, 1, 0]   # Baris 3
]

# Tampilkan matrix
print("Adjacency Matrix:")
for row in matrix:
    print(row)

print("\nPenjelasan setiap baris:")

# Penjelasan tiap baris
# Baris 0
print("Baris 0 [0,1,1,0] -> Node 0 terhubung ke node 1 dan 2")

# Baris 1
print("Baris 1 [1,0,0,1] -> Node 1 terhubung ke node 0 dan 3")

# Baris 2
print("Baris 2 [1,0,0,1] -> Node 2 terhubung ke node 0 dan 3")

# Baris 3
print("Baris 3 [0,1,1,0] -> Node 3 terhubung ke node 1 dan 2")