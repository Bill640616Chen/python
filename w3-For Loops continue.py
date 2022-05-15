#https://www.w3schools.com/python/python_while_loops.asp
#Python For Loops 

print("--------------------continue Statement 繼續陳述式-1")
#The continue Statement 繼續陳述式
#With the continue statement we can stop the current 
# iteration of the loop, and continue with the next:
#用continue陳述式,我們可以停止目前迴圈反覆運算,然後繼續下一個
#Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue 
  #跟break一樣,若條件是True就是跳出迴圈,但是continue會繼續下一個
  print(x)
#apple先到for x in fruits:代入x
#然後進入if x == "banana":判斷為False
#跳過continue,直接print(x)輸出
#banana先到for x in fruits:代入x
#然後進入if x == "banana":判斷為True
#執行continue,跳出迴圈,接著換下一個進入迴圈
#cherry先到for x in fruits:代入x
#然後進入if x == "banana":判斷為False
#跳過continue,直接print(x)輸出
#apple
#cherry
print("--------------------continue Statement 繼續陳述式-2")
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print ('当前字母 :', letter)
print("--------------------continue Statement 繼續陳述式-3")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x != "banana":
    continue 
  #跟break一樣,若條件是True就是跳出迴圈,但是continue會繼續下一個
  print(x)
print("--------------------continue Statement 繼續陳述式-4")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue 
  #跟break一樣,若條件是True就是跳出迴圈,但是continue會繼續下一個
print(x) #cherry,print(x)在迴圈外
#apple先到for x in fruits:代入x
#然後進入if x == "banana":判斷為False
#跳過continue,回到for x in fruits:迴圈
#banana先到for x in fruits:代入x
#然後進入if x == "banana":判斷為True
#執行continue,跳出迴圈,接著換下一個進入迴圈
#cherry先到for x in fruits:代入x
#然後進入if x == "banana":判斷為False
#跳過continue,迴圈最後一個x在print(x)輸出
print("--------------------continue Statement 繼續陳述式-5")
fruits = ["apple", "banana", "cherry"]
print(x) #cherry,print(x)在迴圈外
for x in fruits:
  if x == "banana":
    continue 
else:#迴圈完成後,指定一個程式碼區塊要執行
  print("Finally finished!")
  #跟break一樣,若條件是True就是跳出迴圈,但是continue會繼續下一個
#apple先到for x in fruits:代入x
#然後進入if x == "banana":判斷為False
#跳過continue,回到for x in fruits:迴圈
#banana先到for x in fruits:代入x
#然後進入if x == "banana":判斷為True
#執行continue,跳出迴圈,接著換下一個進入迴圈
#cherry先到for x in fruits:代入x
#然後進入if x == "banana":判斷為False
#跳過continue,迴圈最後一個x在print(x)輸出
#迴圈完成後,執行迴圈外的else區塊
print("--------------------continue Statement 繼續陳述式-6")
fruits = ["apple", "banana", "cherry"]
print(x) #cherry,在第58行最後一輪時被賦值為cherry
for y in fruits:
  if y == "banana":
    continue 
  else:#迴圈完成後,指定一個程式碼區塊要執行
    print("Finally finished!")
  #跟break一樣,若條件是True就是跳出迴圈,但是continue會繼續下一個
#76行中的x，在第58行最後一輪時被賦值為cherry
#所以在第76行時印出cherry
#然後第77到81行時印出2次的Finally finished!
#所以當印出上面的程式的x之後,迴圈的x 重新被list賦值
#輸出Finally finished!的是apple跟cherry
#這裡的else縮排,變成if else
print(x) #在第58行最後一輪時被賦值為cherry
print("--------------------continue Statement 繼續陳述式-7")
fruits = ["apple", "banana", "cherry"]
#print(x) #cherry,在第58行最後一輪時被賦值為cherry
for y in fruits:
  if y == "banana":
    continue 
  else:#迴圈完成後,指定一個程式碼區塊要執行
    print("Finally finished!")
  #跟break一樣,若條件是True就是跳出迴圈,但是continue會繼續下一個
#76行中的x，在第58行最後一輪時被賦值為cherry
#所以在第76行時印出cherry
#然後第77到81行時印出2次的Finally finished!
#所以當印出上面的程式的x之後,迴圈的x 重新被list賦值
#輸出Finally finished!的是apple跟cherry
#這裡的else縮排,變成if else
print(y) #在第58行最後一輪時被賦值為cherry