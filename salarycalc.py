"""
Nabiha, a software engineering consultant, receives a variable salary every month.
She wants to create a Python script that helps her manage her monthly finances by calculating
how much money will be allocated to different categories like savings, rent, and electricity, 
based on percentages of his salary.

Your task is to write a Python script that automates these calculations. The script should:

• Ask Nabiha to input her salary for the month.
• Ask Nabiha to input the name of the month she is storing the salary for.
• Ask Nabiha to input the following percentages for: a) Savings b) Rent c) Electricity

The script should calculate and display:

• The amount allocated to savings, rent, and electricity.
• The total amount Nabiha spends on savings, rent, and electricity combined.
• The remainder of Nabiha’s salary after these expenses.
• The monthly rent and electricity multiplied by 12 to estimate Nabiha's yearly rent and electricity costs.
• Nabiha's total salary for the month raised to the power of 2 (just for fun).
• Assume Nabiha saves an additional random amount (e.g., $50) each month, 
    and you need to calculate how much would be left if this amount is divided by the total amount allocated to savings. 

Finally, the script should output all the results in a readable format.
"""

#This function calculates the percentage of the given title according to salary
def calculate_allocations(data, number):
    newvalues = {}
    for key, value in data.items():
        newvalues[key] = value
    for key in newvalues:
        newvalues[key] = float(newvalues[key]) * number /100
    return newvalues

#This function returns the total value of allocations
def total_allocations(data):
    total = 0
    for value in data.values():
        total += value
    return total
    
name = str(input("Please Enter your Name:"))
print("Welcome "+name)
print("*************************")
calender = {
    "1" : "January",
    "2" : "February",
    "3" : "March",
    "4" : "April",
    "5" : "May",
    "6" : "June",
    "7" : "July",
    "8" : "August",
    "9" : "September",
    "10" : "October",
    "11" : "November",
    "12" : "December",
}
print("\n".join("{}\t{}".format(k, v) for k, v in calender.items()))
print("*************************")
month_number = input("Please Enter month number to calculate Salary: ")
salary = float(input(name + " Please Enter Your Salary for month " + calender.get(month_number) + ": "))
#print(calender.get(month_number))
print("*************************")

fixed_expenses = {
    "Savings" : "0",
    "Rent" : "0",
    "Electricity" : "0"
}
for key in fixed_expenses:
    user_input = input(f"Enter a Percentage value to deduct from Salary for '{key}': ")
    value = int(user_input)
    fixed_expenses[key] = value
print("Total Allocations Percentage for fixed expenses are: ", fixed_expenses)


title_perc = fixed_expenses
while True:
    key = input("Enter Title to pay from Salary (or type 'exit' to stop): ")
    if key.lower() == "exit":
        break
    value = input("Enter Percentage: ")
    
    title_perc[key] = value
#print(title_perc) #Printing the Dictionary For Testing

print("*************************")
result = calculate_allocations(title_perc, salary)
print("Detailed Allocations are : ",result)

print("*************************")
total_sum = total_allocations(result)
print("Total Allocations = $",total_sum)

#Remaining From Salary Calculation
print("*************************")
remaining = salary - total_sum
print("Remaining From Salary: $",remaining)

#Rent and electricity Yearly Expenses
print("*************************")
print("Rent Value Per Year: $",result['Rent']*12)
print("Electricity Value Per Year: $",result['Electricity']*12)
print("*************************")
#Salary to the power 2
salary_square = salary*salary
print("Your Salary to the power 2 is : $" , salary_square)
print("*************************")
