#import random

#number = random.randint(-5,11)
#if number > 0:
   # print(number, "is positive.")
#elif number == 0:
  #  print(number, "is zero.")
#else:
    #print(number, "is negative")

import random
number = random.randint(-10, 10)
if number > 0:
    print("{:d} is positive".format(number))
elif number == 0:
    print("{:d} is zero".format(number))
else:
    print("{:d} is negative".format(number))