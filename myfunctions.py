def my_f_1(inList=[4, -3, 5, -2, -1, 2, 6, -2]):
    maxSum = 0
    n = len(inList)
    for i in range(n):
        for j in range(i, n):
            t = 0
            for k in range(i, j):
                t = t + inList[k]
                if(t > maxSum):
                    maxSum = t
    return maxSum

def my_f_2(inList=[4, -3, 5, -2, -1, 2, 6, -2]):
    maxSum = 0
    n = len(inList)
    for i in range(n):
        t = 0
        for j in range(i, n):
            t = t + inList[j]
            if (t > maxSum):
                maxSum = t
    return maxSum
    
    def my_f_3(inList=[4, -3, 5, -2, -1, 2, 6, -2]): 
    n = len(inList)
    if (n == 1):
        return inList[0]
    left_i = 0
    left_j = n//2

    right_i = n//2
    right_j = n

    left_sum = my_f_3(inList[left_i:left_j])
    right_sum = my_f_3(inList[right_i:right_j])

    temp_left_sum = 0
    t = 0

    for i in range(left_j-1, left_i-1, -1):
        t = t + inList[i]
        if(t > temp_left_sum):
            temp_left_sum = t

    t = 0
    temp_right_sum = 0

    for i in range (right_i, right_j) :
        t = t + inList[i]
        if(t > temp_right_sum):
            temp_right_sum = t

    center_sum = temp_left_sum + temp_right_sum

    return max_of_three(left_sum, right_sum, center_sum)
