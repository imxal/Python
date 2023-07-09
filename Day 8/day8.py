# Unpacking, Enumeration, and the zip Function
movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]


for title, director, year in movies:
    print(f"{title} ({year}), by {director}")


#enumerator
names = ["Ross", "Rachel", "Monica"]

for counter, name in enumerate(names, start=1):
    print(f"{counter}. {name}")

#refrence to movies[] above
for counter, (title, director, year) in enumerate(movies, start=1):
    print(f"{counter}. {title} ({year}), by {director}")

#zip
pet_owners = ["Paul", "Soniya", "Miya"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

pets_and_owners = zip(pet_owners, pets)
print(list(pets_and_owners))

#using in loop
for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}.")


#-
movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]
#without list                             
movies = zip(movie_titles, movie_directors)
#o/p for print(f"There are {len(movies_list)} movies in the collection.") =>0

#with list
movies = list(zip(movie_titles, movie_directors))


for title, director in movies:
    print(f"{title} by {director}.")

movies_list = list(movies)

print(f"There are {len(movies_list)} movies in the collection.")
print(f"These are our movies: {movies_list}.")



