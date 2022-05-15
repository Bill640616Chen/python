#https://www.w3schools.com/python/python_tuples_access.asp
#Python Access Tuple Items 訪問Tuple項目
#Access Tuple Items
#You can access tuple items by referring to the index number, 
# inside square brackets:
print("---------------------Print the second item in the tuple")
#Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #索引數字只能[]
#banana
#Note: The first item has index 0.第一個項目的索引值為 0

print("---------------Negative indexing means start from the end.")
#Negative Indexing
#Negative indexing means start from the end.
#-1 refers to the last item, -2 refers to the second last item etc.
#Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #cherry

print("-------------------------------------------Range of Indexes")
#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new tuple with the specified items.
#Note: The search will start at index 2 (included) and end at index 5 (not included).
#Remember that the first item has index 0.
#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple索引位置的值輸出[會:不會])
print(thistuple[2:5]) #('cherry', 'orange', 'kiwi')
print(thistuple[2:-2]) #('cherry', 'orange', 'kiwi')
print(thistuple[:-2]) #('apple', 'banana', 'cherry', 'orange', 'kiwi')
#索引位置取值的規則是由左至右
print(thistuple[-3:]) #('kiwi', 'melon', 'mango')
print(thistuple[-3:1]) #()索引位置取值的規則是由左至右
print(thistuple[-1:-3]) #()索引位置取值的規則是由左至右
print(thistuple[-1:])
#('mango',)索引位置取值的規則是由左至右,左邊的值沒得取,直接到-1的位置取值
print(thistuple[-5:-1]) #('cherry', 'orange', 'kiwi', 'melon')

print("-----------------要確定指定項目是否存在於 Tuple 中，請使用關鍵字")
#Check if Item Exists
#To determine if a specified item is present in a tuple use the in keyword:
#要確定指定項目是否存在於 Tuple 中，請使用關鍵字
#Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#Yes, 'apple' is in the fruits tuple