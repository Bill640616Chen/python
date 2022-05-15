#https://www.w3schools.com/python/gloss_python_for_range.asp
#Looping Through a Range
#To loop through a set of code a specified number of times, we can use the range() function,
#要迴圈流覽一組代碼的指定次數，我們可以使用範圍 （）功能，
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
#範圍（）功能返回一系列數位，從預設值的 0 開始，以 1（預設情況下）為增量，以指定數字結束。
#Using the range() function:
#使用範圍 （） 功能：
for x in range(6):
  print(x)
print('-------------分隔線------------')
#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
#請注意，範圍 （6）不是 0 到 6 的值，而是值 0 到 5。
#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
#範圍（）函數預設為 0 作為起始值，但可以通過添加參數來指定起始值：範圍（2，6），這意味著值從 2 到 6（但不包括 6）：
#Using the start parameter:
#使用起始參數：
for x in range(2, 6):
  print(x)
print('-------------分隔線------------')
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
#範圍（）函數預設增大序列 1，但可以通過添加第三個參數來指定增量值：範圍 （2、30、3） ：
#Increment the sequence with 3 (default is 1):
#以 3（預設值為 1）增量序列：
for x in range(2, 30, 3):
  print(x)
#Related Pages 相關頁面
#Python For Loops Tutorial
#https://www.w3schools.com/python/python_for_loops.asp
#For
#https://www.w3schools.com/python/gloss_python_for.asp
#Loop Through a String
#https://www.w3schools.com/python/gloss_python_for_string.asp
#For Break
#https://www.w3schools.com/python/gloss_python_for_break.asp
#For Continue
#https://www.w3schools.com/python/gloss_python_for_continue.asp
#For Else
#https://www.w3schools.com/python/gloss_python_for_else.asp
#Nested Loops
#https://www.w3schools.com/python/gloss_python_for_nested.asp
#For pass
#https://www.w3schools.com/python/gloss_python_for_pass.asp