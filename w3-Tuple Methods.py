#https://www.w3schools.com/python/python_tuples_methods.asp
#Python Tuple Methods Tuple方法
#Returns the number of times a specified value occurs in a tuple
#https://www.w3schools.com/python/ref_tuple_count.asp
print("---------------------------------------Tuple count() Method")
#Tuple count() Method
#Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x) #2
print(thistuple.count(5)) #2,count在print是帶值的
#Definition and Usage
#The count() method returns the number of times a specified value appears in the tuple.

#Syntax
#tuple.count(value)
#Parameter：Values
#Parameter：Description
#value：Required. The item to search for

print("---------------------------------------Tuple index() Method")
#https://www.w3schools.com/python/ref_tuple_index.asp
#Tuple index() Method
#Search for the first occurrence of the value 8, and return its position:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x) #3
print(thistuple.index(8)) #3,index在print是帶值的
#Definition and Usage
#The index() method finds the first occurrence of the specified value.
#The index() method raises an exception if the value is not found.
#例外：tuple.index(x): x not in tuple
#Syntax
#tuple.index(value)
#Parameter：Values
#Parameter：Description
#value：Required. The item to search for