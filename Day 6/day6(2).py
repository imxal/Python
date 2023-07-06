movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

#Calculate the average budget of all movies in the data set.


budget = 0
count=len(movies)
for movie in movies:
    budget += float(movie[1])
   
    average=budget/count
    print(average)


#Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
for movie in movies:
    if(movie[1]>average):
        print(movie)
        over_average_cost=float(movie[1])-float(average)
        print(f"{movie[0]} cost ${movie[1]}: ${over_average_cost} over average.")







      




