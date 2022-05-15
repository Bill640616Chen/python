#https://www.w3schools.com/python/gloss_python_raise.asp
#Python Raise an Exception 引發異常
#As a Python developer you can choose to throw an exception if a condition occurs.
#作為 Python 開發人員，您可以選擇在出現情況時引發異常。
#To throw (or raise) an exception, use the keyword.raise
#若要引發（或引發）異常，請使用關鍵字。raise
#Raise an error and stop the program if x is lower than 0:
#引發錯誤並在 x 小於 0 時停止程式：
try:
    x = -1
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as e:
    print(e)
#if為True時,引發錯誤
#The keyword is used to raise an exception.raise
#關鍵字用於引發異常。raise
#You can define what kind of error to raise, and the text to print to the user.
#您可以定義要引發的錯誤類型，以及要列印給使用者的文字。
print('-------------分隔線------------')
#Raise a TypeError if x is not an integer:
#如果 x 不是整數，則引發 TypeError：
try:
    x = "hello"
    if not type(x) is int:
        raise TypeError("Only integers are allowed")
except TypeError as e:
    print(e)
#if為True時,引發錯誤
#Related Pages 相關頁面
#Python Try Except Tutorial Python 嘗試教程除外
#https://www.w3schools.com/python/python_try_except.asp
#Error Handling 錯誤處理
#https://www.w3schools.com/python/gloss_python_error_handling.asp
#Handle Many Exceptions 處理許多異常
#https://www.w3schools.com/python/gloss_python_try_except.asp
#Try Else 嘗試其他
#https://www.w3schools.com/python/gloss_python_try_else.asp
#Try Finally 最後試試
#https://www.w3schools.com/python/gloss_python_try_finally.asp
