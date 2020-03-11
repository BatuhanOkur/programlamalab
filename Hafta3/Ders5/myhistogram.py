# Hash içindeki listenin i indisi varsa değerini 1 arttırır,yoksa o andaki key'e 1 ataması yapar.

def my_histogram(inlist = [5, 0, 25, 100, 0, 0, 5, 100, 5]):    
    my_dct = {}
    for i in inlist:
        if i in my_dct:
            my_dct[i] += 1
        else:
            my_dct[i] = 1
    return my_dct
