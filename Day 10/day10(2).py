#set

Empty_set= set()

Empty_set.update({"Name","Age","Address"})

print(Empty_set)


Another_set={"Name", "College", "Hobbies"}

Empty_set.union(Another_set)
Empty_set.intersection(Another_set)
Empty_set.symmetric_difference(Another_set)
Empty_set.difference(Another_set)



Num= range(0,50)
print(Num)
User_input=int(input("Enter any number: "))

if User_input in Num:

    print(f"Your choosen number {User_input} is within range.")
else:
    print(f"Your choosen number {User_input} is not within range.")


