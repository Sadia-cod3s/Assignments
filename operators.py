# Question No 1
burger_price = 400
pizza_price = 2200
burger_quantity = 4
pizza_quantity = 3
total_bill = (burger_price * burger_quantity) + (pizza_price * pizza_quantity)
delivery_charges = 2400
final_bill = (total_bill) + (delivery_charges)
print("Total_food_price" , total_bill)
print("Delivery_charges" , delivery_charges)
print("Final_bill =" , final_bill)

# Question No 2
English = 64
Urdu = 72 
Math = 58
Physics = 63
Pakistan_Studies = 78
total_marks = (English)+(Urdu)+(Math)+(Physics)+(Pakistan_Studies)
Percentage = (total_marks/500) * (100)
print("English" , English)
print("Urdu" , Urdu)
print("Math" , Math)
print("Physics" , Physics)
print("Pakistan_Studies" , Pakistan_Studies)
print("Percentage" , Percentage)

# Question No 3
product_price = 5000
discount_percentage = 100
discount_amount = product_price * (discount_percentage/100)
final_price = product_price - discount_percentage
comparison_result = final_price / 5000
print("Product_price:",product_price)
print("Discount_Amount:", discount_amount)
print("Final_price:",final_price)
print("Comparison_result:",comparison_result)

# Question No 4
account_balance = 50000
withdrawl_amount = 70000
account_balance -= withdrawl_amount
banking_fees =10000
account_balance -= banking_fees
print("Withdrawl_amount:" , withdrawl_amount)
print("Banking_Fees:" , banking_fees )
print("Remaining_Balance:" , account_balance)

# Question No 5
usernamestatus = True
passwordstatus = True
fingerprintstatus = False
finalloginresult = usernamestatus and (passwordstatus or fingerprintstatus)

print("User Name Status:" , usernamestatus)
print("Password Status:" , passwordstatus)
print("Finger Print Status:" , fingerprintstatus)
print("Final Login Result:" , finalloginresult)

# Question No 6
kilometers = 100
fuelused = 3000
average = kilometers / fuelused

print("Total Kilometers:" , kilometers)
print("Fuel Used:" , fuelused)
print("Average:" , average)
print("Comparison Result:" , average >= 15)

# Question No 7
basicsalary = 80000
bonus = 25000
tax = 5000
basicsalary += bonus
basicsalary -= bonus
finalsalary = basicsalary

print("Basic Salary:" , 80000)
print("Bonus:" , bonus)
print("Tax:" , tax)
print("Final Salary:" , finalsalary)

# Question No 8
studentper = 84
teststatus = False
eligibilityresult = (studentper >=70) and (teststatus == False)

print("Percentage:" , studentper)
print("Test Status:" , teststatus)
print("Eligibility Result:" , eligibilityresult)

# Question No 9
electricityunits = 331
priceunit = 94
totalbill = 331 * 94
tax = 350
totalbill += tax
finalbill = totalbill

print("Units:" , electricityunits)
print("Unit Price:" , priceunit)
print("Tax:" , tax)
print("Final Bill:" , finalbill)

# Question No 10
mobilephoneprice = 30000
downpayment = 15000
remainingamount = mobilephoneprice - downpayment
installment = remainingamount / 12
comparisonResult = installment <= 5000


print("Phone Price:" , mobilephoneprice)
print("Down Payment:" , downpayment)
print("Remaining Amount:" , remainingamount)
print("Monthly Installment:" , installment)
print("Comparison Result:" , comparisonResult)