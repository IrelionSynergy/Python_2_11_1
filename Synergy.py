def factorial(i):
   number = int(i)
   if number == 1: return 1
   return  factorial(number - 1) * number

numbers = []
number = int(input('Введите число = '))

for i in range(number, 0, -1):
   numbers.append(factorial(i))
print(numbers)