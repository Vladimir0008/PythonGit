# import random
# file = open('Lesson1.txt', 'w')
# for i in range(1,100):
#     n = random.randint(100, 1000)
#     s = str(n) + '\n'
#     file.write(s)
# file.close()

# file = open('Lesson1.txt', 'r')
#
# for line in file:
#     print(line, end="")

# def func():
#     even_nums = open('even_numbers', 'w')
#     odd_nums = open('odd_numbers', 'w')
#
#     n = int(input("Input count of numbers: "))
#
#     for i in range(1, n + 1):
#         a = int(input("Input num: "))
#         if (a % 2 == 0):
#             s = str(a)
#             even_nums.write(s + '\n')
#         else:
#             s = str(a)
#             odd_nums.write(s + '\n')
#     even_nums.close()
#     odd_nums.close()
#
# func()


# def readFile(fileName) :
#     numbers = open(fileName, 'r')
#     if numbers.read(1) == '':
#         print('File is empty')
#         numbers.close()
#         return
#
#     l = []
#     for line in numbers:
#         s = line.split()
#         l.extend(map(int, s))
#     numbers.close()
#     return l
# def func():
#     l = readFile('numbers.txt')
#     if len(l) == 0:
#         return
#
#     large_even = open('large_even.txt', 'w')
#     small_odd = open('small_odd.txt', 'w')
#     other_numbers = open('other_numbers.txt', 'w')
#
#     l.sort()
#     for i in l:
#         if i % 2 == 0 and i > 50:
#             s = str(i)
#             large_even.write(s + '\n')
#         elif i % 2 != 0 and i < 20:
#             s = str(i)
#             small_odd.write(s + '\n')
#         else:
#             s = str(i)
#             other_numbers.write(s + '\n')
#     large_even.close()
#     small_odd.close()
#     other_numbers.close()
#
# func()


# 1

# def func():
#     n = int(input("Input count of numbers: "))
#
#     for i in range(1, n + 1):
#         a = int(input("Input number: "))
#         if a % 5 == 0 and a % 3 == 0:
#             file = open('multiplies_of_3_and_5.txt', 'a', encoding='UTF-8')
#             s = str(a)
#             file.write(s + '\n')
#             file.close()
#         elif a % 5 == 0:
#             file = open('multiplies_of_5.txt', 'a', encoding='UTF-8')
#             s = str(a)
#             file.write(s + '\n')
#             file.close()
#         elif a % 3 == 0:
#             file = open('multiplies_of_3.txt', 'a', encoding='UTF-8')
#             s = str(a)
#             file.write(s + '\n')
#             file.close()
#         else:
#             file = open('other_numbers.txt', 'a', encoding='UTF-8')
#             s = str(a)
#             file.write(s + '\n')
#             file.close()
# func()
# 2
# import re
# def func() :
#     file = open('text1.txt', 'r')
#     l = []
#     for line in file:
#         words = re.split(r"\W+", line)
#         l.extend(filter(None, words))
#
#     cntWords = 0
#     mostCommonWord = ''
#     setWords = set(l)
#     for word in setWords:
#         cnt = 0
#         for w in l:
#             if word == w:
#                 cnt += 1
#         if cnt > cntWords:
#             cntWords = cnt
#             mostCommonWord = str(word)
#         file = open('unique_words.txt', 'a')
#         file.write(word + ' ')
#         file.close()
#     print(mostCommonWord)
# func()

#3
def func():
    totalGrade = 0
    totalStudents = 0
    studentGrades = {}

    file = open('results.txt', 'r', encoding='utf-8')
    for line in file:
        l = line.split()
        studentGrades[l[0]] = int(l[1])
        totalGrade += int(l[1])
        totalStudents += 1
    file.close()

    avgGrade = round(totalGrade/totalStudents, 2)
    print(studentGrades)
    print(f"Average grade is {avgGrade}")
    print("Students with higher then average grade:", end=" ")
    for k, v in studentGrades.items():
        if v > avgGrade:
            print(k, end=", ")
        elif v < 50:
            file = open('failed_students.txt', 'a', encoding='utf-8')
            file.write(f"{k} {v}\n")
            file.close()

func()
