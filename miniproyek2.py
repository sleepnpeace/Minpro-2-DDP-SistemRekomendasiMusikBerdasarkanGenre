import time
import random
import pwinput
from datetime import datetime

MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
UNGU = "\033[95m"
RESET = "\033[0m"

users = {
    "Ray": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

musik = [
    ["Tabun", "Yoasobi", "Jpop"],
    ["Luna", "Wisp", "Shoegaze"],
    ["Supernatural", "Newjeans", "Kpop"],
    ["California Love", "2Pac", "Hip Hop"],
    ["desire", "bixby", "Indie"],
    ["Helena", "My Chemical Romance", "Rock"]
]

def menu_utama():
    while True:
        print(UNGU + "SISTEM REKOMENDASI MUSIK" + RESET)
        print("Waktu program:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        print()
        print("1. Login")
        print("2. Keluar")

        pilihan = input("Silakan pilih (1-2): ")

        if pilihan == "1":
            role = login()

            if role == "admin":
                menu_admin()

            elif role == "user":
                menu_user()

        elif pilihan == "2":
            print(HIJAU + "\nProgram dihentikan." + RESET)
            time.sleep(1)
            print("Terima kasih, dan sampai jumpa lagi!")
            break

        else:
            print(MERAH + "Pilihan menu tidak valid. Silakan pilih 1-2." + RESET)
            time.sleep(1)

def login():
    print(UNGU + "\nLOGIN SISTEM MUSIK" + RESET)

    while True:
        username = input("Username: ")
        password = pwinput.pwinput("Password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(HIJAU + "\nLogin berhasil!" + RESET)
            time.sleep(1)
            print("Selamat datang,", username)
            print("Role:", role)
            time.sleep(2)
            return role
        else:
            print(MERAH + "Username atau password salah." + RESET)
            print("Silakan coba lagi.\n")
            time.sleep(1)

def tampilkan_musik():
    print(BIRU + "\nDAFTAR MUSIK" + RESET)

    if len(musik) == 0:
        print("Belum ada data musik.")
    else:
        for i, lagu in enumerate(musik, 1):
            print(f"{i}. {lagu[0]} - {lagu[1]} ({lagu[2]})")

def tambah_musik():
    print(HIJAU + "\nTAMBAH MUSIK" + RESET)

    judul = input("Judul musik: ").strip()
    penyanyi = input("Nama penyanyi: ").strip()
    genre = input("Genre: ").strip()

    if judul == "" or penyanyi == "" or genre == "":
        print(MERAH + "Data tidak boleh kosong." + RESET)
        return

    musik.append([judul, penyanyi, genre])
    print(HIJAU + "Musik berhasil ditambahkan!" + RESET)
    time.sleep(1)

def pilih_nomor():
    while True:
        try:
            nomor = int(input("Pilih nomor musik: "))

            if 1 <= nomor <= len(musik):
                return nomor
            else:
                print(MERAH + "Nomor musik tidak tersedia." + RESET)

        except ValueError:
            print(MERAH + "Masukkan angka yang benar." + RESET)

def ubah_musik():
    print(KUNING + "\nUBAH MUSIK" + RESET)

    if len(musik) == 0:
        print("Belum ada data musik.")
        return

    tampilkan_musik()
    nomor = pilih_nomor()

    judul = input("Judul baru: ").strip()
    penyanyi = input("Penyanyi baru: ").strip()
    genre = input("Genre baru: ").strip()

    if judul == "" or penyanyi == "" or genre == "":
        print(MERAH + "Data tidak boleh kosong." + RESET)
        return

    musik[nomor - 1] = [judul, penyanyi, genre]

    print(HIJAU + "Musik berhasil diubah!" + RESET)
    time.sleep(1)

def hapus_musik():
    print(MERAH + "\nHAPUS MUSIK" + RESET)

    if len(musik) == 0:
        print("Belum ada data musik.")
        return

    tampilkan_musik()
    nomor = pilih_nomor()

    lagu = musik.pop(nomor - 1)

    print(HIJAU + f"Musik '{lagu[0]}' berhasil dihapus!" + RESET)
    time.sleep(1)

def rekomendasi():
    print(BIRU + "\nREKOMENDASI MUSIK" + RESET)

    if len(musik) == 0:
        print("Belum ada data musik.")
        return

    daftar_genre = sorted(list(set(lagu[2] for lagu in musik)))

    print("Genre yang tersedia:")

    for genre in daftar_genre:
        print(f"- {genre}")

    genre_pilihan = input("\nMasukkan genre yang disukai: ").strip()

    rekomendasi_musik = [
        lagu for lagu in musik
        if lagu[2].lower() == genre_pilihan.lower()
    ]

    if rekomendasi_musik:
        random.shuffle(rekomendasi_musik)

        print(f"\nRekomendasi musik genre {genre_pilihan}:")

        for lagu in rekomendasi_musik:
            print(f"- {lagu[0]} - {lagu[1]}")
    else:
        print(MERAH + "\nMaaf, genre musik tidak ada." + RESET)

    time.sleep(1)

def menu_admin():
    while True:
        print(UNGU + "\nMENU ADMIN" + RESET)
        print("1. Lihat semua musik")
        print("2. Tambah musik")
        print("3. Ubah musik")
        print("4. Hapus musik")
        print("5. Rekomendasi berdasarkan genre")
        print("6. Logout")

        pilihan = input("Silakan pilih (1-6): ")
        
        if pilihan == "1":
            tampilkan_musik()
        elif pilihan == "2":
            tambah_musik()
        elif pilihan == "3":
            ubah_musik()
        elif pilihan == "4":
            hapus_musik()
        elif pilihan == "5":
            rekomendasi()
        elif pilihan == "6":
            print(HIJAU + "\nLogout berhasil." + RESET)
            time.sleep(1)
            break
        else:
            print(MERAH + "Pilihan menu tidak valid. Silakan pilih 1-6." + RESET)
            time.sleep(1)

def menu_user():
    while True:
        print(UNGU + "\nSISTEM REKOMENDASI MUSIK" + RESET)
        print("1. Lihat semua musik")
        print("2. Rekomendasi berdasarkan genre")
        print("3. Logout")

        pilihan = input("Silakan pilih (1-3): ")

        if pilihan == "1":
            tampilkan_musik()
        elif pilihan == "2":
            rekomendasi()
        elif pilihan == "3":
            print(HIJAU + "\nLogout berhasil." + RESET)
            time.sleep(1)
            break
        else:
            print(MERAH + "Pilihan menu tidak valid. Silakan pilih 1-3." + RESET)
            time.sleep(1)

menu_utama()