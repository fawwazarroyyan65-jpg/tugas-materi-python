import csv 
#3.baca semua data dri csv
with open ("keuangan.csv",newline="",encoding="utf-8") as f :
    reader=csv.DictReader(f)
    data=list(reader)
print(data)

print("\n")

#tampilkan semua data
print("------------------ semua data --------------------------")
for row in data :
    print(f"{row['Tanggal']}|{row['Keterangan']}|{row['Kategori']}|{row['Jumlah']}")
print("\n")

# 2.menghitung semua pengeluaran
total=sum(int(row['Jumlah'])for row in data )
print(f"total pengeluaran:Rp.{total}")

#3. hitung perkategori
kategori_total={}
for row in data :
    kategori= row["Kategori"]
    jumlah=int(row["Jumlah"])
    if kategori not in kategori_total:
        kategori_total[kategori]=0
    kategori_total[kategori]+=jumlah

print("-----------------pengeluaran per kategori----------------")
for kategori,jumlah in kategori_total.items():
    print(f"{kategori}:Rp{jumlah}")

print("\n")

terbesar=None
if terbesar is None or jumlah > terbesar["jumlah"]:
    terbesar_={"kategori":kategori,"pengeluaran":jumlah }

print (f"terbesar {terbesar_['kategori']}:Rp{terbesar_['pengeluaran']}")
