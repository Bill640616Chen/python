#https://www.w3schools.com/python/ref_set_remove.asp
#Python Set remove() Method 集合remove() 方法
#Removes the specified element
#移除指定的元素
#Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) #{'apple', 'cherry'}
#Definition and Usage
#The remove() method removes the specified element from the set.
#This method is different from the discard() method, because 
# the remove() method will raise an error if the specified 
# item does not exist, and the discard() method will not.
#這個方法跟discard()不同,因為remove()要移除的指定元素如果不存在
# 將會提升錯誤,但是discard()不會
#Syntax
#set.remove(item)
#Parameter Values
#Parameter：Description
#item：Required. The item to search for, and remove
fruits = {"apple", "banana", "cherry"}
fruits.discard("orange")
print(fruits) #{'banana', 'apple', 'cherry'}
fruits = {"apple", "banana", "cherry"}
fruits.remove("orange")
print(fruits) #KeyError: 'orange'
