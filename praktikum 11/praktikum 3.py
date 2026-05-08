# ==========================================
# Nama: Herbert Batubara
# NIM: J0403251162
# TPL A/2
# ==========================================

# Adjacency matrix
# 0 = tidak terhubung
# 1 = terhubung
matrix = [
    [0,1,1,0],  # A
    [1,0,1,0],  # B
    [1,1,0,1],  # C
    [0,0,1,0]   # D
]

# Nama node (sesuai urutan matrix)
nodes = ["A", "B", "C", "D"]

# Dictionary kosong untuk menyimpan hasil adjacency list
graph = {}

# Loop setiap baris (node asal)
for i in range(len(matrix)):
    graph[nodes[i]] = []  # siapkan list kosong

    # Loop setiap kolom (node tujuan)
    for j in range(len(matrix)):
        # Jika bernilai 1 berarti ada hubungan
        if matrix[i][j] == 1:
            # Tambahkan node tujuan ke list
            graph[nodes[i]].append(nodes[j])

# Menampilkan hasil adjacency list
print("Adjacency List hasil konversi:")
for node, tetangga in graph.items():
    print(node, "->", tetangga)

# Penjelasan:
# Baris A [0,1,1,0] -> A terhubung ke B dan C
# Baris B [1,0,1,0] -> B terhubung ke A dan C
# Baris C [1,1,0,1] -> C terhubung ke A, B, dan D
# Baris D [0,0,1,0] -> D terhubung ke C