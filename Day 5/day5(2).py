#join
numbers=[1,2,3,4,5]
stringified_numbers= []
for num in numbers:
    stringified_numbers.append(str(num))
print(','.join(stringified_numbers))   


project_authors = ["Mike", "Sofia", "Helen"]
print(f"The people who worked on this project are: {','.join(project_authors)}")
print(f"The people who worked on this project are: {(project_authors)}")
print(f"The people who worked on this project are: {'-'.join(project_authors)}")



#split
user_numbers = input("Please enter 5 numbers separated by commas: ") 
numbers_list = user_numbers.split(",")
print(numbers_list) 

user_numbers = input("Please enter 5 numbers separated by dash: ") 
numbers_list = user_numbers.split("-")
print(numbers_list) 

numbers="1,2,3,4,5,6"
print(numbers.split(','))

sample_string = "Python"


#If we just want to put every character as a different item in a list or tuple, we can just pass the string to the list or tuple function instead:
sample_string = "Python"
print(list(sample_string)) # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(sample_string)) # ('P', 'y', 't', 'h', 'o', 'n')


#The newline character
print("My name is Laxmi.\nI am learning Python ")
print("My name is Laxmi.\n\n I am learning Python ")





