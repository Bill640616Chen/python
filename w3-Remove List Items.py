#https://www.w3schools.com/python/python_lists_remove.asp
#Python Remove List Items 移除清單的項目
#Remove Specified Item 刪除指定項目
#The remove() method removes the specified item.
#The remove()方法刪除指定專案。
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #['apple', 'cherry']

#Remove Specified Index 移除指定的索引
#The pop() method removes the specified index.
#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) #['apple', 'cherry']

#If you do not specify the index, the pop() method removes the last item.
#如果沒有指定索引,the pop()方法會移除最後一個項目
#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) #['apple', 'banana']

#The del keyword also removes the specified index:
#del關鍵字也可以移除指定的索引
#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) #['banana', 'cherry']
#The del keyword can also delete the list completely.
#del關鍵字也可以刪除整個清單
#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist #清單移除了,所以輸出什麼都沒看到

#Clear the List
#The clear() method empties the list.
#clear()方法,清空清單內容
#The list still remains, but it has no content.
#清單還是存在,但是裡面沒內容
#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear() #()裡面不能有值
print(thislist) #[]空清單