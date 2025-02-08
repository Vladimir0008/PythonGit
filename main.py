import random


while True :
    length = random.randint(3,7)
    result = str(chr(random.randint(1040, 1104)))
    for i in range(1, length) :
        result += str(chr(random.randint(1040, 1104)))
    print(result)