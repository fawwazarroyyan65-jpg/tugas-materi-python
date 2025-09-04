def bangung():
    return 'Alhamdulillahilladzi ahyana bada ma amatana wailaihin nusyur.'

def tidur():
    return 'Bismika allahumma ahyaa wa bismika amuut.'

def makan():
    return'Bismillah'



def itung(uang_list):
     return list(map(lambda x: x + 5000, uang_list))
     
def boros(uang_list):
    return list(filter(lambda x: x >= 50000, uang_list))



def urutan (nilai_lagi_list):
    return list(sorted(nilai_lagi_list, reverse=True))
def terbesar(nilaibesar):
    return max(nilaibesar)
def terkecil (kecil):
    return min(kecil)



def emoji (mood):
    moodi={"senang": "😀","biasa": "😐","sedih": "😢","semangat": "💪"}
    return list(map(lambda mod :moodi,mood))