#calculating earnings
employee_name=(input("enter name: ").strip().title())
hourly_wage= (input("enter your hourly wage: "))
woked_hours= (input("enter your working hours: ")) 
earning=(float(hourly_wage) * float(woked_hours))

print(f"{employee_name} earned {earning} this week.")

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length=float(input("Enter length: "))
width=float(input("Enter width: "))
Area=length*width
print(Area)
perimeter=2*(length+width)
print(perimeter)

#Use in operator to check if jargon is in the sentence.
("jargon" in "I hope this course is not full of jargon.") 

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
"on" in "python" and "on" in "dragon"

#Find the length of 'python' and 'dragon' 
len("python")
len("dragon")

#Find the length of the text python and convert the value to float and convert it to string
value=len("python")
print(value)
float(value)
str(value)


#
num=int(input("num "))
print(f"{num}, {1},{num} {num**2}, {num**3}")