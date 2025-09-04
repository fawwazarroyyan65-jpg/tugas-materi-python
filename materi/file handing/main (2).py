import csv

#file handling

#cari posisi file note .txt
file_path=r"C:\Users\dell\Desktop\python\file handing\note.txt"
#open()->buka file target
#mode r->read only (hanya baca)
file_catatan=open(file_path,"r")
#read baca file
catatan=file_catatan.read()
print(f"isi catatan{catatan}")
#tutup file .txt
file_catatan.close()


##open csv 
file_anime_path=r"C:\Users\dell\Desktop\python\file handing\anime.csv"
with open (file_anime_path,"r") as file_anime:
    #gunakan reader dari module csv
    anime_reader=csv.reader(file_anime)
    list_anime=list(anime_reader)
    for anime in list_anime:
     print(list_anime)


#add/tambah data csv
#with open(file_anime_path,"a",newline="")as file_anime :
   #gunakan writer ()dari module csv 
   #write=csv.writer(file_anime)
   #fungsi writerow()-.>tambah baris baru
   #write.writerow(anime_baru)
#print(list_anime)

# cara update csv
#open file  ->baca isi
#->extrak data dengan for loop ->olah data (buat/hapus)->



print("--------------open extrak--------------")

anime_file_path= r"C:\Users\dell\Desktop\python\file handing\anime.csv"
data_anime=[]#list kosong
with open (anime_file_path,"r")as file_anime:
   #gunakan fungsi reader( ) dari modul csv
   baca_file_anime=csv.reader(file_anime)
   #ekstrak data dengan for loop ke list
   for item_anime in baca_file_anime:
      #.append()->menambahkan item ke list
      data_anime.append(item_anime)

   print(data_anime)

#ubah data by index
for item in data_anime:
   if item[1]=="wildan":
      print("di temukan ")
      item[2]="demon slayer"

   else:
      print('tidak di temukan')

#hapus data perbaris index
del data_anime[2]

print("------------mode 'w'""------------------------")

#mode 'w' (write)->ubah seluruh baris csv
with open (anime_file_path,"w")as file_anime:
   #gunakan writer()dari modul csv 
   write_aniem=csv.writer(file_anime)
   #funsi writerow()->tidak sama dgn writerows() 
   #writerow -> satu baris 
   #writerows->seluruh baris
   write_aniem.writerows(data_anime)
