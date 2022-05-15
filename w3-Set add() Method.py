#https://www.w3schools.com/python/ref_set_add.asp
#Python Set add() Method 集合add()方法
#Add an element to the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits.add("orange")) #None
print(fruits) #{'banana', 'apple', 'cherry', 'orange'}
#Definition and Usage
#The add() method adds an element to the set.
#If the element already exists, the add() method does not add the element.
#Syntax
#set.add(elmnt)
#Parameter：Values
#Parameter：Description
#elmnt：Required. The element to add to the set
#Try to add an element that already exists:
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits) #{'cherry', 'banana', 'apple'}
