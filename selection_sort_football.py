#Mengurutkandaftar pemain yang diurutkan berdasarkan jumlah gol yang di cetak secara descending menggunkan selection sort

def selection_sort_players(players):
    n = len(players)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if players[j]["Jumlah Gol"] > players[max_index]["Jumlah Gol"]:
                max_index = j
        players[i], players[max_index] = players[max_index], players[i]

# Daftar pemain yang perlu diurutkan
players = [
    {"Nama Pemain": "Kylian Mbappe", "Klub": "Paris Saint Germain", "Jumlah Gol": 40},
    {"Nama Pemain": "Victor Osimhen", "Klub": "Napoli", "Jumlah Gol": 28},
    {"Nama Pemain": "Robert Lewandowski", "Klub": "Bayern Munich", "Jumlah Gol": 33},
    {"Nama Pemain": "Erling Haaland", "Klub": "Borussia Dortmund", "Jumlah Gol": 52},
    {"Nama Pemain": "Christopher Nkunku", "Klub": "RB Leipzig", "Jumlah Gol": 22},
]

# Memanggil fungsi selection_sort_players untuk mengurutkan daftar pemain
selection_sort_players(players)

# Menampilkan daftar pemain setelah diurutkan
print("Daftar pemain setelah diurutkan berdasarkan jumlah gol:")
print("No.  Nama Pemain            Klub                   Jumlah Gol")
print("-" * 60)
for i, player in enumerate(players, start=1):
    print(f"{i:2}.   {player['Nama Pemain']:<20} {player['Klub']:<22} {player['Jumlah Gol']:>10}")

#Outputnya menampilkan daftar pemain dengan urutan gol terbanyak
