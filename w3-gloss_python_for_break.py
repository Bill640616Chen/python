#https://www.w3schools.com/python/gloss_python_for_break.asp
#For Break 
#With the break statement we can stop the loop before it has looped through all the items:
#通過中斷語句，我們可以在迴圈通過所有專案之前停止迴圈：
#Exit the loop when x is "banana":
#退出迴圈時是「香蕉」：x
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print('-------------分隔線------------')
#Exit the loop when x is "banana", but this time the break comes before the print:
#退出迴圈時是「香蕉」，但這次的中斷之前列印：x
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#Related Pages 相關頁面
#Python For Loops Tutorial
#https://www.w3schools.com/python/python_for_loops.asp
#For
#https://www.w3schools.com/python/gloss_python_for.asp
#Loop Through a String
#https://www.w3schools.com/python/gloss_python_for_string.asp
#For Continue
#https://www.w3schools.com/python/gloss_python_for_continue.asp
#Looping Through a Rrange
#https://www.w3schools.com/python/gloss_python_for_range.asp
#For Else
#https://www.w3schools.com/python/gloss_python_for_else.asp
#Nested Loops
#https://www.w3schools.com/python/gloss_python_for_nested.asp
#For pass
#https://www.w3schools.com/python/gloss_python_for_pass.asp