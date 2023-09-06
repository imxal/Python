#Comprehensions
names = ["mary", "SteVe", "Noah", "KATE"]
names=[name.title() for name in names]
print(names)


names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)
people = [(name.title(), age) for name, age in zip(names, ages)]
print(people)

#set comprehension
#The internal structure of the comprehension is identical to the list comprehension, we just need to surround everything in curly braces, rather than square brackets.
names = ["mary", "Richard", "Noah", "KATE"]
names = {name.title() for name in names}


#Dictionary comprehensions
student_ids = (112343, 134555, 113826, 124888)
names = ("mary", "Richard", "Noah", "KATE")

students = {
    student_id: name.title()
    for student_id, name in zip(student_ids, names)
}
print(students)


#-----------------------------------------------
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)



#-----------------------
movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

movie = {key: value.title() for key, value in movie.items()}
print(movie)



