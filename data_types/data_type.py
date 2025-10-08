# 2.1 Data type usage
# integer
my_int = 6
print (my_int)
type(my_int)
#float
my_float = 7.0
print (my_float)
type(my_float)
#string
my_string = "ayyo"
print (my_string)
type(my_string)
#boolean
my_bool = True
print (my_bool)
type(my_bool)
#nonetype
my_none = None
print (my_none)
type(my_none)
#list
my_list = [5, 4, 3, 2, 1]
print (my_list)
type(my_list)
#dictionary
my_dict = {"wow": "ayyo", "level": 5}
print (my_dict)
type(my_dict)
#tuple  
my_tuple = (1, 2, 3)
print (my_tuple)
type(my_tuple)
#set
my_set = {1, 2, 3, 4, 5}
print (my_set)
type(my_set)
#range
my_range = range(6)
print (my_range)
type(my_range)
# 2.2 Length command  example
#2.2.1
my_string = "it be like that sometimes"
len(my_string) #gives me the length
#2.2.2 Multi-way (If/elif/else clause)
x = 8
#scenario 1 
#first condition is true
if x >= 5 + 2:  #this is true
    print ("The integer could be positive")
elif x * 0 == 0:
    print ("The integer could be zero")
elif x/-4 <= 1:
    print ("The integer could be negative")
else:
    print ("I can't math")
#scenario 2 
#first condition gotta be false
if x >= 5 + 4: #this is false
    print ("The integer could be positive")
elif x * 0 == 0:
    print ("The integer could be zero")
elif x/-4 <= 1:
    print ("The integer could be negative")
else:
    print ("I can't math")
#scenario 3
#first 2 conditions gotta be false
if x >= 5 + 4: #this is false
    print ("The integer could be positive")
elif x + 0 == 0: #this is false
    print ("The integer could be zero")
elif x/-4 <= 1:
    print ("The integer could be negative")
else:
    print ("I can't math") 
#2.2.3 Type gate + nested classification (Nested If/elif/else)
my_range = range(6)
if type(my_range) is list or range or tuple :     #outer condition
    if len(my_range) == 0:
        print("empty")
    elif len(my_range) == 1:    #inner conditions run if outer condition is TRUE
        print("single item")
    elif len(my_range) > 1:
        print("multiple items")
else:
    print("wrong type for this task")   #outer condition
