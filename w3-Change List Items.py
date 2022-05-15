#https://www.w3schools.com/python/python_lists_change.asp
#Python Change List Items
#Change Item Value 更改項目值
#To change the value of a specific item, refer to the index number:
#要更改特定項目的值，請指定索引編號：
#Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) #['apple', 'blackcurrant', 'cherry']

#Change a Range of Item Values
#To change the value of items within a specific range, define a 
# list with the new values, and refer to the range of index numbers 
# where you want to insert the new values:
#要更改特定範圍內的專案值，請使用新值定義清單，並參考要插入新值的索引數字範圍：
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) 
#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:4] = ["blackcurrant", "watermelon"]
#方法裡替換3個,但只有2個值
print(thislist) #位置1,2,3只取代2個值,第3個值就不見了
#['apple', 'blackcurrant', 'watermelon', 'kiwi', 'mango']
#如果插入的項目比替換的要少，則[1:4] = ["blackcurrant", "watermelon"]
#原來沒被取代位置的值自動刪除

#If you insert more items than you replace, the new items will be 
# inserted where you specified, and the remaining items will move
# accordingly:
#如果插入的項目比替換的要多，則新項目將在指定位置插入，其餘項目將相應移動：
#Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
#只替換位置1的值,然後再插入一個值
print(thislist) #['apple', 'blackcurrant', 'watermelon', 'cherry']
#Note: The length of the list will change when the number of items

#  inserted does not match the number of items replaced.
#當插入的項目數與替換的項目數量不匹配時，清單的長度將發生變化。
#If you insert less items than you replace, the new items will
# be inserted where you specified, and the remaining items will move accordingly:
#如果插入的項目少於您取代的項目，則新項目將在指定位置插入，其餘項目將相應移動：
#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]#取代位置1-2的值
print(thislist) #['apple', 'watermelon']

#Insert Items
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#要插入新清單項目，而無需替換任何現有值，我們可以使用insert()方法。
#The insert() method inserts an item at the specified index:
#The insert() 方法在指定索引上插入項目：
#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #在位置2前插入
print(thislist) #['apple', 'banana', 'watermelon', 'cherry']
#Note: As a result of the example above, the list will now contain 4 items.
#筆記: 由於上表，該列表現在將包含 4 個項目。
#下面測試
thislist = ["apple", "banana", "cherry"]
thislist.insert(-1, "watermelon") #在位置-1前插入
print(thislist)#['apple', 'banana', 'watermelon', 'cherry']
thislist = ["apple", "banana", "cherry"]
thislist.insert(3, "watermelon") #在位置3前插入
print(thislist) #['apple', 'banana', 'cherry', 'watermelon']
thislist = ["apple", "banana", "cherry"]
thislist.insert(4, "watermelon") #在位置4前插入,位置2後的位置都可插入
print(thislist) #['apple', 'banana', 'cherry', 'watermelon']
thislist = ["apple", "banana", "cherry"]
thislist.insert(-4, "watermelon") #在位置-4前插入,位置-3前的位置都可插入
print(thislist) #['watermelon', 'apple', 'banana', 'cherry']