#https://www.w3schools.com/python/ref_keyword_break.asp
#Python Keyword break 關鍵字 break
#To break out of a loop
#跳出迴圈。
#End the loop if i is larger than 3:
#如果 i 大於 3，則結束迴圈：
for i in range(9):
  if i > 3:
    break
  print(i)
#Definition and Usage 定義和用法
#The break keyword is used to break out a for loop, or a while loop.
#break 關鍵字用於中斷 for 迴圈或 while 迴圈。
#Break out of a while loop:
print('-------------分隔線------------')
#中斷 while 迴圈：
i = 1
while i < 9:
  print(i)
  if i == 3:
    break
  i += 1
#Related Pages 相關頁面
#Use the continue keyword to end the current iteration in a loop, but continue with the next.
#使用continue關鍵字 可在迴圈中結束當前反覆運算，但繼續進行下一個。
#Read more about for loops in our Python For Loops Tutorial.
#請在我們的 Python For 迴圈教程 中閱讀有關 for 迴圈的更多資訊。
#Read more about while loops in our Python While Loops Tutorial.
#請在我們的 Python While 循環教程 中閱讀有關 while 迴圈的更多資訊。

