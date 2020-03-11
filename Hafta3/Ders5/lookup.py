 #lookup fonksiyonu sözlük içinde value kere tekrar eden ilk sayıyı döndürür.

def lookup(dict, value):
    try:
        for k in dict:
            if dict[k] == value:
                return k
    except:
        print("Değer bulunamadı.")
