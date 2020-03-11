def fibo_rec(n):
    if n < 2:
        return n
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

#Bu kod doğru çalışır ve klasik recursive fib kodudur.Aşağıdaki ise known kütüphanesi kullanılarak yapılmış versiyonudur.

known = {0:0, 1:1}
def fibo_rec(n): 
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1) + fibo_rec(n-2)
        known[n] = result
        return result
