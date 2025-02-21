

def calculate_allocations(data, number):
    newvalues = {}
    for key, value in data.items():
        newvalues[key] = value
    for key in newvalues:
        newvalues[key] = float(newvalues[key]) * number /100
    return newvalues







title_perc = {}
while True:
    key = input("Enter Title to pay from Salary (or type 'exit' to stop): ")
    if key.lower() == "exit":
        break
    value = input("Enter Percentage: ")
    
    title_perc[key] = value
#print(title_perc) #Printing the Dictionary For Testing

salary = float(1200)
print(calculate_allocations(title_perc, salary))
