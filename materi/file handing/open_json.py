import json

file_rukun_islam_path=r"C:\Users\dell\Desktop\python\file handing\rukun_islam.json"
with open (file_rukun_islam_path,"r") as file_rukun_islam:
    #gunakan load() dari module json
    data_rukun_islam=json.load(file_rukun_islam)
    print(f"judulnya:{data_rukun_islam["judul"]}")
    print(f"jumlahnya :{data_rukun_islam["jumlah"]}")
    print(f"status kawin{data_rukun_islam["status kawin"]}")
    print(f"sholat sunnah{data_rukun_islam["solat sunnah"]}") 
    print(f"rating buku :{data_rukun_islam["info"]["rating"]}")
    for item in data_rukun_islam["rukun"]:
        print(f"-->{item}")
print(f"surah ke 1{data_rukun_islam["suroh"][0]['nama surah']}")#akses manual
print("-"*50)
print("|nama surah|jumlah ayat| lokasi turun|")
print("-"*50)
#keys :no ,ayat nama turun 
for item_surah in data_rukun_islam["suroh"]:
    print(f'|{item_surah["no"]}|{item_surah["ayat"]}|{item_surah['no']}|{item_surah["turun"]}')