#https://www.w3schools.com/python/python_lists_access.asp
#Python Access List Items
#訪問清單項目
#Access Items訪問項目
#List items are indexed and you can access them by referring to 
# the index number:
#清單項目已編入索引，您可以通過引用索引編號訪問它們：
#Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana
#Note: The first item has index 0. 第一個項目的索引值為0
#Negative Indexing負數索引
#Negative indexing means start from the end
#負數索引意思是從末端開始
#-1 refers to the last item, -2 refers to the second last item etc.
#-1是指最後一個項目,-2是指到數第二個項目,依此類推
#Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #cherry
#Range of Indexes索引範圍
#You can specify a range of indexes by specifying where to start 
# and where to end the range.
#您可以通過指定開始的位置和結束範圍的位置來指定一系列索引。
#When specifying a range, the return value will be a new list with
# the specified items.
#指定範圍時，返回值將是帶有指定項目的新清單。
#Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #['cherry', 'orange', 'kiwi'] 位置5不算進去
#Note: The search will start at index 2 (included) 
# and end at index 5 (not included).
#搜索將從索引 2（包括在內）開始，以索引 5 結束（不包括在內）。
#Remember that the first item has index 0.
#請記住，第一個項目有索引位置為 0。

#By leaving out the start value, the range will start at the first
# tem:
#將起始值排除在外，範圍將從第一個項目開始：是指方法不用指定起始的位置[:4]
#This example returns the items from the beginning to, but NOT 
# including, "kiwi":
#此範例傳回從開始到未包括「kiwi」的所有項目：
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon"
, "mango"]
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']

#By leaving out the end value, the range will go on to the end of 
# the list:
#將最終價值排除在外，範圍將進入清單的末尾：是指方法不用指定起始的位置[2:]
#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon",
 "mango"]
#print(thistuple索引位置的值輸出[會:不會])
#若[有索引位置參數:無參數],則最右位置的值會輸出
print(thislist[2:]) #['cherry', 'orange', 'kiwi', 'melon', 'mango']
#以下為測試
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:-1]) #['cherry', 'orange', 'kiwi', 'melon']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[4:-3]) #[]這兩位置正好重疊
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-1:2]) #[]索引位置取值的規則是由左至右
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[3:-3]) #['orange']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-1:-3]) #[]索引位置取值的規則是由左至右
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-3:-1]) #['kiwi', 'melon']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-1:]) #['mango']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:-3]) #['apple', 'banana', 'cherry', 'orange']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[::2]) #['apple', 'cherry', 'kiwi', 'mango']0,2,4,6
#[start:end:step]