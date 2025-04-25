
sentence = "This is Python Tutorial"
strr = input("Enter the string")

if strr in sentence:
    print (strr, " string present")
else:
    print (strr, " not present")

#check the string endswith    
if sentence.endswith("Tutorial"):
    print (True)
else:
    print (False)
    
str = "Aeropostale"

#centre a string within given width of characters and replace empty with *
print (str.center(20, '*'))

#count number of strings
world = "Hello world, this is python world, cruel world" 
print (world.count('world'))
#count number of string occurrances starting from 5 to 20
print (world.count('world', 5,20))

#find string function will give the index of the string in the given string
print(world.find('this'))