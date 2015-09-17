name = input("Please enter a pet's name: ")
print(name)
madlib = name
madlib += " ate a bunch of "
madlib += input("Enter a food: ")
madlib += " and got a case of "
madlib += input("Enter and illness: ")
madlib += ".  \nAfter several hours, {} had a full recovery." .format(name)


print(madlib)