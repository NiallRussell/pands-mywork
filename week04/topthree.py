import random

how_many = 10
top_how_many = 3
range_from = 0
range_to = 100

numbers = []
for i in range(0, how_many):
    number = random.randint(range_from,range_to)
    numbers.append(number)
print(f"{how_many} random numbers\t {numbers}")

numbers.sort(reverse = True)
print(f"the top {top_how_many} are \t\t {numbers[0:top_how_many]}")