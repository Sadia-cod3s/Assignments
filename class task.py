print("Question No 1")
name = input("Enter Name:")
age = input("Enter Age:")
city = input("Enter City: ")
course = input("Enter Course: ")
total_marks = int(input("Enter total marks: "))
obtained_marks = int(input("Enter obtained marks: "))

percentage = (obtained_marks / total_marks) * 100

print("\n===============Student Profile===============")
print("Name :", name)
print("Age :", age)
print("City :", city)
print("Course :", course)
print("Percentage:", str(percentage) + "%")

print("\nData Types:")
print("name:", type(name))
print("total_marks:", type(total_marks))
print("percentage:", type(percentage))

print("Question No 2")
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
birth_year = input("Enter Birth Year: ")

username = first_name + last_name + birth_year
username = username.lower()

print("\nUsername :", username)
print("Length :", len(username))
print("First Character:", username[0])
print("Last Character :", username[-1])

print("Question No 3")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
power = num1 ** num2

print("\nAddition :", addition)
print("Subtraction :", subtraction)
print("Multiplication:", multiplication)
print("Division :", division)
print("Modulus :", modulus)
print("Power :", power)

print("Question No 4")
sentence = input("Enter a sentence: ")

print("\nUppercase :", sentence.upper())
print("Lowercase :", sentence.lower())
print("Capitalize :", sentence.capitalize())
print("Count of a :", sentence.count('a'))
print("Replace ' with '-':", sentence.replace(" ", "-"))
print("Reverse :", sentence[::-1])

print("Question No 5")
email = input("Enter your email: ")

is_gmail = email.endswith("@gmail.com")
username = email.split("@")[0]

print("\nValid Gmail :", is_gmail)
print("Username :", username)
print("Length :", len(email))

print("Question No 6")
product_name = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))

total_bill = price * quantity
discount = total_bill * 0.10
final_bill = total_bill - discount

print("\nProduct :", product_name)
print("Quantity :", quantity)
print("Total Bill :", total_bill)
print("Discount :", discount)
print("Final Bill :", final_bill)

print("Question No 7")
name = input("Enter Name: ")
age = input("Enter Age: ")
city = input("Enter City: ")
course = input("Enter Course: ")

print("\n===============Bio Data Card===============")
print("Name\t: " + name + "\nAge\t: " + age + "\nCity\t: " + city + "\nCourse\t: " + course)

print("Question No 8")
password = input("Enter password: ")

print("\nPassword Length :", len(password))
print("Contains @ :", '@' in password)
print("First 3 Characters:", password[0:3])
print("Last 3 Characters :", password[-3:])

print("Question No 9")
movie_name = input("Enter Movie Name: ")
ticket_price = float(input("Enter Ticket Price: "))
quantity = int(input("Enter Quantity: "))

total_amount = ticket_price * quantity

print("\n===============Movie Receipt===============")
print("Movie :", movie_name)
print("Tickets :", quantity)
print("Total Amount :", total_amount)

print("Question No 10")
customer_name = input("Enter Customer Name: ")
food_item = input("Enter Food Item: ")
price = float(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

total_bill = price * quantity

print("\n===============Food Order Receipt===============")
print("Customer :", customer_name)
print("Item :", food_item)
print("Quantity :", quantity)
print("Total Bill:", total_bill)
