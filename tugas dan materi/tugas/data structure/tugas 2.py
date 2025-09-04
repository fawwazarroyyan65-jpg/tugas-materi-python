piket_harian=["harun","ishaq","dika"]

print ("piket hari ini")
for i in piket_harian:
    print("-",i)

rukun_islam=("syahadat","sholat","zakat","puasa","haji")

print("rukun islam")
for d in range(len(rukun_islam)):
    print(f"{d+1}.{rukun_islam [d]}")

kitab={"kitab tjwid","kitab tauhid","kitab fiqh"}
print("kitab kitab:")
for b in kitab:
    print('-',b)

biodata={'nama':"harun",
         "kelas":"10",
         'hafalan':"10"
         }
print("biodata")
num=1

for key,value in biodata.items():
    print(key,value)
