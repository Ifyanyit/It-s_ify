# Tuple = lists that is ordered and can not be changed. It is used to group together related data.

student = ("Ifeanyi", "Male", "31", "Year 2", "Industrial Maths")

print(student.count("Male"))   #Counts how many times an item appeared in the tuple
print(student.index("Ifeanyi"))  #finds the indext of an Item


for x in student:
    print(x)

if "Year 2" in student:
    print("A year 2 student")
