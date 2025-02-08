# def add(x, y):
#     return x+y
#
# print(add('aaaa','bbb'))
# def func():
#     pass
#
# print(func())

# def func1(a,b,c = 5):
#     c = 6
#     return a+b+c
#
# print(func1(a=4, b=10, c=5))

# def func2(*args):
#     return list(args)
#
# print(func2(4,5,7,8,8))

# def func3(**kwargs):
#     return kwargs
# print(func3(a=1, b=2, c=3))

# func4 = lambda x, y: x + y
#
# print(func4(2, 4))

# func5 = lambda *a: a
# b = (1)
# print(b)

# 613 Напишіть функцію для визначення найбільшого з трьох цілих чисел з використанянм вбудованої функції max().

# def maxVal(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
#
# print(maxVal(4,5,3))

# 633 Напишіть функцію, яка може генерувати та друкувати кортеж зі значеннями квадратів чисел від 1 до n включно.

# def func(n):
#     l=[]
#     for i in range(1,n+1):
#         l.append(i**2)
#     return tuple(l)
#
# print(func(5))

# 634 Python має вбудовану функцію __doc__ для друку документації для всіх вбудованих функцій.
# Наприклад, для доступу до документації функції abs(), слід використати такий запис: print(input.__doc__).
# Напишіть функцію для обчислення квадрата цілого числа. В тілі функції додайте багаторядковий коментар про те, що робить функція.
# Викличте функцію і перегляньте її документацію.
# print(input.__doc__)
# def powOfNum(n):
#     '''some text'''
#     print(n**2)
#     print(powOfNum.__doc__)
#
# powOfNum(5)


# 636 Напишіть програму, і створіть в ній дві функції. Перша з них - приймає послідовність цілих чисел і повертає список.
# Друга - повертає новий список, що містить всі елементи першого списку без дублікатів.

# def func1(*nums):
#     return list(nums)
#
#
# def func2(l):
#     return set(l)
#
# print(func2(func1(1,2,3,4,5,5)))

# 659 Написати функцію для перевірки правильності введеної дати. Функція приймає 3 аргументи - день,
# місяць та рік і повертає True, якщо така дата є в календарі, і False в протилежному випадку.
# from datetime import date
#
#
# def func(dd, mm, yy):
#     today = date.today()
#
#     if mm <= 12 and mm > 0:
#         if mm in (1,3,5,7,8,10,12) and dd <= 31 and dd > 0:
#             return True
#         elif mm in (4,6,9,11) and dd <= 30 and dd > 0:
#             return True
#         elif mm == 2 and dd <= 28 and dd > 0:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# print(func(1,2,2025))

# 660 Напишіть функцію для перевірки, чи є число ідеальним чи ні. Примітка.
# У теорії чисел ідеальне число - це додатне ціле число, яке дорівнює сумі власних додатних дільників,
# тобто сумі додатних дільників, виключаючи саме число. Відповідно, ідеальне число - це число,
# що дорівнює половині суми всіх додатних дільників (включаючи саме число). Наприклад: перше ідеальне число - 6,
# оскільки 1, 2 і 3 - це правильні додатні дільники, а 1 + 2 + 3 = 6. Відповідно, число 6 дорівнює половині суми всіх
# його додатних дільників: (1 + 2 + 3 + 6) / 2 = 6. Наступне ідеальне число - 28 = 1 + 2 + 4 + 7 + 14.
# Далі ідуть ідеальні числа 496 і 8128.

# def isIdeal(n):
#     dividers = []
#     for i in range(1, int(n/2)+1):
#         if n % i == 0:
#             dividers.append(i)
#     return sum(dividers) == n
#
# for i in range(497):
#     print(f"number {i} is ideal = {isIdeal(i)}")

#663 Напишіть функцію, яка перевіряє, чи рядок є паліндром чи ні. Регістр літер, пропуски і знаки пунктуації не враховувати.
# Примітка. Паліндром - це слово, фраза або послідовність, яка читається так само як зліва направо, так і справа наліво.

# def isPollindrome(s) :
#     alphabet = list('abcdefghijklmnopqrstuvwxyz')
#     l =[]
#     for i in s:
#         if i.lower() in alphabet:
#             l.append(i.lower())
#     lReverse = l
#     lReverse.reverse()
#     return l == lReverse
#
# print(isPollindrome("A man, a plan, a canal, Panama!"))

#664 Напишіть функцію для сортування рядка в алфавітному порядку без врахування регістру літер.

def stringSort(s):
    l = sorted(s, key=str.lower)
    res = "".join(l)
    return res
print(stringSort("JavaScript"))

