#slice
original_string = "Python"
sliced_string = original_string[0:3]
print(sliced_string)  # Pyt
#
sliced_string = original_string[:]
print(sliced_string)  

#len 
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5

#
no=["1","2","3","4","5"]
print("|".join(no))


#
base_numbers = [1, 2, 3, 4, 5]
processed_numbers = []

for number in base_numbers:
    processed_numbers.append(str(number))

print(" | ".join(processed_numbers))


#Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.
fullname=input("Enter your name and surname: ")
fname=(fullname.split())
print((fname))
firstname=fname[0]
print(firstname)
lastname=fname[1]
print(lastname)


#

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'" ]
for quote in quotes:
    print(quote.strip("'"))



#Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, so you’re going to have to process the string before you find its length.
word=input("Enter a word: ")
len(word.strip())
