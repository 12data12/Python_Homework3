# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint

numbers = [randint(-10, 10) for i in range(int(input('How many numbers are in your list? ')))]
print(f'List of random numbers: {numbers}')

def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: results.append(numbers[0]**2)       
    return results

print(f'The product of pairs of numbers (first and last element, second and next-to last element etc.) of list numbers is {pairs_mult(numbers)}')