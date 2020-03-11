from sympy import FiniteSet
from fractions import Fraction

s = FiniteSet(1, 1.5, Fraction(1, 5), 1, 1.5, 7, 42)
t = FiniteSet(Fraction(1,5), 1, 5, 1, 1, 91, 87) 

for member in s:
    print(member)
#s nin elemanlarını yazdırır.(küçükten büyüğe)
    
if s == t:
    print("True")
else:
    print("False")
#s ve t kümelerinin aynı olup olmadığını kontrol ediyor.
#output: False
    
print(s.union(t)) #s ve t kümelerinin birleşimini çıktı olarak veriyor.
print(s.intersect(t)) #s ve t kümelerinin kesişimini çıktı olarak veriyor.

print(s ** 2)#s kümesinin kartezyen çarpımını "sxs" yi verir.
print(set(s ** 2)) #kartezyen çarpımın elemanlarını tek tek çıktı olarak verir.
