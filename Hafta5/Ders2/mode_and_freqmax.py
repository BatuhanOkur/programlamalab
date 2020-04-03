# get_n_random_numbers,my_frequency_with_dict ve my_frequency_with_list_of_tuples "Ders1" dosyasında mevcuttur burada tanımlanmış kabul edilmiştir.

my_list = get_n_random_numbers(10)
my_freq_dict = my_frequency_with_dict(my_list)
my_freq_list = my_frequency_with_list_of_tuples(my_list)

def my_mode_in_dict(my_hist_d): #Bir kümedeki modu ve kaç kere tekrar ettiğini döndürür.
    freq_max=-1
    mode=-1
    for key in my_freq_dict:
        print(key,my_hist_d[key])
        if my_hist_d[key]>freq_max:
            freq_max=my_hist_d[key]
            mode=key
    return mode,freq_max

def my_mode_in_list(my_hist_l): #Bir listedeki modu ve kaç kere tekrar ettiğini döndürür.
    freq_max=-1
    mode=-1
    for item,frequency in my_hist_l:
        print(item,frequency)
        if frequency>freq_max:
            freq_max=frequency
            mode=item
    return mode,freq_max

result_1=my_mode_in_dict(my_freq_dict)
result_2=my_mode_in_list(my_freq_list)
print(result_1,result_2)
