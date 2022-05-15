#https://www.w3schools.com/python/python_sets_remove.asp
#Python Remove Set Items 移除集合項目
#ARemove Item
#To remove an item in a set, use the remove(), or the discard() method.
print("-----------------Remove 香蕉 by using the remove() method:")
#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) #{'apple', 'cherry'}
#Note: If the item to remove does not exist, remove() will raise an error.

print("-----------------Remove 香蕉 by using the discard() method:")
#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #discard是丟棄
print(thisset) #{'apple', 'cherry'}
#Note: If the item to remove does not exist, discard() will NOT raise an error.

print("-----------------Remove 任意項目 by using the pop() method:")
#You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
#The return value of the pop() method is the removed item.
#Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #set使用pop()方法,()內不用參數,隨機移除
print(x) #apple 
print(thisset) #{'banana', 'cherry'}
#print(thisset.pop())輸出也有值
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

print("-----------------Remove by using the clear() method:變空集合")
#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #set()

print("------------------------Remove by using del set:set整個刪除")
#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #name 'thisset' is not defined