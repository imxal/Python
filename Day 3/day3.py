#lists and tuples

names = ["John", "Alice", "Sarah", "George"]
print(names[1])  # George


names = ("John", "Alice", "Sarah", "George")
print(names[1])  # George


#Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie.
movies =[
    ("Katha", "Sushant", '2023')
    ]

#Use the input function to gather information about another movie. You need a title, director’s name, release year.
Movie=input("Movie: ")
Director=input("Director: ")
R_year=input("R_year: ")

#Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
movies_collection=(Movie, Director, R_year)
print(movies_collection)

#Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"{movies_collection[0]} {movies_collection[2]}")

#Add the new movie tuple to the movies collection using append.
movies.append(movies_collection)

#print 
print(movies[0])
print(movies[1])

#remove
movies.remove(movies[0])
del movies[0]

print(movies)

