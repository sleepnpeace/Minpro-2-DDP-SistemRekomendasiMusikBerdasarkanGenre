# Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre

Nama: Rafik Anugrah Yana
Nim: 086
Kelas: C 2026

1.Penjelasan Kode

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/1.png)

Kode ini berfungsi untuk memasukan library dalam file python ini dan library nya itu time(untuk waktu jeda proses), random(untuk acak rekomendasi lagu berdasarkan genre), pwinput(agar password jadi bintang saat di ketik), dan datetime(untuk melihat tanggal wakttu program dijalankan saat itu).

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/2.png)

Kode ini berfungsi untuk mendefinisikan warna yang diambil dari kode ANSI yang akan digunakan untuk setiap judul menu

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/3.png)

Kode ini berfungsi untuk mendefinisikan role menggunakan dictionary yaitu admin(ray) dan user(user)

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/4.png)

kode ini berfungsi untuk menyimpan data musik menggunakan list dan didalam nya terdapat judul musik, artis, dan genre 

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/5.png)

Kode Ini merupakan function(def) untuk menu utama, while True agar menu terus ditampilkan sampai pengguna memilih keluar. Program menampilkan judul sistem(dengan warna ungu), waktu program dijalankan saat itu juga, serta dua pilihan yaitu Login dan Keluar. Jika pengguna memilih 1, program menjalankan fungsi login() untuk memeriksa akun dan mendapatkan role pengguna. Jika role yang diperoleh adalah admin, pengguna diarahkan ke menu_admin(), sedangkan jika role adalah user, pengguna diarahkan ke menu_user(). Jika pengguna memilih 2, program menampilkan pesan bahwa program dihentikan, dan ada jeda menggunakan time.sleep(), kemudian menggunakan break untuk menghentikan perulangan dan mengakhiri program. Jika pengguna memasukkan pilihan selain 1 atau 2, program menampilkan pesan bahwa pilihan tidak valid dan kembali menampilkan menu utama 

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/6.png)

Kode ini merupakan function(def) untuk login, dan berfungsi untuk melakukan login menggunakan username dan password(yang jika diketik menampilkan bintang karena menggunakan library pwinput), terdapat perulangan while true sampai benar benar bisa login ke menu admin atau user. jika berhasil muncul pesan berhasil dan masuk ke menu role masing masing dengan jeda(karena menggunakan time.sleep) dan jika username dan password tidak valid akan menampilkan pesan "Username atau password salah" dan program akan terus mengulang sampai kita berhasil login

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/7.png)

Kode ini merupakan function(def) untuk menampilkan musik yang ada, menampilkkan judul menu dengan warna biru, muncul output "Belum ada data musik." jika data belum ada, dan jika ada (minimal 1) akan menampilkan list musik dengan judul[0], artis[1], genre[2], terdapat perulangan (for i) dan penomoran otomatis yang dimulai dari 1(enumerate) bukan 0

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/8.png)

Kode ini merupakan function(def) untuk menambah musik, menampilkkan judul menu dengan warna hijau, dan dapat menginput judul, artis, genre untuk menambahkan data ke dalam list, dan dengan append musik baru yang ditambahkan akan ditaruh di bagian terakhir dalam list utama musik, lalu kode untuk menampilkan pesan (Musik berhasil ditambahkan!) dengan sedikit jeda karena time.sleep

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/9.png)

Kode ini merupakan function(def) untuk memilih nomor musik yang tersedia.program meminta pengguna memasukkan nomor musik, kemudian menggunakan try untuk mengubah input menjadi angka. Setelah itu, if mengecek apakah nomor yang dimasukkan sesuai dengan nomor musik yang tersedia. Jika benar, nomor tersebut dikembalikan dengan return nomor. Jika nomor tidak tersedia, program menampilkan pesan kesalahan dan meminta pengguna mencoba lagi. Jika pengguna memasukkan huruf atau bukan angka, except ValueError akan menangani kesalahan tersebut agar program tidak berhenti dan menampilkan pesan "Masukkan angka yang benar."

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/10.png)

Kode ini merupakan function(def) untuk ubah musik, menampilkkan judul menu dengan warna kuning, terdapat conditional statement yaitu, jika belum ada data akan menampilkan pesan "Belum ada data musik.", tetapi jika ada (minimal 1) akan menampilkan list musik dengan judul[0], artis[1], genre[2], terdapat perulangan (for i) dan penomoran otomatis yang dimulai dari 1(enumerate) bukan 0, jika musik berhasil di ubah akan terdapat pesan "musik berhasil diubah" dengan sedikit jeda karena time.sleep

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/11.png)

Kode ini merupakan function(def) untuk hapus musik. menmpilkan judul bewarna merah, kemudian if len(musik) == 0 mengecek apakah daftar musik kosong. Jika kosong, program menampilkan pesan bahwa belum ada data musik dan menggunakan return untuk menghentikan fungsi. Jika masih ada musik, program menampilkan daftar musik dengan tampilkan_musik(), lalu meminta pengguna memilih nomor musik melalui pilih_nomor(). Setelah nomor dipilih, musik.pop(nomor - 1) digunakan untuk menghapus musik dari daftar. Musik yang dihapus disimpan dalam variabel lagu

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/12.png)

Kode ini merupakan function(def) untuk rekomendasi berdasarkan genre. menampilkan judul warna biru, kemudian if len(musik) == 0 mengecek apakah daftar musik kosong. Jika kosong, program menampilkan pesan "Belum ada data musik." lalu return untuk menghentikan fungsi. Jika ada data musik, daftar_genre digunakan untuk mengambil semua genre yang tersedia, menghilangkan genre yang sama dengan set(), kemudian mengurutkannya dengan sorted(). Setelah itu, for genre in daftar_genre menampilkan semua genre yang tersedia. Program kemudian meminta pengguna memasukkan genre yang disukai menggunakan input(). Selanjutnya, rekomendasi_musik mencari musik yang memiliki genre yang sama dengan pilihan pengguna. Penggunaan .lower() membuat huruf besar dan kecil tidak menjadi masalah, misalnya "Rock" dan "rock" tetap dianggap sama. Jika musik dengan genre tersebut ditemukan, random.shuffle() dari (library random) tadi mengacak urutan rekomendasi, lalu program menampilkan judul dan penyanyi musik tersebut. Jika tidak ditemukan, bagian else menampilkan pesan "Maaf, genre musik tidak ada dengan pesan sedikit ada jeda karena time.sleep

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/13.png)

Kode ini merupakan function(def) untuk menu admin, dan berfungsi untuk menampilkan dan memilih pilihan 1-6 dimenu admin, jika memilih 1-5 akan masuk ke menu masing masing dan jika memilih 6 akan log out menggunakan break dan terdapat pesan "logout berhasil" dan program akan kembali ke menu utama yang di awal, jika pilihan tidak valid akan muncul pesan "pilihan menu tidak valid"

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/14.png)

Kode ini merupakan function(def) untuk menu user, dan berfungsi untuk menampilkan dan memilih pilihan 1-3 dimenu user, jika memilih 1-2 akan masuk ke menu lihat dan rekomendasi dan jika memilih 3 akan log out  menggunakan break dan terdapat pesan "logout berhasil" dan program akan kembali ke menu utama yang di awal, jika pilihan tidak valid akan muncul pesan "pilihan menu tidak valid"

2.Penjelasan Alur Flowchart

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/Flowchart%20menu%20menu%20utama.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/Flowchart%20menu%20admin.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/Flowchart%20menu%20user.png)

3.Penjelasan Output

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%201.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%202.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%203.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%204.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%205.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%206.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%207.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%208.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%209.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2010.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2011.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2012.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2013.png)
![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2014.png)
