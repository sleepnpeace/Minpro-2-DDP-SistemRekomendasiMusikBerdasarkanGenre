# Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre

Nama: Rafik Anugrah Yana

Nim: 2609116086

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

Kode ini merupakan function(def) untuk menambah musik, menampilkkan judul menu dengan warna hijau, dan dapat menginput judul, artis, genre untuk menambahkan data ke dalam list, saat ingin menambahkan data musik baru harus ada (judul, artis, dan genrenya) jika salah tidak ada saat proses menambah maka akan tidak bisa ditambah dan muncul pesan data tidak boleh kosong(warna merah), dan dengan append musik baru yang ditambahkan akan ditaruh di bagian terakhir dalam list utama musik, lalu kode untuk menampilkan pesan (Musik berhasil ditambahkan!) dengan sedikit jeda karena time.sleep

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/9.png)

Kode ini merupakan function(def) untuk memilih nomor musik yang tersedia.program meminta pengguna memasukkan nomor musik, kemudian menggunakan try untuk mengubah input menjadi angka. Setelah itu, if mengecek apakah nomor yang dimasukkan sesuai dengan nomor musik yang tersedia. Jika benar, nomor tersebut dikembalikan dengan return nomor. Jika nomor tidak tersedia, program menampilkan pesan kesalahan dan meminta pengguna mencoba lagi. Jika pengguna memasukkan huruf atau bukan angka, except ValueError akan menangani kesalahan tersebut agar program tidak berhenti dan menampilkan pesan "Masukkan angka yang benar."

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/10.png)

Kode ini merupakan function(def) untuk ubah musik, menampilkkan judul menu dengan warna kuning, terdapat conditional statement yaitu, jika belum ada data akan menampilkan pesan "Belum ada data musik.", tetapi jika ada (minimal 1) akan menampilkan list musik dengan judul[0], artis[1], genre[2], terdapat perulangan (for i) dan penomoran otomatis yang dimulai dari 1(enumerate) bukan 0, jika musik berhasil di ubah akan terdapat pesan "musik berhasil diubah" dengan sedikit jeda karena time.sleep, musik harus diubah judul, artis, dan genrenya jika salah satu data kosong akan muncul pesan "Data tidak boleh kosong" dan data gagal diubah 

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

Program mulai dari menu utama dengan 2 pilihan login dan keluar(keluar dari program) kemudian meinput 1-2, jika input 1 akan ke login dan meinput nama lalu input pasword kemudian terdapat decision jika berhasil akan masuk ke menu role masing masing jik username dan password tidak valid akan menampilkan pesan "username dan password salah" dan kembali lagi ke input username hingga login berhasil 

jika input 2 akan keluar dari program dan menampilkan pesan "terima kasih,  dan program selesai

jika input selain angka 1 dan 2 akan muncul pesan "pilihan menu tidak valid".



![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/Flowchart%20menu%20admin.png)

jika login ke menu admin akan terdapat pesan "selamat datang" dan dapat input 1-6

jika input 1 akan masuk ke menu musik dan terdapat decision apakah data musik kosong, jika ya akan menampilkan pesan belum ada data musik, jika tidak akan menampilkan daftar musik dan kembali ke menu utama

jika input 2 akan masuk ke menu tambah musik kemudian, input judul, input artis, input genre untuk menambahkan lagu lalu akan di proses untuk di tambahkan ke list musik, kemudian akan menampilkan pesan "musik berhasil ditambahkan" dan kembali ke menu utama

jika input 3 akan masuk ke menu ubah kemudian terdapat decision apakah data musik kosong jika ya akan menampilkan pesan "belum ada data musik", jika tidak akan menampilkan musik yang ada, lalu ada decision input nomor untuk musik yang ingin diubah jika valid dapat, input judul, artis, dan genre baru dan akan diproses dan ketika sudah berhasil akan menampilkan pesan "musik berhasil diubah" dan kembali ke menu admin, jika nomor yang di input tidak valid akan terus gagal diubah dan kembali ke input nomor sampai benar

jika input 4 akan masuk ke menu hapus musik, ada decision apakah data musik kosong? jika ya menampilkan pesan "belum ada data musik" jika tidak akan menampilkan daftar musik yang ada, lalu ada input nomor yang ingin dihapus jika valid musik terhapus dan kembali ke menu admin, jika tidak akan terus gagal dihapus dan harus input nomor sampai benar agar dapat dihapus

jika input 5 akan masuk ke menu rekomendasi musik berdasarkan genre, terdapat proses untuk menampilkan genre yang ada, lalu input genre, jika genre ada akan menampilkan musik dengan genre tersebut serta artis dan judul musiknya, jika tidak akan menampilkan pesan "maaf genre musik tidak ada" lalu kembali ke menu admin

jika input 6 akan logout dari menu admin dan menampilkan pesan logout berhasil dan kembali ke menu utama


![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/Flowchart%20menu%20user.png)

jika login ke menu user akan terdapat pesan "selamat datang" dan dapat input 1-3

jika input 1 akan masuk ke menu musik dan terdapat decision apakah data musik kosong, jika ya akan menampilkan pesan belum ada data musik, jika tidak akan menampilkan daftar musik dan kembali ke menu user

jika input 2 akan masuk ke menu rekomendasi musik berdasarkan genre, terdapat proses untuk menampilkan genre yang ada, lalu input genre, jika genre ada akan menampilkan musik dengan genre tersebut serta artis dan judul musiknya, jika tidak akan menampilkan pesan "maaf genre musik tidak ada" lalu kembali ke menu user

jika input 3 akan logout dari menu user dan menampilkan pesan logout berhasil dan kembali ke menu utama

3.Penjelasan Output

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%201.png)

Menu awal program terdapat judul dan waktu kapan program dijalankan saat itu juga, dan terdapat 2 pilihan login dan keluar serta input pilihan

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%202.png)

Menu login dan jika berhasil login menggunakan role admin dengan Ray sebagai username dan admin123 passwordnya dan terdapat pesan selamat datang dan 6 pilihan serta input pilihannya

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%203.png)

Menu lihat semua daftar musik dengan cara input angka 1

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%204.png)

Menu tambah musik dengan cara input angka 2 kemudian memasuki input judul,artis, dan genre, lalu hasil di daftar musik nya ketika sudah ditambah

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%205.png)

Menu ubah musik dengan cara input 3 kemudian ubah judul, artis, dan genrenya, lalu hasil di daftar musik nya ketika sudah diubah 

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%206.png)

Menu hapus musik dengan cara input 4 kemudian input nomor musik yang mau dihapus,  lalu hasil di daftar musik nya ketika sudah dihapus

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%207.png)

Menu rekomendasi genre musik, ketika input genre, dan hasil musiknya berdasarkan genre

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%208.png)

Fungsi dari library random nya yaitu musik yang di cari berdasarkan genrenya akan acak hasil susunannya

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%209.png)

Ketika logout dari menu admin

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2010.png)

Ketika login dan masuk ke menu user menggunakan username "user" dan password "user123" dan terdapat pilihan 1-3 dan input nya

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2011.png)

Menu lihat semua musik dengan cara input angka 1 dan terhubung dengan list yang ada dan yang dari ditambahi, diubah, atau dihapus oleh admin

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2012.png)

Menu rekomendasi genre musik dengan cara input 2 dan input genre nya

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2013.png)

Ketika user logout dan kembali ke menu utama

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/input%20menu%20utama%20tidak%20valid.png)

Ketika input menu utama tidak valid

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/input%20username%20dan%20password%20tidak%20valid.png)

Ketika username dan password tidak valid

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/input%20menu%20admin%20tidak%20valid.png)

Ketika input pilihan di menu admin tidak valid

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/ubah%20musik%20admin%20tidak%20valid.png)

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/tambah%20musik%20tidak%20valid.png)
Ketika tambah musik tidak valid

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/input%20angka%20ubah%20musik%20tidak%20valid.png)

Ketika input angka genre di menu admin tidak valid

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/input%20menu%20user%20tidak%20valid.png)

Ketika input menu admin tidak valid karena data kosong

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/ubah%20musik%20tidak%20valid.png)

Ketik ubah genre di menu user tidak valid

![alt text](https://github.com/sleepnpeace/Minpro-2-DDP-SistemRekomendasiMusikBerdasarkanGenre/blob/main/image/output%2014.png)

Ketika input 2 di menu utama dan program selesai dengan pesan terima kasih
