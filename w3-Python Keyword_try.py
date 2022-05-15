#https://www.w3schools.com/python/ref_keyword_try.asp
#Python Keyword try 關鍵字 try
#To make a try...except statement
#編寫 try... except 語句。
#Try a block of code, and decide what to to if it raises an error:
#嘗試一段代碼，並確定如果引發錯誤該怎麼辦：
try:
  x > 3
except:
  print("Something went wrong")
#Definition and Usage 定義和用法
#The try keyword is used in try...except blocks. It defines a block of code test if it contains any errors.
#try 關鍵字用於 try... except 塊中。 它定義了代碼測試塊是否包含任何錯誤。
#You can define different blocks for different error types, and blocks to execute if nothing went wrong, see examples below.
#您可以為不同的錯誤類型定義不同的塊，以及在沒有問題的情況下執行的代碼塊，請參見下面的例子。
#Raise an error and stop the program when there is an error in the try block:
print('-------------分隔線------------')
#在 try 塊中發生錯誤時引發錯誤並停止程式：
try:
  x > 3
except:
  Exception("Something went wrong")
#Related Pages 相關頁面
#The except keyword.
#https://www.w3schools.com/python/ref_keyword_except.asp
#The finally keyword.
#https://www.w3schools.com/python/ref_keyword_finally.asp

