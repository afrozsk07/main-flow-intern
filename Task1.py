# Operations on python Lists

# Creation of a List in Python

# Creating an empty List
empty_List = []
print(empty_List)

# Creating a List containing items of different data types
List = [1, "Interviewbit", 9.5, 'D']
print(List)

# Creating a nested List
nested_List = [[6, 2, 8], [1, "Interviewbit", 3.5], "preparation"]
print(nested_List)

# Accessing list elements

# using positive Index
print(List[0])
print(List[3])

# using negative Index
print(List[-4])
print(List[-1])

# Add/Change elements in list

vowels = ['a', 'e']
print(vowels)
# Appending an element in list
vowels.append('i')
print(vowels)
# Extending an element in list
vowels.extend(['o', 'u'])
print(vowels)

# Deleting/Removing items from the List.
my_List = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_List)
# Deleting/Removing a single item from the list
del my_List[3]
print(my_List)

# Concatenating two python lists

List1 = [1, 2, 3, 4] 
List2 = [5, 6, 7, 8]
concat_List = List1 + List2
print(concat_List)

# Slicing python list

my_List = ['i', 'n', 't', 'v', 'i', 'e', 'w', 'b', 'i', 't']
# Accessing elements from index beginning to 5th index
print(my_List[:6])
# Accessing elements from index 3 to 6
print(my_List[3:7])
# Accessing elements from index 5 to end
print(my_List[5:])
# Accessing elements from beginning to end
print(my_List[:])
# Accessing elements from beginning to 4th index
print(my_List[:-6])

# Operations on python Dictionarys
# Accessing the specific key from the dictionary
my_dict = {'name': 'John', 'age': 30}
print(my_dict.get('name'))
print(my_dict.get('address', 'Not Found'))

# Returns a list of all the keys and values in the dictionary
my_dict = {'name': 'John', 'age': 30}
print(my_dict.keys())
print(my_dict.values())

# return a list of all key-value pairs in the dictionary
my_dict = {'name': 'John', 'age': 30}
print(my_dict.items())

# Updating the list  key-value pairs to a dictionary 
my_dict = {'name': 'John', 'age': 30}
my_dict.update({'age': 31, 'address': '123 Street'})
print(my_dict)

# Removing the list key-value pair from a dictionary
my_dict = {'name': 'John', 'age': 30, 'address': '123 Street'}
removed_value = my_dict.pop('address')
print(removed_value)
print(my_dict)

# Returns the last key-value pair added to the dictionary
my_dict = {'name': 'John', 'age': 30, 'address': '123 Street'}
removed_pair = my_dict.popitem()
print(removed_pair)
print(my_dict)

# Operations on python Tuples

# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple) 

# Accessing Elements in a Python Tuple and Indexing
tempTuple = ('hello', 1, 2, 3)
print(tempTuple[0]) # prints first element of the tuple
print(tempTuple[3]) # prints last element of the tuple
# print(tempTuple[4]) # error

# Nested Python Tuple Accessibility
nestedTuple = ('hello', [1 ,2, 3], (4, 5, 6))
print(nestedTuple[0][2])
print(nestedTuple[2][2])

# Accessing Via Negative Indices
tempTuple = ('A', 'B', 'C', 'D.', 'E', 'F', 'G', 'H')
print(tempTuple[2]) # C
print(tempTuple[-6]) # C

# Updating Tuples in Python
tempTuple = ('Welcome', 'to', 'interview', 'bit.', 'Have', 'a', 'great', 'day', [1, 2, 3])
# tempTuple[0] = 'Hello' # throws type error
tempTuple[8].append(4) # appending a new integer 
# Printing the list at 8th index in the tuple
print(tempTuple[8]) 
tempTuple[8].pop(3) # popping element 
# Printing the list at 8th index in the tuple
print(tempTuple[8]) # OUTPUT: [1, 2, 3]
tempTuple = (1, 2, 3) # Assigning tuple all over again
print(tempTuple) 

# Slicing python Tuple
temptuple =  ("Welcome", "to", "interview", "bit.", "Have", "a", "great", "day")
tuple1 = temptuple[::] # fetching complete tuple
print("tuple1:", tuple1)
tuple2 = temptuple[0 : 6] # fetching tuple from 0th index to 6th index
print("tuple2:", tuple2)
tuple3 = temptuple[:: 3] # jumping every third element from start to end
print("tuple3:", tuple3) 
tuple4 = temptuple[1:5:2] # jumping to every 2nd element starting from 1st index until 5th index
print("tuple4:", tuple4) 
tuple5 = temptuple[-8:-5] # 8th index from end to 5th index from end
print("tuple5:", tuple5) 
tuple6 = temptuple[::-3] # jumping every 3rd element in reverse
print("tuple6:", tuple6) 
tuple7 = temptuple[-7:-3:2] # alternate implementation of tuple4
print("tuple7:", tuple7)

# conditional statements 
#if statement
a=True
if a: 
	print("a is True") 
print("Program ended") 

#if-else statement
a=100
b=200
print(a if a>b else b)
print("Program ended") 

# if..else chain statement 
x= "a"
if x== "b": 
	print("letter is b") 
else: 
	if x== "c": 
		print("letter is c") 
	else: 
		if x== "a": 
			print("letter is a") 
		else: 
			print("letter isn't a,b and c") 

# if-elif statement example 
y = "b"

if y== "b": 
	print("letter is b") 

elif y== "c": 
	print("letter is C") 

elif y== "a": 
	print("letter is A") 

else: 
	print("letter isn't a,b or c") 

# Python lambda expression
a, b = 10, 20
print ("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")

# Other operations on data

# Arithmetic operations 
a = 15
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# Manipulation of strings

# Eliminating Unnecessary Character of a String
text = "!!!Hello, World!!!"  
clean_text = text.strip("!")  
print(clean_text) 

# Dividing a string into multiple substrings 
text = "Hello world, how are you today?"  
words = text.split()  
print(words) 

# Concatenate Strings
string1 = "Hello"  
string2 = "world"  
result = string1 + " " + string2  
print(result)
