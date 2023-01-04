#membuat list dengan []
buah = ["mangga", "melon", "jeruk", "apel"]

#
print (buah[0])

# menambah list menggunakan append

buah.append("pisang")
print (buah)

#mengubah list
#variabel index keberapa = nilai baru
buah[0] = "jambu"
print (buah)

#menghapus list
#del, buah  [index yang mau dihapus]
del buah[1]
print(buah)

#mengambil data akhir menggunakan pop
print(buah.pop())

#mengetahui jumlah data dari list
#menggunakan len()
print(len(buah))

#menyisipkan data sesuai yang diinginkan
#menggunakan inser(index, value)
buah.insert(1, "duku")
print(buah)

#mengambil seluruh data di list
#menggunakan perulangan for
for i in buah:
    #apa yang dieksekusi
    print (i)