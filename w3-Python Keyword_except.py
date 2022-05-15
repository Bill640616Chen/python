#https://www.w3schools.com/python/ref_keyword_except.asp
#Python Keyword except 關鍵字 except
#Used with exceptions, what to do when an exception occurs
#處理異常，發生異常時如何執行。
#If the statement raises an error print "Something went wrong":
#如果語句引發錯誤，則列印 「Something went wrong」：
# (x > 3) will raise an error because x is not defined:
try:
  x > 3
except:
  print("Something went wrong")
print("Even if it raised an error, the program keeps running")
#Definition and Usage 定義和用法
#The except keyword is used in try...except blocks. It defines a block of code to run if the try block raises an error.
#在 try ... except 塊中使用了關鍵字 except。 它定義 try 塊引發錯誤時要運行的代碼塊。
#You can define different blocks for different error types, and blocks to execute if nothing went wrong, see examples below.
#您可以為不同的錯誤類型定義不同的塊，以及沒有問題的情況下執行的塊，請參見下面的例子。
#Write one message if it is a NameError, and another if it is an TypeError:
print('-------------分隔線------------')
#如果引發 NameError 則寫一條消息，如果引發 TypeError 則寫另一條：
x = "hello"
try:
  x > 3
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
#Try to execute a statement that raises an error, but none of the defined error types (in this case, a ZeroDivisionError):
print('-------------分隔線------------')
#嘗試執行一條引發錯誤的語句，但沒有定義的錯誤類型（在這種情況下為 ZeroDivisionError）：
try:
  x = 1/0
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
except:
  print("Something else went wrong")
#Write a message if no errors were raised:
print('-------------分隔線------------')
#如果沒有出現錯誤，寫一條訊息：
x = 1
try:
  x > 10
except NameError:
  print("You have a variable that is not defined.")
except TypeError:
  print("You are comparing values of different type")
else:
  print("The 'Try' code was executed without raising any errors!")
#Related Pages 相關頁面
#The try keyword.
#The finally keyword.

