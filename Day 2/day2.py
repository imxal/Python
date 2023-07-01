#formatting strings and processing user input

hours_worked = input("How many hours did you work this week? ")
print("Hours worked: " + hours_worked)

#converting int to str
age =str(28)
print(type(age))

#using format
print("{} is {} years old! already, How fast the time flies".format("John", 24))

#different ways to use format
output = "{} is {} years old, and {} works as a {}."
print(output.format("John", 24, "John", "web developer"))

output1 = "{0} is {1} years old, and {0} works as a {2}."
print(output1.format("Ram",24,"Web developer"))

output2= "{name} is {age} and {name} works as {job}."
print(output2.format(name="Ram",age=24, job="web developer"))


#String interpolation with f-strings
name="Evan"
age_evan=20
print(f"{name} is {age_evan * 12} months old")

#Basic String Processing
"hello world".upper()
"hello world".lower()
"hello world".capitalize()
"hello world".title()
" hello world ".strip() #removes white space

" hello world ".strip().title()


greeting = "Hello"
print(greeting + "!")

print(f"{greeting}!")

username=input("fname: ")
print((greeting + " " f"{username}!" ))

"I am "+ str(20)


title = "Joker"
director = "Todd Phillips"
release_year = 2019
print(f"{title}({release_year}), directed by {director} ")

