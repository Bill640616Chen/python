#https://www.w3schools.com/python/python_sets_add.asp
#Python Add Set Items 增加集合項目
#Add Items
#Once a set is created, you cannot change its items, but you can add new items.
#To add one item to a set use the add() method.
print("-----------------Add an item to a set, using the add() method")
#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset) #{'banana', 'apple', 'cherry', 'orange'}
print("---------------------------------------------set可以轉換成list")
print(list(thisset)) #['cherry', 'apple', 'banana', 'orange']
print("---------------------------------------------list可以轉換成set")
thislist = ["apple", "banana", "cherry"]
print(set(thislist)) #{'cherry', 'apple', 'banana'}
#Add Sets
#To add items from another set into the current set, use the update() method.
#要將另一set中的項目添加到當前set中，請使用update()方法。
print("-----Add elements from tropical into thisset:請使用update()方法")
#Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #排列完全無序,２個set並沒辦法用運算子＋合併
#{'cherry', 'mango', 'pineapple', 'papaya', 'apple', 'banana'}
#Add Any Iterable 添加任何可迭代
#The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.).
#更新（）方法中的物件不必是一個set，它可以是任何可迭代物件
# （tuples, lists, dictionaries等）。
print("----------Add elements of a list to at set:請使用update()方法")
#Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist) #用update把list加人set裡
print(thisset)
#{'apple', 'cherry', 'kiwi', 'banana', 'orange'}

