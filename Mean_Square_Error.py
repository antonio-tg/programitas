def mse(array_a, array_b):
    sum = 0
    for i in range(len(array_a)):
        sum += (array_a[i] - array_b[i])**2
    return sum/len(array_a)

print(mse([10, 20, 10, 2], [10, 25, 5, -2]))
