#array, list
num = [1,2,3,4,5,6]
#list
letters = ['w', 'e', 't', 'c', 'a', 'z', 'n', 'c']
#tuple (multiple data type)
names = ('ram', 'sita', 'isha', 'shanvi', 'mata', (1,2,3), 'amar')
#dictionary key value pair
pairs = {'ram' : 'sita' , 'fruit': 'apple', 'flower':'rose', 1 : 3}

#create a new dict object with existing list or set
alph = 'kishore'
new_dict = dict.fromkeys(num, alph)

#ietrate over new_dict object
for a,b in new_dict.items():
    print (a,b)
for n in names:
    print (n)

# for i in num:
#     print (i)
# dict can be retrieved through items()
for k, v in pairs.items():
    print (k,v)

#enumerate can retrieve values with index 
for en in enumerate(names):
    print (en)
    
#zip is used to combine two objects and retrive the values
for x,y in zip(num, names):
    print (x, y)
    
#SORT THE ITEMS IN A LIST
sorted_letters = sorted(letters)
print (sorted_letters)

print (letters.count('c'))