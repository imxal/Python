#reading files

employee_file = open("employess.txt", "r")

#different ways of reading files
print(employee_file.readable())

print(employee_file.read())

print(employee_file.readline())

print(employee_file.readlines())

print(employee_file.readlines()[1])



for employee in employee_file.readlines():
    print(employee)

employee_file.close()




