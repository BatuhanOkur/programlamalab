def my_linear_search(mylist,item_search): #girilen değerin listede kaçıncı indiste olduğunu döndürür.
    found=(-1,-1) #başlangıç değeridir girilen değer listede yoksa (-1,-1) döner.
    n=len(mylist)
    for indis in range(n):
        if mylist[indis]==item_search:
            found=(mylist[indis],indis)
            #break --Eğer ki ilk bulduğu indisi döndürmek istiyorsak break'i uncommentlememiz gerek.
    return found

def my_mean(mylist): # listenin ortalamasını alır
    s,t=0,0
    for item in mylist:
        s=s+1
        t=t+item
    mean=t/s
    return mean

def bubble_sort(mylist): # listeyi küçükten büyüğe sıralar.
    n=len(mylist)
    print(mylist)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(mylist[j]<mylist[j+1]):
                temp=mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=temp
    return mylist

def bineary_search(mylist,item_search): #sıralanmış bir listeyi ikiye bölerek aranmak istenen itemi arar.
    found=(-1,-1)
    low=0
    high=len(mylist)-1
    
    while low <= high:
        mid=(low+high)//2
        if mylist[mid]==item_search:
            return mylist[mid],mid
        elif mylist[mid]> item_search:
            high=mid-1
        else:
            low=mid+1
    return found

def median(mylist): #bir listenin medyanını bulur.
    my_list_2=bubble_sort(my_list)
    print("Listenin sıralanmış hali:",my_list_2)
    n=len(my_list_2)
    if n%2==1:
        middle=int(n/2)+1
        median=my_list_2[middle]
        #print(median)
    else:
        middle_1=my_list_2[int(n/2)]
        middle_2=my_list_2[int(n/2)+1]
        median=(middle_1+middle_2)/2
        #print(median)
    return median
    
    



mylist=[5, 3, 3, 5, 0, 0, 0, 2, 2, 0]
print(my_linear_search(mylist,0))
#çıktı : (0,9)
#eğer break comment durumunda olmasaydı çıktı (0,4) olurdu.
print(my_mean(mylist)) 
print(bubble_sort(mylist))
print(bineary_search(bubble_sort(mylist),0))
        

size=int(input("Listenin boyutunu giriniz:"))
my_list=get_n_random_numbers(size)
print("Listem:",my_list)
print(median(my_list))
