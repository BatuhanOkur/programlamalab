my_d={2:3,3:1,4:1,6:7,5:1}

def lookup(d,v):
  print(d,v)
  for key in d:
    if d[key]==v:
      return key
  else:
    return -1
print(lookup(my_d,3))
#output: 2
