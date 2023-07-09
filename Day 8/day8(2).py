#1
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for (character_name, voice_actor, species_of_character) in main_characters:
    print(f"{character_name} is a {(species_of_character).lower()} voiced by {voice_actor}")


#2
#Unpacking the tuple into 4 variables.
name, id_number, (major, minor) = ("John Smith", 11743, ("Computer Science", "Mathematics"))

#alternative
student = ("John Smith", 11743, ("Computer Science", "Mathematics"))
name, id_number, (major, minor) = student
print(student)

#
std_info=[("John Smith", 11743, ("Computer Science", "Mathematics"))]

for student_name, id_number, (major, minor) in student:
    print(f"{student_name}'s id number is:{id_number} with {major,minor} as major and minor discipline respectively.)") 

#3
#  Investigate what happens when you try to zip two iterables of different lengths. 
# For example, try to zip a list containing three items, and a tuples containing four items.
list_of_people=["Ram", "Shyam", "Hari"]
vehicle=("car", "bike", "cycle","onwalk")

print(list(zip(list_of_people,vehicle)))
