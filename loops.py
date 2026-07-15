# While Loop
i = 1
while i <= 100:
    print(i)
    i += 1
    
i = 100
while i >= 1:
    print(i)
    i -= 1
    
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
    
numbers = [12, 45, 8, 23, 67, 34, 90, 15, 56, 78]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
    
numbers = (18, 45, 72, 91, 34, 56, 29, 83, 67, 10)
x = int(input("Enter number to search: "))
i = 0
found = False
while i < len(numbers):
    if numbers[i] == x:
        found = True
        print(f"{x} found at index {i}")
        break
    i += 1
if not found:
    print(f"{x} not found")
    
n = int(input("Enter n: "))
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print("Sum =", sum)

# Loops
fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Grapes', 'Peach', 'Cherry', 'Guava', 'Pineapple', 'Watermelon']
for fruit in fruits:
    print(fruit)
    
cities = ('Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Quetta', 'Multan', 'Hyderabad', 'Faisalabad', 'Sialkot', 'Sukkur')
x = input("Enter city name to search: ")
found = False
for i in range(len(cities)):
    if cities[i] == x:
        found = True
        print(f"{x} found at index {i}")
        break
if not found:
    print(f"{x} not found")

n = int(input("Enter n: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)

# Range
for i in range(1, 101):
    print(i)

for i in range(100, 0, -1):
    print(i)
    
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")