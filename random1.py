import random
import pymorphy2
import time
import numpy as np

start_time = time.time()

lower_vowels = "аеєиіїоуюя"
upper_vowels = "АЕЄИІЇОУЮЯ"
lower_not_vowels = "бвгджзйклмнпрстфхцчшщ"
upper_not_vowels = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
alphabet = list("аеєиіїоуюябвгджзйклмнпрстфхцчшщ")

morph = pymorphy2.MorphAnalyzer(lang='uk')

file = open("text.txt", "a")

cnt_shlack = 0
cnt_norm = 0
for j in range(30):
    while True:
        length = 4  # random.randint(4,10)
        # result = (str(random.choice(alphabet))).upper()
        result = np.random.choice(alphabet).upper()
        for i in range(1, length):
            result += np.random.choice(alphabet)
            # result += str(random.choice(alphabet))

        parsed = morph.parse(result)
        if any(p.is_known for p in parsed):
            cnt_norm += 1
            end_time = time.time()
            all_time = end_time - start_time

            if result == "Мама":
                file.write(f"{j}. Ура! Маму знайдено! На це нам знадобилось: {all_time}\n")
                file.write(f"Знайдено шлаку: {cnt_shlack}\n")
                file.write(f"Знайдено слів: {cnt_norm}\n")
                break
        else:
            cnt_shlack += 1
file.close()
file = open("text.txt", "r")
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
