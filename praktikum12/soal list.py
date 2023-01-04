# list makanan dengan 2 dimensi
list_makanan = [
    ['bakwan', 'tempe', 'tahu'],                        #index-0
    ['nasi uduk', 'nasi pecel', 'sate padang']          #index-1
]

print(list_makanan [1][1])

# cetak semua makanan yang ada di list makanan
# sampai tidak ada di dalam kotak

for i in list_makanan:
  for detail_makanan in i:
    print (detail_makanan)