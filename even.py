numbers = [1,3,5,9,2]
even = None
index = 0
number = numbers[index]

while number % 2 != 0:
    index += 1
    number = numbers[index]

print(numbers[index])