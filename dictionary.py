# ========== Question 1 - Student Profile System ==========
student = {
    "name": "Sadia", 
    "age": 14, 
    "city": "Karachi",
    "hobbies": ["reading", "coding", "drawing"], 
    "skills": ["Python", "HTML", "English"] 
}

print("Student Name:", student["name"])
print("First Hobby:", student["hobbies"][0])
print("Total Skills:", len(student["skills"]))

# ========== Question 2 - Student Marks System ==========
marks = {
    "math": 85, 
    "english": 78,
    "science": 92,
    "computer": 88
}

print("\nAll Subject Marks:")
for subject, score in marks.items():
    print(subject, ":", score)

total = sum(marks.values())
average = total / len(marks)
print("Total Marks:", total)
print("Average Marks:", average)

# ========== Question 3 - Grade Checking System ==========
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("\nFinal Grade:", grade)
if grade == "Fail":
    print("Status: Failed")
else:
    print("Status: Passed")

# ========== Question 4 - Attendance Management System ==========
attendance = {
    "total_classes": 24, 
    "attended_classes": 18 
}

percentage = (attendance["attended_classes"] / attendance["total_classes"]) * 100
print("\nAttendance Percentage:", round(percentage, 2), "%")

if percentage < 75:
    print("Short Attendance")
else:
    print("Eligible For Exam") 

# ========== Question 5 - Fee Management System ==========
student_fee = {
    "name": "Sadia",
    "fee_paid": True 
}

if student_fee["fee_paid"]:
    print("\nFee Cleared")
else:
    print("\nFee Pending")

# ========== Question 6 - Skills Management System ==========
skills_data = {
    "skills": ["Python", "HTML", "CSS"]
}

skills_data["skills"].append("JavaScript") 
skills_data["skills"].remove("CSS") 

print("\nUpdated Skills List:", skills_data["skills"])
print("Total Skills:", len(skills_data["skills"]))

# ========== Question 7 - Login Authentication System ==========
login = {
    "username": "sadia14", 
    "password": "pass123" 
}

user = input("Enter Username: ")
pwd = input("Enter Password: ")

if user == login["username"] and pwd == login["password"]:
    print("Login Successful")
else:
    print("Invalid Credentials")

# ========== Question 8 - Address Management System ==========
address = {
    "area": "Gulshan Iqbal", 
    "street": "Street 5",
    "house_number": "D-5" 
}

print("\nComplete Address:", address["house_number"] + ",", address["street"] + ",", address["area"])

address["area"] = "Nazimabad" 
address["zip_code"] = "75300" 

print("Updated Address:", address)

# ========== Question 9 - Multiple Students Database ==========
students = {
    "student1": {"name": "Ali", "city": "Lahore", "marks": 88},
    "student2": {"name": "Sadia", "city": "Karachi", "marks": 92} 
}

print("\nStudent1 Name:", students["student1"]["name"])
print("Student2 Marks:", students["student2"]["marks"])

students["student2"]["city"] = "Gulshan Iqbal" 
print("Updated Student2:", students["student2"])

# ========== Question 10 - FINAL STUDENT REPORT CARD SYSTEM==========

 # 1. Nested Dictionary
student_report = {
    "profile": {
        "name": "Sadia",  
        "age": 14,
        "hobbies": ["reading", "coding", "drawing"], 
        "skills": ["Python", "HTML", "English"]      
    },
    "marks": {
        "math": 85,
        "english": 78,
        "science": 92,
        "computer": 88
    },
    "attendance": {
        "total_classes": 24,   
        "attended_classes": 18 
    },
    "fee": {
        "status": True  
    },
    "address": {
        "house_number": "D-5",         
        "street": "Street 5", 
        "area": "Gulshan Iqbal",     
        "zip_code": "75300"
    }
}

# 2. Calculations
marks = student_report["marks"]
total = sum(marks.values())
average = total / len(marks)

# 3. Grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

# 4. Attendance
att = student_report["attendance"]
attendance_per = (att["attended_classes"] / att["total_classes"]) * 100
if attendance_per >= 75:
    attendance_status = "Eligible For Exam"
else:
    attendance_status = "Short Attendance"

# 5. Fee
if student_report["fee"]["status"]:
    fee_status = "Fee Cleared"
else:
    fee_status = "Fee Pending"

# ========== PRINT REPORT CARD ==========
print("="*40)
print("        STUDENT REPORT CARD")
print("="*40)

print("\n--- PROFILE ---")
print("Name:", student_report["profile"]["name"])
print("Age:", student_report["profile"]["age"])
print("Address:", student_report["address"]["house_number"] + ",", 
      student_report["address"]["street"] + ",", 
      student_report["address"]["area"] + ",", 
      student_report["address"]["zip_code"])
print("Hobbies:", ", ".join(student_report["profile"]["hobbies"]))
print("Skills:", ", ".join(student_report["profile"]["skills"]))
print("Total Skills:", len(student_report["profile"]["skills"]))

print("\n--- MARKS ---")
for subject, score in student_report["marks"].items():
    print(subject.capitalize(), ":", score)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Final Grade:", grade)

print("\n--- OTHER DETAILS ---")
print("Attendance:", round(attendance_per, 2), "% -", attendance_status)
print("Fee Status:", fee_status)

print("\n--- RESULT ---")
if grade != "Fail" and attendance_status == "Eligible For Exam" and student_report["fee"]["status"]:
    print("Status: PASSED")
else:
    print("Status: FAILED")
print("="*40)