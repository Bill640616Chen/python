#https://www.w3schools.com/python/ref_set_discard.asp
#Python Set discard() Method 集合discard() Method方法
#Remove "banana" from the set:
#直接移除集合裡的項目
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) #{'apple', 'cherry'}
#print(fruits.discard("banana")) #None,不會傳回值
#Definition and Usage
#The discard() method removes the specified item from the set.
#discard() method從集合裡移除指定的項目
#This method is different from the remove() method, because 
# the remove() method will raise an error if the specified item 
# does not exist, and the discard() method will not.
#這個方法不同於remove() method,因為remove() method當指定項目不存在時,
# 將會提高錯誤,但是discard() method將不會造成錯誤
fruits = {"apple", "banana", "cherry"}
fruits.discard("orange")
print(fruits) #{'apple', 'cherry', 'banana'}
fruits.remove("orange")
print(fruits) #KeyError: 'orange'
#fruits.remove()
#Remove an element from a set; it must be a member.
#If the element is not a member, raise a KeyError.
#fruits.discard()
#Remove an element from a set if it is a member.
#If the element is not a member, do nothing.

#Syntax
#set.discard(value)
#Parameter：Values
#Parameter：Description
#value：Required. The item to search for, and remove