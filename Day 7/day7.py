#Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.
target_number = 50

guess = int(input("Enter a number: "))

while guess != target_number:
    print("Wrong!")
    guess = int(input("Enter a number: "))

print("You guessed correctly!")


#Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
sample_string = "Python"

for character in sample_string:
    if character == "o":
        continue

    print(character)



#Create a program that prints out every prime number between 1 and 100.
for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        print(dividend)

#alternative way 
primes = []

for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(str(dividend))

print(", ".join(primes))




