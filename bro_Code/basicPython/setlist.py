#set = a collection which is unordered,unindexed and has no duplicate value.

from xdrlib import Packer


utensils = {"fork","spoon", "knife","tray"}

#utensils.add("packer")
#utensils.remove("packer")

#for i in utensils:
   # print(i)

dishes = {"plate", "cup","bowl","tray"}

#utensils.update(dishes)
#print(utensils)
#for i in utensils:
    #print(i, end=" ")

dinner_table = utensils.union(dishes)
#print(dinner_table)
for i in dinner_table:
    print(i, end=" ")
print("\n")
print(utensils.difference(dishes))
print(utensils.intersection(dishes))
print(utensils.symmetric_difference(dishes))