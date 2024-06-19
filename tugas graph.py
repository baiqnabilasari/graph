def semua_path(graph, mulai, akhir, path=[]):
    path = path + [mulai]
    if mulai == akhir:
        return [path]
    if mulai not in graph:
        return []
    paths = []
    for node in graph[mulai]:
        if node not in path:
            new_paths = semua_path(graph, node, akhir, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def jalur_terpendek(graph, mulai, akhir, path=[]):
    path = path + [mulai]
    if mulai == akhir:
        return path
    if mulai not in graph:
        return None
    terpendek = None
    for node in graph[mulai]:
        if node not in path:
            jalur_baru = jalur_terpendek(graph, node, akhir, path)
            if jalur_baru:
                if not terpendek or len(jalur_baru) < len(terpendek):
                    terpendek = jalur_baru
    return terpendek

def temukan_semua_jalur_terpendek(semua_jalur, jalur_terpendek):
    list_jalur_terpendek = []
    for jalur in semua_jalur:
        if len(jalur) == len(jalur_terpendek):
            list_jalur_terpendek.append(jalur)
    return list_jalur_terpendek

def tampilkan_blok(jalur):
    for i, j in enumerate(jalur, start=1):
        print(f'Jalur {i} = {j}')

def temukan_semua_garis(graph):
    list_garis = []
    for kunci in graph.keys():
        for nilai in graph[kunci]:
            list_garis.append(f'{kunci} => {nilai}')
    return list_garis

graf_sembarang = {
    'A': ['C', 'D'],
    'B': ['C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['C', 'E'],
    'E': ['C', 'B'],
    'F': []
}

# Temukan semua jalur dari 'A' ke 'E'
daftar_semua_jalur = semua_path(graf_sembarang, 'A', 'E')
print('\nSemua Jalur:')
tampilkan_blok(daftar_semua_jalur)
print("==============================")
print("|by : Nama : Baiq Nabila Sari|")
print("==============================")

