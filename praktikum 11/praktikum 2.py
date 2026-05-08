# ==========================================
# Nama: Herbert Batubara
# NIM: J0403251162
# TPL A/2
# ==========================================

# Graph:
# A --- B
# |     |
# C --- D

# Dictionary digunakan untuk menyimpan adjacency list
# Key = node
# Value = list tetangga (node yang terhubung)
graph = {
    "A": ["B", "C"],  # A terhubung ke B dan C
    "B": ["A", "D"],  # B terhubung ke A dan D
    "C": ["A", "D"],  # C terhubung ke A dan D
    "D": ["B", "C"]   # D terhubung ke B dan C
}

# Menampilkan adjacency list
print("Adjacency List:")
for node, tetangga in graph.items():
    # node = simpul saat ini
    # tetangga = daftar simpul yang terhubung
    print(node, "->", tetangga)

# Penjelasan:
# A -> ['B', 'C'] artinya A terhubung ke B dan C
# B -> ['A', 'D'] artinya B terhubung ke A dan D