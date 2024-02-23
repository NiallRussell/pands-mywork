number = float(input("Enter number (0 to quit):"))
numbers = []

while number != 0:
    numbers.append(number)
    number = float(input("Enter number (0 to quit):"))

average = sum(numbers)/len(numbers)
for value in numbers:
    print(value)
print(f'The average is {average}')
input("End")
