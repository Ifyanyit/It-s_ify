#name = ""

#while len(name) == 0:
#    name = input("Enter your name:")
#print("Your name is", name)
#print("Your name has", (len(name)), "letters.")
#Or 

name = None
while not name:
    name = input("Enter your name: ")
print("Hello,", name)