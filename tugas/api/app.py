import requests
kota =input("masukin nama kota:")
tanggal=input("tanggal :")
print("---------------------------------")
print (f"kota:{kota}")

 #buat target url ke api al adhan
url =f"https://api.aladhan.com/v1/timingsByCity/{tanggal}?city={kota}&country=Indonesia&method=5"
response= requests.get(url) #htpp get (ambil data)
data_json= response.json(); #ambil data sebagai format json
print(data_json)
print("--------------jadwal sholat----------------")
print(f"waktu maghrib ={data_json["data"]["timings"]["Maghrib"]}")

jadwal_sholat=data_json["data"]["timings"]
print(f"->shubuh ={jadwal_sholat["Maghrib"]}")
