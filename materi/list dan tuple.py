#materi 6 struktur data
#list->[]->berrurutan,berubah duplikat
    #append()untuk menambah item diakhir list
     #remove()menghapus item berdasarkan velue /namanya
    #insert()menambah item ke spesifik index
daftar_belanjaan=[
    "olive chiken",
    "gorengan",
    "es teh desa",
      ]
print("daftar belanjaan:",daftar_belanjaan)
daftar_belanjaan.append("tahu golek")
print("daftar belanjaan:",daftar_belanjaan)
daftar_belanjaan.remove("olive chiken")
print("daftar belanjaan:",daftar_belanjaan)
daftar_belanjaan.insert(0,"gabin")
print("daftar belanjaan:",daftar_belanjaan)
print(daftar_belanjaan[2])# memanggil salah satu index yg terdapat di list
print("potong list:",daftar_belanjaan[1:3])#hanya memanggil yg kita pilih hingga yg terakhir yg kita tentukan

#menggabungkan list dengan +
jajanan_pagi=["nasi uduk","nasi kuning"]
jajanan_sore=["es teh desa","tahu golek"]
gabungan=jajanan_pagi + jajanan_sore# print nya sesuai urutan gabungannyA
print("gabungan:",gabungan)


#tuple->()->berurutan,berubah,tidak duplikat
ttl=("bekasi",23,"juni",2010)
print("tempat tanggal lahir:",ttl)
print("tanggal",ttl[1])

#unpacking tuple ke variabel baru 
#harus berurutan 
tempat_lahir,tanggal_lahir,buln_lahir,tahun_lahir=ttl
print("tempat lahir:",tempat_lahir)
 
game=("df","ml","coc")
game_fps,game_moba,game_setrategi=game
print('gema kesukaan:',game_fps)
#list multi dimensi
daftar_minuman=[
    ["esdoger","eskopi"],
    ["kopianget","teh anget"]
]
print(daftar_minuman[1][0])
#len untuk menghitung  jumlah list dari hitungan satu bukan 0
print(len(ttl))
#pop untuk menghapus yng di akhir list
daftar_belanjaan.pop()
print(daftar_belanjaan)
#extend menggabungkan list dengan list
daftar_belanjaan.extend(daftar_minuman[0][1])
print(daftar_minuman[0][1])