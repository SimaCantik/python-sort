def bubble_sort(daftar_nilai):
    n = len(daftar_nilai)
    
    for i in range(n - 1):
        # Lakukan perulangan dalam
        for j in range(n - 1 - i):
            # Bandingkan pasangan nilai
            if daftar_nilai[j] > daftar_nilai[j + 1]:
                # Tukar nilai jika diperlukan
                daftar_nilai[j], daftar_nilai[j + 1] = daftar_nilai[j + 1], daftar_nilai[j]
    
    return daftar_nilai

# Inisialisasi daftar nilai siswa
daftar_nilai = [78, 65, 90, 82, 70]

# Panggil fungsi bubble_sort
daftar_nilai_terurut = bubble_sort(daftar_nilai)

# Cetak daftar nilai terurut
print(daftar_nilai_terurut)