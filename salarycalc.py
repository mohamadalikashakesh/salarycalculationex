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
print("*************************")
print("Total Allocations Percentage for fixed expenses are: ", fixed_expenses)

print("*************************")
result_fixed = calculate_allocations(fixed_expenses, salary)
print("Detailed Allocations for fixed expenses are : ",result_fixed)
print("*************************")

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

#Extra Savings
old_savings = {
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0,
    "10" : 0,
    "11" : 0,
    "12" : 0,
}

extra_savings = 0
for key in old_savings:
    old_savings[month_number] = result_fixed['Savings']
#print(old_savings)
answer = input("Do you have any extra Savings ?(Press y to add n to exit)")
if answer == 'y':
    extra_savings = int(input("Please Enter Amount: "))
    old_savings = {key: value + extra_savings if value > 0 else value for key, value in old_savings.items()}
    #print(old_savings)
else:
    print("No Savings !")

print(f"Total Saving for Month {calender.get(month_number)} is $ {old_savings[month_number]}")
#print(f"Total Saving for Month {calender.get(month_number)} is $ {int(value in old_savings.items()) +extra_savings}")
print("*************************")
print("Remaining from Salary= $",remaining-extra_savings)
print("*************************")