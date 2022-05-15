#https://www.w3schools.com/python/python_while_loops.asp
#Python While Loops 
#Python Loops
#Python has two primitive loop commands:
#while loops
#for loops

print("----------------------print在while後面")
#The while Loop
#With the while loop we can execute a set of statements as long as a condition is true.
#在while迴圈,只要條件是True我們就可以執行一組陳述式
#Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1
#從i = 1開始,然後進入while迴圈
#進到whiel i < 6: 1<6 是True
#到print(i)輸出1
#再到 i+= 1, 此時的i變成 1+=1,i=2
#再回到while 2<6 : 繼續往下執行
#迴圈到while i < 6:是False迴圈就停止
#Note: remember to increment i, or else the loop will continue forever.
#筆記：記得增量 i， 否則循環將永遠繼續下去。
#如果是減量,迴圈就沒止盡了...
#The while loop requires relevant variables to be ready, 
# in this example we need to define an indexing variable, 
# i, which we set to 1.
#迴圈需要相關變數做好準備，但在本示例中，我們需要定義索引變數 i，
#我們將其設置為 1

print("-----------break Statement(print在while後面)")
#The break Statement 中斷陳述
#With the break statement we can stop the loop even if the while condition is true:
#靠著break陳述,我可以停止迴圈,即使while條件是True
#Exit the loop when i is 3:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#如果 i == 3 ，就停止迴圈
#進到while迴圈,執行i<6,再print(i)
#接著進到if i == 3:結果沒有==3,沒中斷,進到i += 1
#回到迴圈while i <6