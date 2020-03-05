def my_h(liste):
  my_d={}
  for item in liste:
    if item not in my_d:
      my_d[item]=1
    else:
      my_d[item]=item+1
  return my_d
print(my_h([2,3,4,6,2,5,6,6,6,6,6,6,6,2]))

# output:{2: 3, 3: 1, 4: 1, 6: 7, 5: 1}
