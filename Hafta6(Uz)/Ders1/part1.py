from sympy import Symbol
from sympy import factor,expand
from sympy import pprint
#Symbol bir değişkeni sembole dönüştürür ve sembolik modelleme yapmamıza olanak sağlar.
x=1
print(x+x+1) #output: 3


x = Symbol('x')
print(x+x+1)#output: 2*x+1

a = Symbol('x')
print(a+a+1)#output: 2*x+1

p = x * (x + x)
print(p) #output: 2*x**2

p = (x + 2)*(x + 3)
print (p) #output: (x + 2)*(x + 3)

x = Symbol('x')
y = Symbol('y')
expr = x**2 - y**2
print(factor(expr)) #output:(x - y)*(x + y)
#factor metodu bir ifadeyi çarpanlarına ayırır.
factors = factor(expr)
expand = expand(factors)
print(expand) #output: x**2 - y**2
#expand metodu çarpanlara ayrılmış bir ifadeyi eski haline getirir.

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3 #(x+y)**3 nin açılımı
print(factor(expr)) #output: (x + y)**3
pprint(factor(expr)) #output: (x+y)^^3
#pprint metodu üstel ifadeleri kod öbeğinden matematiksel gösterime dönüştürür.

x = Symbol('x')
series = x
n = 5
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)#output aşağıdaki gibidir.

# 5    4    3    2    
#x    x    x    x     
#── + ── + ── + ── + x
#5    4    3    2    
 
expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1 , y:2})
print(res)#output : 9
#subs metodu sembolleri atanan değerler ile değiştirir.

r = expr.subs({x:1-y}) #x'i y'ye bağlı olarak değiştirdik.
print(r) #output: y**2 + 2*y*(1 - y) + (1 - y)**2

x = Symbol('x')
series = x
n = 5
x_value = 10
for i in range(2,n+1):
    series = series + (x**i)/i
pprint(series)
series_value = series.subs({x:x_value})
print("Serinin değeri:",series_value) #output aşağıdaki gibidir.

# 5    4    3    2    
#x    x    x    x     
#── + ── + ── + ── + x
#5    4    3    2     
#Serinin değeri: 68680/3
