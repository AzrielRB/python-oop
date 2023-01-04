# membuat class dengan kata kunci "class"

class mahasiswa:
    #atribut
    #constructor
    def __init__(self, nim, nama, rombel) :
        self.nim = nim
        self.nama = nama
        self.rombel = rombel
    #method
    def lulus (self, nilai):
        if (nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")
# class mahasiswa memiliki 3 atribut dan 1 fungsi

    def cetak(self):
        print("nama :", self.nama)
        print("nim :", self.nim)
        print("rombel :", self.rombel)

# membuat objek
mahasiswa1 = mahasiswa("0110222130", "Azriel Rakhan Bilal", "TI 05")
# print(help(mahasiswa1))

# mencetak atribut
mahasiswa1.cetak()
mahasiswa1.lulus(95)

# objek ke 2
mahasiswa2 = mahasiswa("0110120", "Joko", "TI05")

# mencetak atribut2
mahasiswa2.cetak()
mahasiswa2.lulus(95)