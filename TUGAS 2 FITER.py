class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        # Metode untuk menampilkan informasi Nama, NIM, dan nama Jurusan mahasiswa
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        # Metode untuk menambahkan objek Mahasiswa ke dalam DaftarMahasiswa
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        # Metode untuk menampilkan daftar mahasiswa yang terdaftar dalam Jurusan
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
        for mahasiswa in self.DaftarMahasiswa:
            print("-" * 30)
            mahasiswa.tampilkan_info()


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        # Metode untuk menambahkan objek Jurusan ke dalam DaftarJurusan
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        # Metode untuk menampilkan daftar jurusan yang ada di Universitas
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)
        for jurusan in self.DaftarJurusan:
            print("-" * 30)
            print("Nama Jurusan:", jurusan.NamaJurusan)


# Langkah 2: Membuat objek Universitas "XYZ University"
xyz_university = Universitas("XYZ University")

# Langkah 3: Membuat objek Jurusan "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
teknik_informatika = Jurusan("Teknik Informatika")
xyz_university.tambah_jurusan(teknik_informatika)

# Langkah 4: Membuat objek Mahasiswa "Kalian masing" dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa1 = Mahasiswa("Fiter Ramadansyah", "G1A022053", teknik_informatika)
teknik_informatika.tambah_mahasiswa(mahasiswa1)

# Langkah 5: Menampilkan daftar jurusan di Universitas XYZ
xyz_university.tampilkan_daftar_jurusan()

# Langkah 6: Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
teknik_informatika.tampilkan_daftar_mahasiswa()