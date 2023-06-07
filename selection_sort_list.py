def selection_sort(daftar_angka):
    n = len(daftar_angka)
    
    for i in range(n - 1):
        # Temukan indeks angka terkecil dalam sisa daftar angka
        indeks_terkecil = i
        for j in range(i + 1, n):
            if daftar_angka[j] < daftar_angka[indeks_terkecil]:
                indeks_terkecil = j
        
        # Tukar angka terkecil dengan angka pada indeks i
        if indeks_terkecil != i:
            daftar_angka[i], daftar_angka[indeks_terkecil] = daftar_angka[indeks_terkecil], daftar_angka[i]
    
    return daftar_angka

# Inisialisasi daftar angka
daftar_angka = [9, 5, 3, 8, 2]

# Panggil fungsi selection_sort
daftar_angka_terurut = selection_sort(daftar_angka)

# Cetak daftar angka terurut
print(daftar_angka_terurut)
