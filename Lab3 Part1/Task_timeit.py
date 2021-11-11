import timeit
import random
import os
randfile = open("Randomnm.txt", "w" )

while os.path.getsize("Randomnm.txt") <= 1048576*50:
    line = str(random.randint(1, 1000)) + "\n"
    randfile.write(line)

randfile.close()

check = """
summa = 0
with open("Randomnm.txt") as file:
    my_lines = file.readlines()
    for line in my_lines:
        if line.strip().isdigit():
            summa += int(line.strip())
"""
print(timeit.timeit(check, number=10))

check = """
summa = 0
with open("Randomnm.txt") as file:
    for line in file:
        if line.strip().isdigit():
            summa += int(line.strip())
"""

print(timeit.timeit(check, number=10))

check = """
with open("Randomnm.txt") as file:
    res = (int(line) for line in file if line.strip().isdigit())
    summa = sum(res)
"""
print(timeit.timeit(check, number=10))
