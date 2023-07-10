#Dictionaries
(
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
 )



music_band = {
    "album_name":"The Dark Side of the Moon",
    "artist": "Pink Floyd",
    "release_year": 1973,
    "track_list" : ["Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"    ]
}

for key, value in music_band.items():
    print(f"{key}:{value}")

del music_band["track_list"]
del music_band["release_year"]

music_band.update({
    "release_year": "March 1st, 1973"
})


print(music_band)

print(music_band["track_list"])

print(music_band.get(("track_list")))