#slicing string means extracting elements or letters from a string.
#  indexing method uses []
#  slicing method uses ()
# contains three parts [start:stop:step]

# indexing method

name = "Ngene Ifeanyi"

surname = name[0:5]  # Or name[:5] , 0 is inclusive and 5 is exclusive
print(surname)

first_name = name[6:13]  # Or name[6:], prints everything after index 6.
print(first_name)

funky_name = name[0:13:2]  # Or name[::2], skips second letters
print(funky_name)

#slice  cutting a part of string

website = "https://google.com"

webname = slice(8,-4)  #prints only google
print(website[webname])  