#https://www.w3schools.com/python/python_sets_access.asp
#Python Access Set Items 拜訪集合項目
#Access Items
#You cannot access items in a set by referring to an index or a key.
#您不能透過引用索引或key來訪問set中的項目。
#But you can loop through the set items using a for loop, or ask if a specified value 
# is present in a set, by using the in keyword.
#但是，您可以使用「迴圈」來迴圈通過set項目，或者使用關鍵字來詢問
# set是否存在指定值。
print("-----------------Loop through the set, and print the values:")
#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#apple
#cherry
#banana

print("-------------------------------------檢查項目是否存在於 set:")
#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) #判斷True

#Change Items
#Once a set is created, you cannot change its items, but you can add new items.
#當set被建立，你不能改變項目，但你可以新增一個項目。