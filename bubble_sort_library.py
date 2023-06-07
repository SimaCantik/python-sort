# Mengurutkan daftar buku berdasarka halaman secara ascending menggunakan bubble sort

def bubble_sort_books(books):
    n = len(books)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if books[j]["Jumlah Halaman"] > books[j + 1]["Jumlah Halaman"]:
                books[j], books[j + 1] = books[j + 1], books[j]

# Daftar buku yang perlu diurutkan
books = [
    {"Judul Buku": "Harry Potter and the Sorcerer's Stone", "Penulis": "J.K. Rowling", "Jumlah Halaman": 230},
    {"Judul Buku": "To Kill a Mockingbird", "Penulis": "Harper Lee", "Jumlah Halaman": 281},
    {"Judul Buku": "The Great Gatsby", "Penulis": "F. Scott Fitzgerald", "Jumlah Halaman": 180},
    {"Judul Buku": "Pride and Prejudice", "Penulis": "Jane Austen", "Jumlah Halaman": 432},
    {"Judul Buku": "1984", "Penulis": "George Orwell", "Jumlah Halaman": 328}
]

# Memanggil fungsi bubble_sort_books untuk mengurutkan daftar buku
bubble_sort_books(books)

# Menampilkan daftar buku setelah diurutkan
print("Daftar buku setelah diurutkan:")
print("No.  Judul Buku                              Penulis               Jumlah Halaman")
print("-" * 85)
for i, book in enumerate(books, start=1):
    print(f"{i:2}.   {book['Judul Buku'][:40]:<40} {book['Penulis']:<20} {book['Jumlah Halaman']:>13}")

#Outputnya tampilan daftar no, judul buku, penulis dan jumlah halaman yang berurutan 
