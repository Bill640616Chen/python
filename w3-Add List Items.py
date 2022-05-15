#https://www.w3schools.com/python/python_lists_add.asp
#Python Add List Items
#增加清單項目
#Append Items增加項目
#To add an item to the end of the list, use the append() method:
#要在清單末尾添加項目，請使用append()方法：
#Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #['apple', 'banana', 'cherry', 'orange']

#Insert Items
#To insert a list item at a specified index, use the insert() method.
#要在指定索引中插入清單項目，請使用insert()方法。
#The insert() method inserts an item at the specified index:
#The insert()方法在指定索引上插入項目：
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) #['apple', 'orange', 'banana', 'cherry']
#Note: As a result of the examples above, the lists will now contain 4 items.
#筆記: 由於上述示例，清單現在將包含 4 個項目。

#Extend List 擴展清單
#To append elements from another list to the current list, use the extend() method.
#要將元素從另一個清單附加到當前清單，請使用extend()方法。
#Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) 
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
#合併兩個清單,方法內的清單不見了,只留下.之前的清單
#基本上所有「.」之後的都是屬性。由於 Python 所有東西都是物件，
#所以取得某物件的屬性也可說是「從一個物件中取得附屬於該物件的另一個物件」。
#The elements will be added to the end of the list.
#這些元素將被添加到清單的末尾。

#Add Any Iterable 添加任何可反覆運算
#程式設計師解釋:迭代就是從一個集合物件中一個一個取出來
#將這個集合物件放入迭代處理時,就會取出元素,一直取到最後為止
#迭代指的是一個重複的過程，每次重複都必須基於上一次的結果而繼續
#迭代器協議中包含了2個最基本的概念，分別是可迭代物件和迭代器物件。
#可迭代物件（Iterable）：內部實現了__iter__()方法的物件則被稱為可迭代物件
#迭代器物件（Iterator）：內部實現了__next__()方法的物件則被稱之為迭代器物件
#https://iter01.com/599973.html
#The extend() method does not have to append lists, you can add 
# any iterable object (tuples, sets, dictionaries etc.).
#The extend()方法不必附加清單，您可以添加任何可重做物件（圖、集、字典等）。
#經過測試，所有的容器型別（list、tuple、str、dict、set、frozenset）
# 均屬於可迭代物件，但不屬於迭代器物件
#原子型別（bool、int、float、None）等均不屬於可迭代物件，
# 更不屬於迭代器物件。
#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#['apple', 'banana', 'cherry', 'kiwi', 'orange']

#以下測試
#用+號完成多個清單的合併
#https://www.jianshu.com/p/5c7a682130ad
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
tropical1 = ["mago", "ppple", "pya"]
newlist=thislist+tropical+tropical1
print(newlist) 
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya',
# 'mago', 'ppple', 'pya']
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.append(tropical)
print(thislist) 
#['apple', 'banana', 'cherry', ['mango', 'pineapple', 'papaya']]
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
newlist=thislist+list(thistuple) #清單與元組也可用+合併為清單
print(newlist) #['apple', 'banana', 'cherry', 'kiwi', 'orange']

mylist = ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya', 'mago', 'ppple', 'pya']
for item in mylist: #這個就是迭代處理
#迭代就是從一個集合物件中一個一個取出來
#for item in mylist:  先從mylist中取出第一個位置的值放入item裡
    print(item)
    #執行 print(item) 印出item，也就是apple
    #再回到 for item in mylist: 取出第二個位置的值放入item
    #執行 print(item) 印出item，也就是banana
    #直到取出最後的值並印出後，迭代就結束
    #apple
    #banana
    #cherry
    #mango
    #pineapple
    #papaya
    #mago
    #ppple
    #pya
