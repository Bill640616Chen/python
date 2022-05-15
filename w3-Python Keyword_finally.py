#https://www.w3schools.com/python/ref_keyword_finally.asp
#Python Keyword finally 關鍵字 finally
#Used with exceptions, a block of code that will be executed no matter if there is an exception or not
#處理異常，無論是否存在異常，都將執行一段代碼。
#The finally block will always be executed, no matter if the try block raises an error or not:
#無論 try 塊是否引發錯誤，都將始終執行 finally 塊：
try:
  x > 3
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
finally:
  print("The try...except block is finished")
#Definition and Usage 定義和用法
#The finally keyword is used in try...except blocks. It defines a block of code to run when the try...except...else block is final.
#finally 關鍵字在 try ... except 塊中使用。 它定義了一個代碼塊，當 try... except... else 塊結束時，該代碼塊將運行。
#The finally block will be executed no matter if the try block raises an error or not.
#無論 try 塊是否引發錯誤，都將執行 finally 塊。
#This can be useful to close objects and clean up resources.
#這對於關閉物件和清理資源很有用。
#Related Pages 相關頁面
#The try keyword.
#The except keyword.


