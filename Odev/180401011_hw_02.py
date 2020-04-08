# -*- coding: utf-8 -*-

import csv,sys
from datetime import datetime

arg1 = sys.argv[1]
path = arg1 + "\\input_hw_2.csv"
arg2 = sys.argv[2]
receiver = arg2 + "\\180401011_hw_02_output.txt"

with open(path, 'r', encoding="utf-8") as csv_dosya:
    csv_okuyucu = csv.reader(csv_dosya, delimiter=';')
    main_data = [word for word in [row for row in csv_okuyucu]]
    ayrilis_tarihleri = [main_data[index][3] for index in range(len(main_data))]
    for index in range(len(ayrilis_tarihleri)):
        ayrilis_tarihleri[index] = datetime.strptime(
            ayrilis_tarihleri[index], "%Y-%m-%d %H:%M:%S.%f")
    aylar = [ayrilis_tarihleri[index].month for index in range(len(ayrilis_tarihleri))]
    
    
def Histogram(liste):
    aylar_dic=dict()
    for index in range(len(liste)):
        if liste[index] in aylar_dic:
            aylar_dic[liste[index]] += 1
        else:
            aylar_dic[liste[index]] = 1
    for item in range(1,13): 
        if not (item in aylar_dic):
            aylar_dic[item] = 0
    return aylar_dic

def mean(liste):
    toplam = 0
    eleman_sayisi = len(liste)
    for index in liste:
        toplam  += index
        # eleman_sayisi += 1 // eleman sayısı öğrenilmek istenirse uncommentlenip returnlenebilir.
    ortalama = toplam  / eleman_sayisi
    return ortalama

def getMedian(liste):
    new_liste = sorted(liste)
    n = len(new_liste)
    if n % 2 == 1:
        middle = int(n/2)+1
        median = new_liste[middle - 1]
    else:
        middle_1 = int(n/2) - 1
        middle_2 = middle_1 + 1
        median = (new_liste[middle_1] + new_liste[middle_2]) / 2
    return median

aylar_dict = Histogram(aylar)
value_list = [*aylar_dict.values()]
median = getMedian(value_list)
mean = int(mean(value_list))
output_list = ["Medyan", str(median), "Ortalama", str(mean)]

with open(receiver, "w", encoding="utf-8") as dosya:
    for i in range(0,len(output_list),2):
        dosya.write(output_list[i] + " " + output_list[i+1] + "\n")
