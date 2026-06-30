# QUESTION NO:1
print("======================================================")
print("                  Online Food Delivery System")
print("======================================================")
Foods = ["Burger" , "Pizza" , "Fries" , "Broast" , "Sandwich"]
print("First food item ===>" , Foods[0])
print("last food item ===>" , Foods[-1]) 

Foods[2] = "pasta"
print("Replace 'Fries' with 'Pasta'===>" , Foods)

Foods.append("Zinger")
print("Add 'Zinger' at the end ===>" , Foods)

Foods.insert(2, "Shawarma")
print("Insert 'Shawarma' at index 2 ===>" , Foods)

Foods.remove("Pizza")
print("Remove 'Pizza' ===>" , Foods)

Foods.pop()
print("Remove last item using 'pop()' ===>", Foods)

print("Print total items using 'len()' ===>" ,len(Foods))

print("first 3 items ===>" , Foods[0:3])
print("last 2 items ===>" , Foods[-2:])

Foods.reverse()
print("Reverse the list ===>" , Foods)

Foods.sort(reverse=True)
print("Sort the list ===>" , Foods)

print("Print final updated list ===>" , Foods)

# QUESTION NO:2
print("======================================================")
print("                 Student Attendance Management")
print("======================================================")
students = ["Ali", "Sara", "Ahmed", "Zoha Khan", "Hira"]
print("second student name ===>" , students[2])
print("last student name ===>" , students[-1])

students[2] = "Hamza"
print("Replace Change 'Ahmed' into 'Hamza' ===>" , students)

students.append("Fatima")
print("Add 'Fatima' in the list ===>" , students)

students.insert(1, "Ayesha")
print("Insert 'Ayesha' at index 1 ===> , students")

students.remove("Sara")
print("remove student ===>" , students)

students.pop(3)
print("Remove student at index 3 'pop()' ===>", students)

print("Print total students ===>" ,len(students))

print("students from index 1 to 4 ===>" , students[1:4])

students.reverse()
print("Reverse the list ===>" , students)

print("Print final updated list ===>" , students)

#QUESTION NO:3
print("======================================================")
print("                 Mobile Prices Analysis")
print("======================================================")

prices = [45000, 120000, 30000, 85000, 60000]

prices.sort()
print("Sort the list ===>" , prices)

print(prices[-1])
print(prices[0])

prices.sort()
print("Sort prices in ascending order" , prices)

prices.sort(reverse=True)
print("Sort prices in descending order" , prices)

prices.append("90000")
print("Add new mobile price ===>" , prices)

prices.remove(120000)
print("Remove one price using remove() ===>" , prices)

prices.pop(-1)
print(" Remove last price using pop() ===>", prices)

print("first 3 prices ===>" , prices[0:3])
print("last 2 prices ===>" , prices[-2:])

print ("total number of prices ===>" , prices)

#QUESTION NO:4
print("======================================================")
print("                 Cricket Team Management")
print("======================================================")

players = ["Babar", "Virat", "Shaheen", "Buttler", "Rashid"]

print("Captain Name:" , players[0])
print(players[-1])

players[4] = "Wasim"
print(players)

players.append("Rizwan")
print(players)

players.insert(2, "Shoaib Malik")
print(players)

players.remove("Buttler")
print(players)

print(players[0:4])
print(players[-3:])

players.reverse()
print(players)

#QUESTION NO:5
print("======================================================")
print("                 Shopping Cart System")
print("======================================================")

cart = ["Shoes", "Watch", "Bag", "Laptop", "Bottle"]

print("First item:", cart[0]) 
print("Last item:", cart[-1]) 

cart[cart.index("Bottle")] = "Headphones" 
cart.append("Keyboard") 
cart.insert(1, "Mouse") 
cart.remove("Bag") 
cart.pop() 

print("Total cart items:", len(cart)) 
print("Middle 3 items:", cart[1:4]) 

cart.reverse() 
print("Updated cart:", cart) 

#QUESTION NO:6
print("======================================================")
print("                  Employee Salary Records")
print("======================================================")

salaries = [25000, 40000, 70000, 55000, 90000]

print("Highest salary:", max(salaries)) 
print("Lowest salary:", min(salaries)) 

salaries.sort()
print("Ascending:", salaries)

salaries.sort(reverse=True) 
print("Descending:", salaries)

salaries.append(65000) 
salaries.remove(25000) 

print("Second highest salary:", salaries[1]) 
print("First 3 salaries:", salaries[:3]) 
print("Total salaries count:", len(salaries)) 
print("Final salary list:", salaries) 

#QUESTION NO:7
print("======================================================")
print("                   Movie Collection System")
print("======================================================")

movies = ["Janaan", "Stree", "Raees", "Dhamaal", "Alpha"]

print("First movie:", movies[0]) 
print("Last movie:", movies[-1]) 

movies[movies.index("Raees")] = "Highway" 
movies.append("War 2") 
movies.insert(3, "Animal") 
movies.remove("Dhamaal") 
movies.pop() 

print("First 4 movies:", movies[:4])
movies.reverse() 
print("Final updated movie collection:", movies)

#QUESTION NO:8
print("======================================================")
print("                    Exam Marks Analysis")
print("======================================================")

marks = [78, 45, 90, 66, 82]

print("Highest marks:", max(marks)) 
print("Lowest marks:", min(marks)) 

marks.sort() 
print("Sorted marks:", marks)

marks.sort(reverse=True) 
print("Descending marks:", marks)

marks.append(88) 
marks.remove(45) 

print("Top 3 marks:", marks[:3]) 
print("Last 2 marks:", marks[-2:]) 
print("Total subjects:", len(marks)) 
print("Final marks list:", marks)

# QUESTION NO:9
print("======================================================")
print("                    Website Visitors Record")
print("======================================================")

visitors = ["Ali", "Sara", "Ahmed", "Zoha Khan", "Hira"]

print("First visitor:", visitors[0]) 
print("Last visitor:", visitors[-1]) 

visitors.append("Bilal") 
visitors.insert(2, "Fatima") 
visitors.remove("Ahmed") 
visitors.pop() 

print("First 3 visitors:", visitors[:3]) 
print("Last 3 visitors:", visitors[-3:]) 

visitors.reverse() 
print("Total visitors:", len(visitors))

# QUESTION NO:10
print("======================================================")
print("                    Programming Languages System")
print("======================================================")

languages = ["Python", "JavaScript", "Java", "C++", "PHP"]

print("First language:", languages[0])
print("Last language:", languages[-1]) 

languages[languages.index("PHP")] = "TypeScript" 
languages.append("Go") 
languages.insert(2, "Rust") 
languages.remove("Java") 

print("First 4 languages:", languages[:4]) 
print("Last 2 languages:", languages[-2:]) 

languages.sort() 
print("Sorted:", languages)

languages.reverse() 
print("Final updated languages list:", languages)