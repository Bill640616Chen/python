#https://www.w3schools.com/python/python_for_loops.asp
#Python Loop for Lists 迴圈for清單
#A for loop is used for iterating over a sequence (that is either a 
# list, a tuple, a dictionary, a set, or a string).
#for循環用於在序列中迭代,（即清單、tuple、字典、set或字串）。
#This is less like the for keyword in other programming languages, 
# and works more like an iterator method as found in other 
# object-orientated programming languages.
#這不像其他程式設計語言中的關鍵字，並且工作方式更像其他對象導向程式設計
# 語言中的迭代器方法。
#With the for loop we can execute a set of statements, once for 
# each item in a list, tuple, set etc.
#對於迴圈，我們可以執行一組語句，一次針對清單中的每個項目、tuple、集合等。
#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  #apple
  #banana
  #cherry
#The for loop does not require an indexing variable to set beforehand.
#for迴圈不需要事先設置索引變數。

print("------------------循環通過字串")
#Looping Through a String
#循環通過字串
#Even strings are iterable objects, they contain a sequence of characters:
#即使是字串是可迭代的物件，它們也包含一序列的字元：
#Loop through the letters in the word "banana":
for x in "banana": #"banana"是一個序列也是有可迭代性的字串
  print(x) #輸出為每個字母,垂直呈現

#The break Statement
#中斷的陳述
#With the break statement we can stop the loop before it has looped through all the items:
#通過中斷陳述,我們可以在它已經迴圈過所有項目前停止迴圈
#Exit the loop when x is "banana":
#當x is "banana"時,離開迴圈
print("------------------break在print之後")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #先代入輸出
  if x == "banana":
    break #如果代入x的值是"banana"就中斷迴圈,但輸出在條件式之前
    #apple
    #banana
print("-----------測試執行迴圈的順序-1")
#Exit the loop when x is "banana", but this time the break comes before the print:
#當 x 是「香蕉」時退出迴圈，但這次中斷在列印之前：
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": 
    break          
  print(x) #apple
#執行for迴圈
#x取fruits第一個值apple
#x不等於banana,沒被中斷
#輸出x的值(此時x的值為apple)
#x取fruits第二個值banana
#x等於banana,立刻被中斷for迴圈,沒法輸出
  #如果把print(x)縮排在條件式裡,是無法執行的

print("---------------測試執行迴圈的順序-2")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": 
    break           
print(x) 
#執行for迴圈
#x取fruits第一個值apple
#判斷x不等於banana,繼續取值
#x取fruits第二個值banana
#判斷x等於banana
#中斷for迴圈
#繼續執行程式print輸出x(此時x的值為banana)


print("------------------continue Statement")
#The continue Statement
#繼續的陳述
#With the continue statement we can stop the current iteration 
# of the loop, and continue with the next:
#通過繼續陳述，我們可以停止迴圈的當前的迭代，並繼續下一個：
#Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#apple
#cherry

print("------------------The range(x) Function")
#To loop through a set of code a specified number of times,
#  we can use the range() function,
#要迴圈流覽一組代碼的指定次數，我們可以使用range（） 功能，
#The range() function returns a sequence of numbers, starting
# from 0 by default, and increments by 1 (by default), 
# and ends at a specified number.
#range（）功能返回一系列數位，從預設值的 0 開始，以 1（預設情況下）
# 為增量，以指定數字結束。
#Using the range() function:
for x in range(6):
  print(x)
#Note:that range(6) is not the values of 0 to 6, 
# but the values 0 to 5.
print("------------------The range(start,end) Function")
#The range() function defaults to 0 as a starting value, 
# however it is possible to specify the starting value 
# by adding a parameter: range(2, 6), which means values 
# from 2 to 6 (but not including 6):
#Using the start parameter:
for x in range(2, 6):
  print(x)
print("------------------The range(start,end,step) Function")
#The range() function defaults to increment the sequence by 1, 
# however it is possible to specify the increment value by 
# adding a third parameter: range(2, 30, 3):
#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

print("------------------Else in For Loop-1")
#Else in For Loop
#Else在迴圈裡
#The else keyword in a for loop specifies a block of code to 
# be executed when the loop is finished:
#循環中的其他關鍵字指定了在迴圈完成時要執行的代碼塊：
#Print all numbers from 0 to 5, and print a message
# when the loop has ended:
for x in range(6): #迴圈執行
  print(x)
else:
  print("Finally finished!") #code block

print("------------------Else in For Loop-2")
#Note: The else block will NOT be executed if the loop is 
# stopped by a break statement.
#else block將不會被執行，如果迴圈在break陳述裡停止
#Break the loop when x is 3, and see what happens with the
# else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") #迴圈執行到最後時,要執行的動作

print("------------------Nested Loops")
#Nested Loops 嵌套迴圈
#A nested loop is a loop inside a loop.
#迴圈中的迴圈
#The "inner loop" will be executed one time for each iteration of the "outer loop":
#"內迴圈"將執行一次,對於「外迴圈」的每個迭代(反覆運算)
#先執行外部迴圈再執行內部迴圈
#Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

print("------------------pass Statement")
#The pass Statement 通過陳述
#for loops cannot be empty, but if you for some reason have a 
# for loop with no content, put in the pass statement to 
# avoid getting an error.
#對於迴圈不能是空的，但如果您出於某種原因有一個沒有內容的迴圈，
# 請放在通過陳述中以避免出錯。
for x in [0, 1, 2]:
  pass #因為pass,變空迴圈
#https://www.w3schools.com/python/ref_keyword_pass.asp
#pass Statement的連結
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
print(range(0,10)) #range(0, 1)
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

