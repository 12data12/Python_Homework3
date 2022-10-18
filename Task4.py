# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input('Enter a number to convert to binary: '))
s = ''
while n != 0:
    s = str(n%2) + s
    n //=2
print(f'Your converted number is {s}')