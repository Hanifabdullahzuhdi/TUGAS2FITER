# TUGAS2FITER
Kelas Mahasiswa:

Atribut:

Nama: Menyimpan nama mahasiswa dalam bentuk string.
NIM: Menyimpan NIM (Nomor Induk Mahasiswa) dalam bentuk string.
Jurusan: Menyimpan objek Jurusan yang menjadi jurusan mahasiswa.
Metode:

__init__(self, nama, nim, jurusan): Metode inisialisasi yang digunakan untuk mengatur nilai awal atribut Nama, NIM, dan Jurusan saat objek Mahasiswa dibuat.
tampilkan_info(self): Metode untuk menampilkan informasi Nama, NIM, dan nama Jurusan mahasiswa.
Kelas Jurusan:

Atribut:

NamaJurusan: Menyimpan nama jurusan dalam bentuk string.
DaftarMahasiswa: Menyimpan daftar objek Mahasiswa yang terdaftar di jurusan.
Metode:

__init__(self, nama_jurusan): Metode inisialisasi yang digunakan untuk mengatur nilai awal atribut NamaJurusan dan DaftarMahasiswa saat objek Jurusan dibuat.
tambah_mahasiswa(self, mahasiswa): Metode untuk menambahkan objek Mahasiswa ke dalam DaftarMahasiswa.
tampilkan_daftar_mahasiswa(self): Metode untuk menampilkan daftar mahasiswa yang terdaftar dalam Jurusan.
Kelas Universitas:

Atribut:

NamaUniversitas: Menyimpan nama universitas dalam bentuk string.
DaftarJurusan: Menyimpan daftar objek Jurusan yang ada di universitas.
Metode:

__init__(self, nama_universitas): Metode inisialisasi yang digunakan untuk mengatur nilai awal atribut NamaUniversitas dan DaftarJurusan saat objek Universitas dibuat.
tambah_jurusan(self, jurusan): Metode untuk menambahkan objek Jurusan ke dalam DaftarJurusan.
tampilkan_daftar_jurusan(self): Metode untuk menampilkan daftar jurusan yang ada di Universitas.
Untuk menggunakan kelas-kelas tersebut, langkah-langkah yang diikuti adalah:

Membuat objek Universitas dengan menggunakan kelas Universitas dan memberikan nama universitas pada saat inisialisasi.
Membuat objek Jurusan dengan menggunakan kelas Jurusan dan memberikan nama jurusan pada saat inisialisasi. Kemudian, objek Jurusan tersebut ditambahkan ke objek Universitas dengan menggunakan metode tambah_jurusan.
Membuat objek Mahasiswa dengan menggunakan kelas Mahasiswa dan memberikan nama, NIM, serta objek Jurusan yang sesuai pada saat inisialisasi. Selanjutnya, objek Mahasiswa tersebut ditambahkan ke objek Jurusan dengan menggunakan metode tambah_mahasiswa.
Menampilkan daftar jurusan di Universitas dengan menggunakan metode tampilkan_daftar_jurusan pada objek Universitas.
Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan dengan menggunakan metode tampilkan_daftar_mahasiswa pada objek Jurusan.
Pada contoh implementasi di atas, objek Universitas bernama "XYZ University" telah dibuat, kemudian objek Jurusan dengan nama "Teknik Informatika" juga telah ditambahkan ke dalam objek Universitas tersebut. Terakhir, objek Mahasiswa dengan nama "Hanif Abdullah Zuhdi", NIM "G1A022041", dan terdaftar di Jurusan Teknik Informatika di Universitas XYZ juga telah dibuat.

Kemudian, hasilnya ditampilkan dengan menggunakan metode tampilkan_daftar_jurusan pada objek Universitas untuk menampilkan daftar jurusan yang ada di Universitas XYZ, dan metode tampilkan_daftar_mahasiswa pada objek Jurusan untuk menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ.
