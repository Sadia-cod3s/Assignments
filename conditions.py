print("Question No 1")
balance = int(input("Enter Account Balance: "))
withdraw = int(input("Enter Withdraw Amount: "))

if withdraw > balance:
    print("Insufficient Balance")
elif withdraw < 500:
    print("Minimum withdrawal is 500")
else:
    balance = balance - withdraw
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)

if balance > 10000:
    print("Premium User")
else:
    print("Normal User")
    
print("Question No 2")
username = input("Enter Username: ")

if len(username) < 8:
    print("Username must be at least 8 characters long")
elif " " in username:
    print("Username should not contain spaces")
elif not username[0].isupper():
    print("Username must start with a capital letter")
elif not any(char.isdigit() for char in username):
    print("Username must contain at least one number")
else:
    print("Username is Valid")
    
print("Question No 3")
name = input("Enter Student Name: ")
attendance = float(input("Enter Attendance Percentage: "))
fees_status = input("Enter Fees Status (paid/unpaid): ")

if attendance >= 75 and fees_status.lower() == "paid":
    print(name, "is Eligible For Exam")
else:
    if attendance < 75:
        print("Not Eligible: Attendance less than 75%")
    if fees_status.lower()!= "paid":
        print("Not Eligible: Fees not paid")
        
print("Question No 4")
password = input("Enter Password: ")

has_digit = False
has_special = False
special_chars = "!@#$%^&*"   

for char in password:
    if char.isdigit():
        has_digit = True
    if char in special_chars:
        has_special = True

conditions = 0
if len(password) >= 8:
    conditions += 1
if has_digit:
    conditions += 1  
if has_special:
    conditions += 1

if conditions == 3:
    print("Strong Password")
elif conditions == 2:
    print("Medium Password")
else:
    print("Weak Password")
    
print("Question No 5")
name = input("Enter Customer Name: ")
bill = float(input("Enter Total Bill: "))
membership = input("Membership Status (yes/no): ")

print("\n===============Bill Receipt===============")
print("Customer Name:", name)

if bill > 5000 and membership.lower() == "yes":
    discount = bill * 0.20
    final_bill = bill - discount
    print("20% Discount Applied")
elif bill > 3000:
    discount = bill * 0.10
    final_bill = bill - discount
    print("10% Discount Applied")
else:
    final_bill = bill
    print("No Discount")

print("Total Bill:", bill)
print("Final Bill to Pay:", final_bill)

print("Question No 6")
email = input("Enter Email: ")

if email.endswith("@gmail.com") and " " not in email and len(email) > 12:
    print("Email Verified")
else:
    print("Invalid Email")
    
print("Question No 7")
num = int(input("Enter a Number: "))

print("\n===============Analysis===============")
if num >= 0:
    print("Number is Positive")
else:
    print("Number is Negative")

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

if num % 5 == 0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

if num > 100:
    print("Large Number")
    
print("Question No 8")
username = input("Enter Username: ")
password = input("Enter Password: ")

if username and password: 
    print("Login Attempted")
    print("Username in lowercase:", username.lower())
    print("Reversed username:", username[::-1]) 
else:
    print("Fields Cannot Be Empty")
    
print("Question No 9")
sentence = input("Enter a Sentence: ")

if "Python" in sentence:
    print("Python Found")

if len(sentence) > 20:
    print("Long Sentence")
else:
    print("Short Sentence")

new_sentence = sentence.replace("Python", "JavaScript")
print("After Replace:", new_sentence)
print("Reversed Sentence:", sentence[::-1])

print("Question No 10")
username = input("Enter Username: ")
password = input("Enter Password: ")
role = input("Enter Role (admin/student): ")
correct_user = "Admin"
correct_pass = "Admin123"

if username == correct_user and password == correct_pass:
    if role.lower() == "admin":
        print("Welcome Admin")
    elif role.lower() == "student":
        print("Welcome Student")
    else:
        print("Invalid Role")
else:
    print("Invalid Username or Password")