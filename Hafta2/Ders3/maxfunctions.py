def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))
