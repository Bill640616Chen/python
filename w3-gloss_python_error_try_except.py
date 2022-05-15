#https://www.w3schools.com/python/gloss_python_try_except.asp
#Python Try Except 錯誤處理
#The block lets you test a block of code for errors.try
#該塊允許您測試代碼塊是否存在錯誤。try
#The block lets you handle the error.except
#該塊允許您處理錯誤。except
#The block lets you execute code, regardless of the result of the try- and except blocks.finally
#該塊允許您執行代碼，而不管 try- 的結果如何，除了塊。finally
#Many Exceptions
#You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
#您可以根據需要定義任意數量的異常塊，例如，如果要為特殊類型的錯誤執行特殊的代碼塊：
#Print one message if the try block raises a and another for other errors:NameError
#如果 try 塊引發 a，則列印一條消息，另一條消息用於其他錯誤：NameError
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
#Related Pages 相關頁面
#Python Try Except Tutorial Python 嘗試教程除外
#https://www.w3schools.com/python/python_try_except.asp
#Error Handling 錯誤處理
#https://www.w3schools.com/python/gloss_python_error_handling.asp
#Try Else 嘗試其他
#https://www.w3schools.com/python/gloss_python_try_else.asp
#Try Finally 最後試試
#https://www.w3schools.com/python/gloss_python_try_finally.asp
#raise 引發
#https://www.w3schools.com/python/gloss_python_raise.asp