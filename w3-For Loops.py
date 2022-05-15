#https://www.w3schools.com/python/python_for_loops.asp
#Python For Loops 
#Python For Loops
#A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set, 
# or a string).
#for迴圈用在超過一個序列上反覆運算(要嘛是a list, a tuple, 
# a dictionary, a set, or a string)
#This is less like the for keyword in other programming
# languages, and works more like an iterator method as
# found in other object-orientated programming languages.
#這不像其他程式設計語言中的for關鍵字，並且工作方式更像其他物件
#導向程式設計語言中的傳譯器方法。
#With the for loop we can execute a set of statements, 
# once for each item in a list, tuple, set etc.
#對於迴圈，我們可以執行一組語句，一次為a list, tuple, set 
# etc.每個項目
#Print each fruit in a fruit list:
print("-------------------------------迴圈清單")
#在清單中輸出每個水果
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#The for loop does not require an indexing variable to set beforehand.
#for迴圈不需要事先設置索引變數

print("-------------------------------迴圈字串")
#Looping Through a String 迴圈字串
#Even strings are iterable objects, they contain a sequence of characters:
#字串也是可迭代物件,是含有字元的序列
#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

print("--------------------------print在迴圈裡,在berak前面")
#The break Statement 中斷陳述式
#With the break statement we can stop the loop before it has looped through all the items:
#在迴圈所有項目之前,我們可以使用break陳述式停止迴圈
#Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("--------------------------print在迴圈裡,在berak後面")
#Exit the loop when x is "banana", but this time the break 
# comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#先由apple代入x,然後判斷有沒有等於banana
#判斷為沒有,跳過中斷,因為print(x)在迴圈裡,執行print(x)
#再來banana代入x,然後判斷有沒有等於banana  
#判斷為有等於,就執行break跳出迴圈
print("------------------------print在迴圈外面,在berak後面")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
print(x)
#當print(x)在迴圈外面時,x要完全跑完迴圈(到break算完整)
#x才有值給print(x)輸出
print("------------------------print在迴圈外面,在berak前面")
fruits = ["apple", "banana", "cherry"]
print(x)
for x in fruits:
  if x == "banana":
    break
#67行print(x)沒有值,當apple進入迴圈,先代入for的x
#判斷不等於,跳出迴圈,換banana進入迴圈,先代入for的x
#判斷等於,中斷迴圈,for的x值直接給65行print(x)輸出
#當print(x)在迴圈外面時,x要完全跑完迴圈(到break算完整)
#x才有值給print(x)輸出

print("------------------The range() Function 範圍（） 功能")
#The range() Function 範圍（） 功能
#To loop through a set of code a specified number of times,
# we can use the range() function,
#要迴圈流覽一組代碼的指定次數，我們可以使用range （） 功能，
#The range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1 
# (by default), and ends at a specified number.
#range（）功能返回一系列數位，從預設值的 0 開始，以 1
# （預設情況下）為增量，以指定數字結束。
#Using the range() function:
for x in range(6):
  print(x)
  #6是指定結束的數字,所以輸出不會有
#Note：that range(6) is not the values of 0 to 6,
# but the values 0 to 5.
print("------------------The range(),()裡可以設定起始,結束)")
#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
#Using the start parameter:
for x in range(2, 6):
  print(x)
print("--------------The range(),()裡可以設定起始,結束,增量)")
#The range() function defaults to increment the sequence by 1
# , however it is possible to specify the increment value by 
# adding a third parameter: range(2, 30, 3):
#range()功能預設的序列增量為1,然後也可以
# 定增量range(起始,結束,增量)
#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)
#range(2, 30, 3)=range(起始,結束,增量)

print("--Else in For Loop,當迴圈完成了,指定一個程式碼區塊要執行")
#Else in For Loop
#The else keyword in a for loop specifies a block of code 
# to be executed when the loop is finished:
#else關鍵字在for迴圈,當迴圈完成了,指定一個程式碼區塊要執行
#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:#迴圈完成後,指定一個程式碼區塊要執行
  print("Finally finished!")
print("-----如果迴圈因為break停止迴圈了,else block將不會被執行")
#Note: The else block will NOT be executed if the loop is stopped by a break statement.
#筆記：如果迴圈因為break停止迴圈了,else block將不會被執行
#Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print("---迴圈中的迴圈,外圈跑第一次後,進入內圈跑完,才跳出換外圈")
#Nested Loops
#迴圈中的迴圈,外圈跑第一次後,進入內圈跑完,才跳出換外圈
#A nested loop is a loop inside a loop.
#嵌套迴圈是迴圈內的迴圈
#The "inner loop" will be executed one time for each iteration of the "outer loop":
#"內迴圈"將被執行一次對於"外迴圈"的每個反覆運算：
#Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
#x取了第一個值後,接著到內迴圈,y取值,要等到y取完所有值後
#y取值後,就會與x進入print(x,y)輸出
#才會回到外迴圈,進行x取第二個值,再進入內迴圈,y取值,
# 等到y取完所有值後
#每一次y取值後,就會與x進入print(x,y)輸出
#才會回到外迴圈,進行x取第三個值,再進入內迴圈,y取值,
# 等到y取完所有值後
#每一次y取值後,就會與x進入print(x,y)輸出

print("-----for迴圈不能是空的,請放在pass陳述式中以避免出錯。")
#The pass Statement pass 陳述式
#for loops cannot be empty, but if you for some reason have
# a for loop with no content, put in the pass statement to 
# avoid getting an error.
#for迴圈不能是空的，但如果您出於某種原因有一個沒有內容的迴圈，
# 請放在pass陳述式中以避免出錯。
for x in [0, 1, 2]:
  pass
# having an empty for loop like this, would raise an error
# without the pass statement