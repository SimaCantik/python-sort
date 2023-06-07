def bubble_sort_descending(daftar_angka):
    n = len(daftar_angka)
    
    for i in range(n - 1):
        # Lakukan perulangan dalam
        for j in range(n - 1 - i):
            # Bandingkan pasangan angka
            if daftar_angka[j] < daftar_angka[j + 1]:
                # Tukar angka jika diperlukan
                daftar_angka[j], daftar_angka[j + 1] = daftar_angka[j + 1], daftar_angka[j]
    
    return daftar_angka

# Inisialisasi daftar angka
daftar_angka = [42, 19, 33, 8, 55]

# Panggil fungsi bubble_sort_descending
daftar_angka_terurut = bubble_sort_descending(daftar_angka)

# Cetak daftar angka terurut
print(daftar_angka_terurut)
