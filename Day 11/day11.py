#function
#Addition
def add_numbers(a,b):
    sum=a+b
    print(sum)

add_numbers(4,5)

#subtraction
def sub(a,b):
    diff=a-b
    print(diff)

sub(4,5)

#multiply
def mul(a,b):
    multiply=a*b
    print(multiply)

mul(4,5)

#Division
def divide(a, b):
    if b == 0:
        print("You can't divide by 0!")
    else:
        print(a / b)

divide(20,0)

#
def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} season(s)")

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}

print_show_info(tv_show)

#
def print_show_info(show):
        
            print(f"{show['title']} {show['seasons']} {show['initial_release']}")

series =[ {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
 ]

for show in series:
 print_show_info(show)

#palindrome
def palindrome_check(word):
     word=word.strip().lower()
     reverse_word=(reversed(word))
     if (list(word) == list(reverse_word)):
          print(f"{word} is palindrome word.")
     else:
          print(f"{word} is not palindrome")

palindrome_check("Hannah")



#alternative
def is_palindrome(word):
    word = word.strip().lower()

    if word == word[::-1]: #[::-1]=> give me the whole sequence in reverse order
        print(True)
    else:
        print(False)

is_palindrome("Hannah")  # True
is_palindrome("Fred")    # False
