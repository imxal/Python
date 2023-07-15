#Scope and Returning Values from Functions
def greet(name):
    greeting = f"Hello, {name}!"
    print(greeting)

greet("laxmi")

#
def exponentiate(a,b):
    result=a**b
    return result

exponentiate(2,3)


#
def process_string(word):
    conversion=word.strip().lower()
    return conversion
process_string("HAppy  ")

#
def actor_info(actors):
   return (f"{actors['name']} {actors['nationality']} {actors['age']}")
    
actor={
        "name":"Bipin", 
        "nationality": "Nepali", 
        "age":32
    }

actor_info(actor)

#   
def prime(dividend):
    for divisor in range(2, dividend):
         if(dividend % divisor == 0):
            return (f"{dividend} is a not prime number")
    
    return(f"{dividend} is a prime number")
    
prime(2)
    
