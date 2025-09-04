#function def
def halo_dunia():
    print("halo")  #pake def jika lebih dari 1  baris
    print("dunia")
#cara akses function ,sertakan nama dan () nya
halo_dunia()
#funsi dengan parametr
def sapa(nama):
    print(f"salam dari {nama}")

sapa("fulan")

def rumus(d1,d2):
    print(f"alas: {d1}")
    print(f"tinggi:{d2}")
    rumus= 1/2*(d1)
    print(f"hasil {rumus}")
rumus(10,20)
#fungsi anonim dengan 'lambda' jika hanya 1baris
greeting=lambda name: print(f"name {name} with lambda")

greeting("ali")
greeting("fudel")
greeting("fulan")
#map () untuk mentransformasi data
nilai_mentah=[199,10.0,244,199.2]
bulatkan=map(lambda nilai: round(nilai),nilai_mentah)
list_nilai=list(bulatkan)
print(f"nilai ynga sudah di bulatkan:{list_nilai}")
#map([perubahan data],[sumberdata])
nilai =[22.3,44.,590.4]
nilai_dikalikan=map(lambda nilai:nilai*5,nilai)
nilailist=list(nilai_dikalikan)
print(nilailist)

#sorted()mengurutkan data
daftar_minuman=[{"nama":"haris","angka":23},
                {"nama":"adul","angka":87},
                {"nama":"fulan","angka":45},
                ]

print(daftar_minuman)
daftrTerurut=sorted(daftar_minuman,key=lambda siswa:siswa["angka"])
for i in range(0,1):
    print(daftar_minuman)

#sorting list
nama=['hanif',"abdul","fawwaz",'ziad']
daftarurut=sorted(nama)
kebalik=sorted(nama,reverse=True)
print(daftarurut)
print(kebalik)

#filter()menyaring data 
transsaksi=[240000,50000,10000]
transsaksibesar=filter(lambda angka: angka>= 25000,transsaksi)
list=list(transsaksibesar)
print(transsaksi)
print(list)


import materi
doa3=materi.doa_sebelum_makan() 
print(doa3)
