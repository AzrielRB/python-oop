# membuat tuple menggunakan tupe buka tutup kurung ("value", ...)
gorengan = ('bakwan', 'combro', 'misro')
sop = ('sop iga', 'sop buntut', 'sop kaki')
nasi = ('nasi uduk', 'nasi goreng', 'nasi rames')
# tuple di dalam tuple
makanan = (gorengan, sop, nasi)
# index     0       1       2

# cetak gorengan dari variable makanan dikeluarkan dari buka tutup kurung
#for i in makanan[0]:
#    print(i)

#cetak sop buntut
#print(makanan[1][1])

# cetak nasi remas
#print(makanan[2][2])

# cetak seluruhnya dan pastikan keluarkan dari buka tutup kurungnya
for i in makanan:
  for makanan in i:
    print (makanan)