#for loops, break statement, range function
print(range(0,10))

numbers = list(range(10))             
print(numbers)

for number in range(10):
    print(number)

for _ in range(10):
    print("Hello World")


#Print how much each employee is due to be paid at the end of the week in a nice, readable format and print out those who are earning an hourly wage above average.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]


for emp in employees:
 Amount=float(emp[1]*emp[2])
 print((f"{emp[0]} is due {Amount}"))

 

total=0
count=0
for emp in employees:
   total=float(total+emp[2])
   count=float(count+1)
   average=total/count

   
for emp in employees:
    if emp[2] > average:
        print(f"{emp[0]} earns more than average.")



#--------------------------------------------------------------------------------------------------------------------------
#fizz and buzz
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num%5== 0:
        print("Buzz")
    elif num % 3 == 0 :
        print("Fizz")
    else:
        print(num)
