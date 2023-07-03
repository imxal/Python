#conditionals and booleans
#Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.


a=[1,2,3]
b=a
c=[1,2,3]

a==b #true
a is b #true

a==c #true
a is c #false

print(id(a)== id(c)) #false
print(id(a)== id(b)) #true


#------------------------
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(id(numbers))
print(id(new_numbers))

print (numbers is new_numbers) #false

numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))


#Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
number=int(input("Enter any number "))
if number > 0 :
    print(f"{number} is a positive number")
elif number<0:
    print(f"{number} is a negative number")
else:
    print(f"You entered is zero")   


#Ask the user to enter a number. Tell the user whether the number is odd,even or negative.
number=int(input("Enter any number "))
if number % 2 == 0 :
    print(f"{number} is a even number")
elif number<0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is odd")   

#Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
#If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours.
#In effect, the employees get paid 110% of their hourly wage for any overtime.

Hours_worked=float(input("How many hours did you work? "))
Hourly_wage=float(input("What is your hourly wage? "))
Amount= Hourly_wage * Hours_worked

if Hours_worked > 40 :
    Over_time= (Amount) +( (Hours_worked - 40)  * Hourly_wage * 10/100)
   
    print(f"you will be paid  {Over_time}")
else:
    
    print (f"you will be paid {Amount}")

#alternative way
Hours_worked=float(input("How many hours did you work? "))
Hourly_wage=float(input("What is your hourly wage? "))
Amount= Hourly_wage * Hours_worked

if Hours_worked > 40 :
    
    Over_time=  40 * Hourly_wage + ((Hours_worked - 40)  * Hourly_wage * 110/100)
   
   
    print(f"you will be paid  {Over_time}")
else:
    
    print (f"you will be paid {Amount}")




    