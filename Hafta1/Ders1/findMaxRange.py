#findMaxRange fonksiyonu girilen dizi içindeki maksimum toplamı verir.i_1 ve i_2 ise sınır indislerdir.#
def findMaxRange_i(inlist=[4, -3, 5, -2, -1, 2, 6, -2]):
    max = 0
    for i in range(len(inlist)):
        for j in range(i+1, len(inlist)):
            # print(i, j)
            t = 0
            for k in range(i,j+1):
                t = t + inlist[k]
            if t > max:
                max = t
                i_1, i_2 = i, j
    return max , i_1, i_2
print(findMaxRange_i(inlist=[4, -3, 5, -2, -1, 2, 6, -2])
#output:(11,0,6) 

#Alttaki fonksiyonda  daha az kontrol var#
def findMaxRange_ii(inlist=[4, -3, 5, -2, -1, 2, 6, -2]):  
    max = 0
    for i in range(len(inlist)):
        t = 0
        for j in range(i, len(inlist)):
            t = t + inlist[j]
            if t > max:
                max = t
                i_1, i_2 = i, j
    return max , i_1, i_2
print(findMaxRange_ii(inlist=[4, -3, 5, -2, -1, 2, 6, -2])
#output:(11,0,6)       
