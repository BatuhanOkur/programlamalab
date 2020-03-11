def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b > 1:
        if b % 2 == 0:
            return power(a * a, b / 2)
        return power(a * a, b / 2) * a

            # return power (a, b-1)*a
            # return power(a*a, b/2)


print(power(2, 5))
