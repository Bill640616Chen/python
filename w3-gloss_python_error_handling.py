#https://www.w3schools.com/python/gloss_python_error_handling.asp
#Python Error Handling 錯誤處理
#The block lets you test a block of code for errors.try
#該塊允許您測試代碼塊是否存在錯誤。try
#The block lets you handle the error.except
#該塊允許您處理錯誤。except
#The block lets you execute code, regardless of the result of the try- and except blocks.finally
#該塊允許您執行代碼，而不管 try- 的結果如何，除了塊。finally
#Exception Handling 異常處理
#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#當發生錯誤或我們所說的異常時，Python通常會停止並生成錯誤消息。
#These exceptions can be handled using the statement:try
#可以使用以下語句處理這些異常：try
#The block will generate an exception, because is not defined:tryx
#該塊將生成異常，因為未定義：try x
try:
  print(x)
except:
  print("An exception occurred")
#Since the try block raises an error, the except block will be executed.
#由於 try 塊會引發錯誤，因此將執行 except 塊。
#Without the try block, the program will crash and raise an error:
#如果沒有 try 塊，程式將崩潰並引發錯誤：
#This statement will raise an error, because is not defined:x
#此語句將引發錯誤，因為 未定義：x
#print(x)
#Related Pages 相關頁面
#Python Try Except Tutorial Python 嘗試教程除外
#https://www.w3schools.com/python/python_try_except.asp
#Handle Many Exceptions 處理許多異常
#https://www.w3schools.com/python/gloss_python_try_except.asp
#Try Else 嘗試其他
#https://www.w3schools.com/python/gloss_python_try_else.asp
#Try Finally 最後試試
#https://www.w3schools.com/python/gloss_python_try_finally.asp
#raise 引發
#https://www.w3schools.com/python/gloss_python_raise.asp