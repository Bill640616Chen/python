#https://www.w3schools.com/python/python_lists_loop.asp
#Python Loop Lists 迴圈清單
#You can loop through the list items by using a for loop:
#您可以使用「迴圈」循環來循環清單項目：
#Print all items in the list, one by one:
#
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) #(清單的值依序放入到x裡頭)
  #apple
  #banana
  #cherry
#Learn more about for loops in our Python For Loops Chapter.
#瞭解更多關於迴圈在我們的 Python 迴圈章節。

print("------------(range))Loop Through the Index Numbers")
#Loop Through the Index Numbers
#迴圈瀏覽索引編號
#You can also loop through the list items by referring to their index number.
#您也可以通過引用其索引編號來循環瀏覽清單項目。
#Use the range() and len() functions to create a suitable iterable.
#使用range（） 和 len （） 功能創建合適的可迭代物件。
#經過測試，所有的容器型別（list、tuple、str、dict、set、frozenset）
# 均屬於可迭代物件，但不屬於迭代器物件
#原子型別（bool、int、float、None）等均不屬於可迭代物件，
# 更不屬於迭代器物件。
#Print all items by referring to their index number:
#靠著指定他們的索引號列印所有的項目
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  #apple
  #banana
  #cherry
print("------------len(thislist)測試")
print(len(thislist)) #3
#(function)功能 len長度: (__obj物件: Sized多長) ->輸出 int數字
#Return the number of items in a container.
print("------------range(0,10)測試")
print(range(0,1)) #range(0, 1)
#(class) range
#range(stop) -> range object range(start, stop[, step]) -> range object
#Return an object that produces a sequence of integers from start
#  (inclusive) to stop (exclusive) by step. range(i, j) produces
#  i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted!
#  range(4) produces 0, 1, 2, 3. These are exactly the valid indices
#  for a list of 4 elements. When step is given, it specifies the 
# increment (or decrement).
#類別） 範圍
#範圍（停止） - >範圍物件range(start, stop[, step])- >範圍物件
#將生成一系列整數的物件從開始（包含）返回到逐步停止（排他）。
# 範圍 （i， j） 產生 i， i+1， i+2， ...j-1。開始預設到 0，並省略停止！
# 範圍 （4） 產生 0， 1， 2， 3.這些正是列出清單裡 4 個元素的有效指數。
# 當給定步驟時，它指定增量（或減量）。
#The iterable created in the example above is [0, 1, 2].
#這可迭代物件在上述例子是[0, 1, 2](索引號碼)
#所以 for i in range(len(thislist)):
#len(thislist)：取得陣列內容的數量
#得到數量後， range(len(thislist)) 產生一個該數量的整數列表，如上例即為  range(3) 
#for i in range(len(thislist)): 就是 for i in range(3):
#for i in range(3): 就是 i 從 0 抓到2
#因此，後面的程式碼 print(thislist[i])，就是依序印出陣列裡的元素

print("------------While Loop")
#Using a While Loop
##http://tw.gitbook.net/python/python_while_loop.html
#while循環語句在Python編程語言中，只要給定的條件為真時重複執行的目標語句。
#You can loop through the list items by using a while loop.
#您可以使用while條件循環來循環清單項目。
#Use the len() function to determine the length of the list, 
# then start at 0 and loop your way through the list items by refering to their indexes.
#使用 len（） 功能確定清單的長度，然後從 0 開始，透過引用清單的索引
#來循環瀏覽清單項目。
#Remember to increase the index by 1 after each iteration.
#請記住，每次反覆運算後將索引增加 1。
#Print all items, using a while loop to go through all the index numbers
#列印所有項目，使用while迴圈來流覽所有索引數字
thislist = ["apple", "banana", "cherry"]
i = 0 # while的條件,i的起始值要設定
while i < len(thislist):
  print(thislist[i]) #輸出的結果跟for一樣
  i = i + 1 #條件是i要一直往上加到小於3為止

print("----Looping Using List Comprehension")
#Looping Using List Comprehension迴圈使用清單理解
#List Comprehension offers the shortest syntax for looping through lists:
#清單理解提供了循環瀏覽清單的最短語法：
#A short hand for loop that will print all items in a list:
#循環的簡短語句，將列印清單中的所有項目：
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#簡單語句需要有[]
