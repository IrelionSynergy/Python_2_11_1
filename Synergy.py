def factorial(i):
   number = int(i)
   if number == 1: return 1
   return  factorial(number - 1) * number

print(factorial(input('Введите число = ')))