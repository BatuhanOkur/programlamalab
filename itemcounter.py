#itemcounter fonksiyonu girilen listenin elemanlarından kaç tane olduğunu bir küme çıktısı olarak döndürür.
def itemcounter(liste):
  my_d={}
  for item in liste:
    if item not in my_d:
      my_d[item]=1
    else:
      my_d[item]=item+1
  return my_d
print(itemcounter([2,3,4,6,2,5,6,6,6,6,6,6,6,2]))

# output:{2: 3, 3: 1, 4: 1, 6: 7, 5: 1}
