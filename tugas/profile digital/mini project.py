nama=input("nama kamu :")
umur = int(input("umur kamu :"))
kelas=input("kelas :")
hobi= input("hobi:")
cita_cita=input("cita cita :")
waktu_belajar=input("belajar paling enak pas :")
tahun= 2025 - umur
print("=====> tipe digital <=====")
print("1.wibu")
print("2.kpopers")
print("3.gamer")
print("4.anak nongki")
print("5.anak konten")
pilihan=input("pilih yg mana(hanya namanya saja ):")
if(pilihan=="wibu"):
    anime=input("siapa waifu kesukaanmu :")
if(pilihan=="kpopers"):
    kpop=input("siapa bias kesukaan mu:")
if(pilihan=="gamer"):
    game=input("game kesukaan:")
if(pilihan=="anak nongki"):
    nong=input("nongkrong enak nya dimana :")
if(pilihan=="anak konten"):
    ngonten=input("platform apa yng kamu pake untk ngonten:")
print("=======>profil digital<=======")
print(f"Nama : {nama}")
print(f"umur : {umur}")
print(f"kelas: {kelas}")
print(f"hobi: {hobi}")
print(f"cita cita : {cita_cita}")
print(f"belajar yang paling enak pas: {waktu_belajar}")
print(f"tahun lahir :{tahun}")
print("=====> tipe digital <=====")
print(f"tipe : {pilihan}")
if(pilihan=="wibu"):
    print("komentar : wah kamu pasti kamu sering nonton anime sambil makan bawang ya !!! ")
if(pilihan=="kpopers"):
    print("komentar: wah kamu pasti sering dengerin lagu korea ya ")
if(pilihan=="gamer"):
    print("komentar: wah kamu pasti jago main",game,"sambil belajar ya ")
if(pilihan=="anak nongki"):
    print("wah kamu sering ngumpul sama teman kamu ya ")
if(pilihan=="anak konten"):
    print("wah kamu sering ngevlog ya ")
print("======>fun check<======")
bauBadan=input("teman sebelah kamu bau nggak?(y/n)")
if(bauBadan== "y"):
   print("wah darurat .....kasih parfum kelas dunia dong")
if(bauBadan=="n"):
   print("nah ini baru temen yg baik")