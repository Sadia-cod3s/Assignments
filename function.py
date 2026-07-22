# Python Functions Assignment

print("Question - 1")
def print_list_length(my_list):
    print("Length of the list:", len(my_list))

print("Question - 2")
def print_list_elements(my_list):
    print("Elements of the list:", end=" ")
    for element in my_list:
        print(element, end=" ")
    print()  
    
print("Question - 3")
def find_factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial

print("Question - 4")
def convert_pkr_to_usd(pkr):
    exchange_rate = 280      
    usd = pkr / exchange_rate  
    return round(usd, 2)       

print("Question - 5")
def check_even_odd(number):
    if number % 2 == 0:      
        return f"{number} is Even"  
    else:                    
        return f"{number} is Odd"   

# --- Testing the functions ---
if __name__ == "__main__":
    print("--- Q1 ---")
    sample_list1 = [10, 20, 30, 40, 50]
    print_list_length(sample_list1)

    print("\n--- Q2 ---")
    sample_list2 = ["Apple", "Banana", "Mango", "Orange"]
    print_list_elements(sample_list2)

    print("\n--- Q3 ---")
    num = 5
    print(f"Factorial of {num} is:", find_factorial(num))

    print("\n--- Q4 ---")
    pkr_amount = 5600
    print(f"{pkr_amount} PKR = {convert_pkr_to_usd(pkr_amount)} USD")

    print("\n--- Q5 ---")
    test_num = 17
    print(check_even_odd(test_num))