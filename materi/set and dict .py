##set ->{}-> tdk berurutan ,berubah, tidak duplikat
daftar_game={"valorant","dark soul"}
game={"gensin","mlbb","valorant"}
print("game:",daftar_game)
print("game:",game)
#.add()->menambah kan item baru
daftar_game.add("ff")
print("game:",daftar_game)# jika sudah ada dalam set maka tidak bisa muncul
#remove()->menghapus item
game.remove("mlbb")
print("game:",game)
#len()->menghitung item 
print("game ada:",len(game),game)
#.union()->menggabungkan 2 set berbeda
game_berdua=game.union(daftar_game)
print("daftar semua game nya :",len(game_berdua),game_berdua)
#intersection()->mncari item yg kembar
game_yg_sama=game.intersection(daftar_game)
print("game yg sama",game_yg_sama)
#difference()->mencari item yg berbeda
gameYgbeda=game.difference(daftar_game)
print("game yg beda:",gameYgbeda)

##dict->{key:velue}/{kunci:isinya}->berurutan berdasarkan key,berubah ,key tidak bisa di ubah

animeazka= {
    "wind_breker": "sakura",
    "red_zero": "subaru",
    "waifu":{               #ini sperti list multi dimensi
        "red_zero":"rem"
    }
    }
print(animeazka)
print("waifu red zero:",animeazka["waifu"]["red_zero"])
#menammbah atau ubah data dict
animeazka["naruto"]="hidan"
animeazka['red_zero']="gak ada"
print("anme skrg:",animeazka)

#dict dipanggil dgn key
#operator untuk dict
data_dict={
    "cup":"ucup",
    "tong":"otong",
    "dung":"dudung",
}
lendict=len(data_dict)#variabel counstan
print(lendict)
#mengecek data
key ="cup"#harus dgn key nya
keyen=key in data_dict
print(f"apakah data {key}ada di data_dict:",keyen)
#kostum error
print(data_dict.get("fudel","key tidak di temukan"))
#mengapdate data 
data_dict["cup"]="ucup si ganteng"
print(data_dict)

data_dict.update({"cup":"ucup ganteng"})
print(data_dict)
