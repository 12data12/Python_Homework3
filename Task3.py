#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


import random
numbers = [round(random.uniform(-99.999, 100), 2) for x in range(int(input('How many numbers are in your list? ')))]
print(f'Your list: {numbers}')

new_numbers = [round (i-int(i), 2) for i in numbers]
new_numbers = list(map(abs,new_numbers))
print(f'Fractional parts of the list numbers: {new_numbers}')
print(f'Max frac is {max(new_numbers)}')
print(f'Min frac is {min(new_numbers)}')
print(f'Difference between max and min fracs = {round(max(new_numbers)-min(new_numbers),2)}')