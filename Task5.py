# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Enter a number: '))
fibosub = [1,-1]
fibon = [1,1]
for i in range(2,n):
    list = fibon[i-1]+fibon[i-2]
    fibon.append(list)
    sub = fibosub[i-2] - fibosub[i-1]
    fibosub.append(sub)
fibosub.reverse()
fibosub.append(0)
print(f'Fibonacci for negative and positive indices for n = {n} is {fibosub+fibon}')