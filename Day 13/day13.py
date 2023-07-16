#Working with Files
#
write_file = open("write_example.txt", "w")
write_file.write("Welcome to the world, write_example.txt!")

write_file.write("\nNow we have two lines!!")
write_file.close()


#
with open("example.txt", "r") as example_file:
   print(example_file.read())
    

#
with open("write_example.txt", "w") as write_file:
    write_file.write("hello world! I am learning python")



#
f = open("hello_world.txt", "w")
f.write("Hello, World!")
f.close()

#
with open("hello_world.txt", "a") as f:
    f.write("How are you?")