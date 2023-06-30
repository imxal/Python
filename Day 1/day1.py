#day1
#Numbers, Arithmetic, and Printing to the Console, variables, getting input from users

#addition
print(1 + 2)
print(3.4 + 11)
print(8 + 4.0)

#subtraction
print(-4 - 9)

#division
print(5 / 6.5)
print(20 / 2)
print(5.5 / 0.5)

## exponential(**)=> square
print(3 ** 2)  

# modulus(%) vs /
print(5 % 2)  #=>1
print(5 / 2)  #=>2.5


# Floor division operator(//)
print(5 // 2)  


#multiple operators
print((4 - 5) * (5 + 3) / 2)


print("I am learning python. It's Day 1 of learning.")

#Calculate and print the number of days, weeks, and months in 27 years. Don’t worry about leap years!

#no.of days
print(365 * 27) 

#no.of weeks
print(52*27)

#no.of month
print(27*12)

#Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.
print(3.14*(5*5))
#using square
print(3.14 * 5**2)
#using pow
print(3.14 * pow(5,2) )

# Checking data types
print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Laxmi'))             # String
print(type([1, 2, 3]))           # List
print(type({'name':'Laxmi'}))    # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

print([1, 2, 3]) 
print({'fname':'Laxmi','lname':'Satyal'})
print({9.8, 3.14, 2.7})
print((9.8, 3.14, 2.7))



#variables 
workinghour= 8
salary= 50000
skill= "python"

#getting input from users
name = input("Please enter your name: ")

#Ask the user for their name and age, assign theses values to two variables, and then print them.
myname=input("Enter your name: ")
age= input("Enter your age: ")
print(myname)
print(age)



# declaring variables in one line and printing
first_name, last_name, country, age,  = 'Laxmi', 'Satyal', 'Nepal', 20, 
print( {'name': first_name, 'lname': last_name, 'country': country,  'age': age,} )

