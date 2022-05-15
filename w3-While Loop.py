#https://www.w3schools.com/python/python_lists_loop.asp
#Python While Loop 條件式迴圈
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
print("------------While Loop")
thislist = ["apple", "banana", "cherry"]
i = 0 # while的條件,i的起始值要設定
while i < len(thislist):
  print(thislist[i]) #輸出的結果跟for一樣
  i = i + 1 
#條件是i要一直往上加到小於3為止,
# i += 1也可, i -= 1會變成list index out of range
print("------------While Loop")
#Python has two primitive loop commands:
#Python 有兩個原始迴圈指令
#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.
#在迴圈中，只要條件屬實，我們就可以執行一組陳述。
#Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1 #此line為增量,line30-32是一組陳述
#Note: remember to increment i, or else the loop will continue forever.
#筆記:記住要增量 i，否則迴圈將永久持續。滅量也會造成迴圈永久持續= =
#The while loop requires relevant variables to be ready, in this 
# example we need to define an indexing variable, i, 
# which we set to 1.
#while迴圈需要相關變數做好準備，但在本示例中，我們需要定義索引變數 i，
# 我們將其設置為 1。
print("------------break Statement(print在break之前)")
#The break Statement 中斷陳述
#With the break statement we can stop the loop even if the while condition is true:
#用中斷陳述，我們可以停止迴圈，即使whilel裡的條件是True：
#Exit the loop when i is 3:
i = 1
while i < 6:
  print(i) #1 2 3
  if i == 3:
    break
  i += 1
print("-----break Statement(print在break之後)")
i = 1
while i < 6:
  if i == 3:
    break
  i += 1
  print(i) #2 3,一開始代入的1,中斷後,變成i=2,輸出當然是由2開始
#1. i賦值1
#2. 進入while迴圈
#3. 判斷i是否小於6 因為i等於1，1<6正確，執行while迴圈
#4. 判斷i是否等於3，因為i=1，1不等於3，不執行if判斷式內的程式
#5. 執行i+=1,原本i 等於1, +1變成2
#6. print(i)輸出i,因為目前i等於2，所以輸出2
print("-----------在while裡面每次代入都沒輸出,print沒在while迴圈裡")
i = 1
while i < 6:
  if i == 3:
    break
  i += 1
print(i) #3
#在while裡面每次代入都沒輸出,當中斷時才有值輸出
print("-----------在while裡面每次代入都沒輸出,print沒在while迴圈裡")
i = 1
while i < 20:
  if i == 18:
    break
  i += 1
print(i) #18
#在while裡面每次代入都沒輸出,當中斷時才有值輸出
#如果把print(i))縮排在條件式裡,是無法執行的
  