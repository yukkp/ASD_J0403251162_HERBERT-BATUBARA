# ==========================================
# Nama: Herbert Batubara
# NIM: J0403251162
# TPL A/2
# ==========================================

graph = {
    "Andi": ["Budi", "Citra"],
    "Budi": ["Deni"],
    "Citra": ["Andi"],
    "Deni": ["Eka"],
    "Eka": ["Budi"]
}

# Tampilkan node
print("Node:")
for i in graph:
    print(i)

# Tampilkan adjacency list
print("\nAdjacency List:")
for i in graph:
    print(i, "->", graph[i])

# Buat adjacency matrix sederhana
nodes = list(graph.keys())
matrix = []

for i in nodes:
    row = []
    for j in nodes:
        if j in graph[i]:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

# Tampilkan adjacency matrix
print("\nAdjacency Matrix:")
for row in matrix:
    print(row)

# Tampilkan hubungan
print("\nHubungan:")
for i in graph:
    for j in graph[i]:
        print(i, "follow", j)
