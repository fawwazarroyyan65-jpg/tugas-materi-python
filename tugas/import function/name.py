import data_doa

print(data_doa.bangung())
print(data_doa.tidur())
print(data_doa.makan())

jajan = [50000, 30000, 15000, 70000, 10000]
jajanbonus=data_doa.itung(jajan)
jajanboros=data_doa.bors(jajan)
print(f"dapet bonus total nya jadi:{jajanbonus}")
print(f"wah nih boros :{jajanboros}")


list=[75, 90, 60, 88, 100, 55]
urut=data_doa.urutan(list)
besar=data_doa.terbesar(list)
kecil=data_doa.terkecil(list)
print(f"urutan terbesar:{urut}")
print(f"terbesar:{besar}")
print(f"terkecil:{kecil}")


moodis=[data_doa.emoji("senang")]
mood=data_doa.emoji(moodis)
print(f"emojinya:{mood}")