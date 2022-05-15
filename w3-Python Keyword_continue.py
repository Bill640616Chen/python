#https://www.w3schools.com/python/ref_keyword_continue.asp
#Python Keyword continue 關鍵字 continue
#To continue to the next iteration of a loop
#繼續迴圈的下一個反覆運算。
#Skip the iteration if the variable i is 3, but continue with the next iteration:
#如果變數 i 為 5，則跳過反覆運算，但繼續進行下一個反覆運算：
for i in range(9):
  if i == 3:
    continue
  print(i)
#Definition and Usage 定義和用法
#The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
#continue 關鍵字用於在 for 迴圈（或 while 迴圈）中結束當前反覆運算，然後繼續下一個反覆運算。
#Use the continue keyword in a while loop:
print('-------------分隔線------------')
#在 while 迴圈中使用 continue 關鍵字：
i = 0
while i < 9:
  i += 1
  if i < 3:
    continue
  print(i)
#Related Pages 相關頁面
#Use the break keyword to end the loop completely.
#使用 break 關鍵字 徹底結束迴圈。
#Read more about for loops in our Python For Loops Tutorial.
#請在我們的 Python For 迴圈教程 中學習更多有關循環的知識。
#Read more about while loops in our Python While Loops Tutorial.
#請在我們的 Python While 循環教程 中學習更多有關循環的知識。