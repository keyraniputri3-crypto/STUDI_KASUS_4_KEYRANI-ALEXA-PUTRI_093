# PROGRAM DATA BUKU

buku = {
    "judul": "Melangkah",
    "penulis": "J. S. Khairen",
    "tahun_terbit": 2020
}

# Menu
while True:
    print("MENU DATA BUKU")
    print("1. Tampilkan Data")
    print("2. Tambah Penerbit")
    print("3. Ubah Penulis")
    print("4. Hapus Penerbit")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        for key, value in buku.items():
            print(key, ":", value)

    elif pilihan == "2":
        buku["penerbit"] = input("Masukkan nama penerbit: ")
        print("Penerbit berhasil ditambahkan.")

    elif pilihan == "3":
        buku["penulis"] = input("Masukkan nama penulis baru: ")
        print("Penulis berhasil diubah.")

    elif pilihan == "4":
        if "penerbit" in buku:
            del buku["penerbit"]
            print("Penerbit berhasil dihapus.")
        else:
            print("Data penerbit tidak ada.")

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")

print("DATA BUKU SETELAH PERUBAHAN:")

for key, value in buku.items():
    print(key, ":", value)