#nested functions are function calls inside function calls.
#innermost function gets resolved first,
#and the return value is used as argument for the next outer function.

#number = input("Enter a whole positive number: ")
#number = float(number)
#number = abs(number)
#number = round(number)
#print(number)

print(round(abs(float(input("Enter a whole positive number: ")))))