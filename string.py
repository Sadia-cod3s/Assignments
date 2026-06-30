# Question No 1
email = "bestpostbusiness@gmail.com"
employee_username = email[0:16]
company_name = email[16:22]
domain_extension = email[22:]
email_without_domain_extension ="(employee_username)+(company_name)"
first_12_char_of_email = email[0:16]
last_10_char_of_email = email[-10:]
print("Employee Username:" ,employee_username)
print("Company Name:" ,company_name)
print("Domain_Extension:" ,domain_extension)
print("Email Without Domain Extention:" ,email_without_domain_extension)
print("First 12 characters:" ,first_12_char_of_email)
print("last 10 characters:" ,last_10_char_of_email)

# Question No 2
product_code = "MOB-OPPO-F19-128GB-BLUE"
category = product_code[0:3]
company = product_code[4:9]
model = product_code[10:12]
storage = product_code[22:27]
color = product_code[29:]
first_char_company = product_code[4]
last_char_model = product_code[20]
print("Product Category:", category)
print("Company Name:", company)
print("Model Name", model)
print("Storage Size:", storage)
print("Product Color:", color)
print("First Characters Company Name:", first_char_company)
print("Last Characters Model Name:", last_char_model)

# Question No 3
banking_SMS = "PKR 50000 has been successfully transferred to account 12345"
transferred_amount = banking_SMS[4:9]
account_num = banking_SMS[-5:]
transaction_status = banking_SMS[19:30]
first_25_characters = banking_SMS[0:26]
last_15_characters = banking_SMS[-15:]
count_letter_a = banking_SMS.count("a")
print("Transferred Amount:", transferred_amount)
print("Account Number:", account_num)
print("Transaction Status:", transaction_status)
print("First 25 Character:", first_25_characters)
print("Last 15 Character:", last_15_characters)
print("Count Letter a:", count_letter_a)

# Question No 4
student_record = 'B-ED|2013|045|Azharuddin'
department_name = student_record[0:4]
batch_year = student_record[5:9]
roll_number = student_record[10:0]
full_name = student_record[14:]
first_name = student_record[14:22]
initials = full_name[0] + '.' + full_name[0] + '.'

print("Department Name",department_name)
print('Batch Year', batch_year)
print('Roll Number', roll_number)
print('Student full name', full_name)
print('Only first name', first_name)
print('initials', initials)

# Question No 5
url = 'https://www.colourpouch.com'
remove_https = url[8:]
remove_www = url[12:]
website_name = url[12:-4]
domain_extension = url[-4:]
ends_with_com = url.endswith(".com")
middle_portion = url[10:25]

print(" remove https://:", remove_https)
print("remove_www.:", remove_www)
print("Website_Name:", website_name) 
print("Domain_Extension:", domain_extension) 
print("Ends_with_com:", ends_with_com) 
print("Middle_Portion:", middle_portion)

# Question No 6
password = 'Dreamisarmy133292!'
hidden_format = password[0] + '*' * (len(password) - 2) + password[-1]
first_character = password[0]
last_character =  password[-1]
total_length = len(password)
middle_characters = password[4:12]
ends_with_number = password[-1].isdigit()

print('Hidden_format:', hidden_format)
print("First_Character:", first_character)
print("Last_Character:", last_character)
print("Total_Length:", total_length)
print("Middle_Characters:", middle_characters)
print("Ends_with_Number:", ends_with_number)

# Question No 7
filename = "python_final_project_documentation_2026 .pdf"
new_filename = filename.replace("_"," ")
print("===============Q.7 FileManagment System===============")
print(new_filename[0:39])
print(new_filename[-5:-1])
print(new_filename.endswith(".pdf"))
print("First 20 Characters:",new_filename[0:21])
print("Last 10 Characters:", new_filename[-10:-1])

# Question No 8
first_name = "Sadia"
last_name = "Umair"
favorite_game = "chess"
lucky_number = "14"

username = first_name + "_" + last_name + "_" + favorite_game + "_" + lucky_number

without_lucky_number = username[:-3]  
game_name = username[14:19]  
only_lucky_number = username[-2:]  
first_8_characters = username[:8]  
last_6_characters = username[-6:]  
capitalize_format = username.capitalize()

print("Username:", username)
print("Without Lucky Number:", without_lucky_number)
print("Game Name:", game_name)  
print("Only Lucky Number:", only_lucky_number)
print("First 8 Characters:", first_8_characters)  
print("Last 6 Characters:", last_6_characters)
print("Capitalize Format:", capitalize_format)  

# Question No 9
message = "hello mam i have completed my python assigment successfully"
print("===============Q.9 Chat Application Massage Analyzer===============")
print(message.capitalize())
print(message.replace("python", "javascript"))  
print(len(message))
print(message.find("s"))
print(message[0:19]) 
print(message[-20:])  
print(message[18:27]) 

# Question No 10
Course_information = "python programming complete bootcamp 2026"
print("===============Q.10 Online Course Information System===============") 
print("Course:", Course_information[0:17])
print("Batch_year:", Course_information[-4:])  
print("First_Word:", Course_information[0:6])  
print("Last_Word:", Course_information[-4:])  
print(Course_information[0:15])
print(Course_information[-12:])
print(Course_information.find("o"))
print(Course_information.endswith("2026"))