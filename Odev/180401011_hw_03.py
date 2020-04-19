"""
Ad Soyad:Batuhan Okur
Numara : 180401011
"""
import sympy as sym
from sympy import Symbol,pprint
import matplotlib.pyplot as plt

e=Symbol('e')
lam=Symbol('lambda')
x=Symbol('x')
my_f_part_0=e**(-lam*x)
#print(my_f_part_0)
pprint(my_f_part_0)

my_f=lam*my_f_part_0
#print(my_f)
pprint(my_f)

sym.plot(my_f.subs({lam:0.5,e:3}), (x,-5,5),title='exponential distribution plot for lambda=0.5')

x_values=[]
y_values=[]
for value in range(-5,5):
    y=my_f.subs({lam:0.5,e:3,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)

plt.plot(x_values,y_values)

"""
Exponential Distribution(Üstel Dağılım):
  Sabit ortalama değişme haddinde ortaya çıkan bağımsız olaylar arasındaki 
zaman aralığını tanımlayan olasılık dağılımıdır.



Üzerinde çalıştığım formul :       -λ⋅x  
                               λ. e    
    
Sabit değişkenler: λ=0.5 ve e=3
Bağımsız değişkenler: x(-5 ile 5 arası)

"""


      
