import random

random.randint(1,100)  # 1 ile 100 arasında rastgele sayı üretir.(1 ve 100 dahil)

def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers
get_n_random_numbers()
#Bu fonksiyon min_ ve max_ değer arasında n tane rastgele sayı üretir.    

get_n_random_numbers(22,-56,64) # -56 ile 64 arasında 22 tane rastgele sayı üretir.

my_list=get_n_random_numbers(15,-4,4)

def my_frequency_with_dict(list): # Hangi elemanın kaç kere listede geçtiğini bir küme olarak döndürür.
    freq_dict={}
    for item in list:
        if (item in freq_dict):
            freq_dict[item]=freq_dict[item]+1
        else:
            freq_dict[item]=1
    return freq_dict
my_frequency_with_dict(my_list)


def my_frequency_with_list_of_tuples(list_1): # Hangi elemanın kaç kere listede geçtiğini bir liste olarak döndürür.
    freq_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(freq_list)):
            if(list_1[i]==freq_list[j][0]):
                freq_list[j][1]=freq_list[j][1]+1
                s=True
        if(s==False):
            freq_list.append(list_1[i],1)
    return freq_list

my_list=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4,4]
result_1=my_frequency_with_dict(my_list)
result_2=my_frequency_with_list_of_tuples(my_list)
