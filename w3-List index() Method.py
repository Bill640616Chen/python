#https://www.w3schools.com/python/ref_list_index.asp
#Python List List index() Method 清單索引方法
#What is the position of the value "cherry":
#value「櫻桃」的位置是什麼？
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x) #索引位置為2
#Definition and Usage
#The index() method returns the position at the first occurrence of the specified value.

#Syntax
#list.index(elmnt)(元素)
#Parameter Values
#Parameter(參數)：Description(描述)
#elmnt(元素)：Required(必填). Any type (string, number, list, etc.).
# The element to search for
#What is the position of the value 32:
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x) #都是從左往右點,所以32在位置3
#Note: The index() method only returns the first occurrence of the value.
