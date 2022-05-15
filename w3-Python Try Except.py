#https://www.w3schools.com/python/python_try_except.asp
#Python Try Except 檢查錯誤並處理。
#The try block lets you test a block of code for errors.
#try 塊允許您測試代碼塊以查找錯誤。
#The except block lets you handle the error.
#except 塊允許您處理錯誤。
#The finally block lets you execute code, regardless of the result of the try- and except blocks.
#finally 塊允許您執行代碼，無論 try 和 except 塊的結果如何。
print("------------------------Exception Handling 異常處理")
#Exception Handling 異常處理
#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
#當我們調用 Python 併發生錯誤或異常時，通常會停止並生成錯誤消息。
#These exceptions can be handled using the try statement:
#可以使用 try 語句處理這些異常：
#The try block will generate an exception, because x is not defined:
#try 塊將生成異常，因為 x 未定義：
try:
  print(x)
except:
  print("An exception occurred")
#Since the try block raises an error, the except block will be executed.
#由於 try 塊引發錯誤，因此會執行 except 塊。
#Without the try block, the program will crash and raise an error:
#如果沒有 try 塊，程式將崩潰並引發錯誤：
#This statement will raise an error, because x is not defined:
#該語句將引發錯誤，因為未定義 x：
#print(x)
#NameError: name 'x' is not defined

print("------------------------Many Exceptions 多個異常")
#Many Exceptions 多個異常
#You can define as many exception blocks as you want, e.g. if 
# you want to execute a special block of code for a special 
# kind of error:
#您可以根據需要定義任意數量的 exception 塊，例如，假如您要為
# 特殊類型的錯誤執行特殊代碼塊：
#Print one message if the try block raises a NameError and 
# another for other errors:
#如果 try 塊引發 NameError，則列印一條消息，如果是其他錯誤則列印
# 另一條消息：
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

print("-----------------Else 使用 else 關鍵字來定義要執行的代碼塊")
#Else
#You can use the else keyword to define a block of code to be executed if no errors were raised:
#如果沒有引發錯誤，那麼您可以使用 else 關鍵字來定義要執行的代碼塊：
#In this example, the try block does not generate any error:
#在本例中，try 塊不會產生任何錯誤：
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

print("------------------------------------Finally 最後處理")
#Finally 最後處理
#The finally block, if specified, will be executed regardless 
# if the try block raises an error or not.
#如果指定了 finally 塊，則無論 try 塊是否引發錯誤，都會執行 finally 塊。
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#This can be useful to close objects and clean up resources:
#這對於關閉物件並清理資源非常有用：
print("------------------finally---試圖開啟並寫入不可寫的檔案")
#Try to open and write to a file that is not writable:
#試圖開啟並寫入不可寫的檔案：
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close() #直接關閉物件
except:
  print("Something went wrong when opening the file")
#The program can continue, without leaving the file object open.
#程式可以繼續，而且不會打開文件物件。

print("-----------------------------Raise an exception 引發異常")
#Raise an exception 引發異常
#As a Python developer you can choose to throw an exception if a condition occurs.
#作為 Python 開發者，您可以選擇在條件發生時拋出異常。
#To throw (or raise) an exception, use the raise keyword.
#如需拋出（引發）異常，請使用 raise 關鍵詞。
#Raise an error and stop the program if x is lower than 0:
#假如 x 小於 0，則引發異常並終止程式：
try:
    x = -1
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as e:
    #錯誤被捕抓到except Exception裡去做處理了，處理完後，就繼續從
    # except Exception補捉到的錯誤as e:賦值給e
    print(e)
    #except處理錯誤的關鍵字,as把類別實體化
  #Exception("裡面的文字可以修改")
#The raise keyword is used to raise an exception.
#raise 關鍵字用於引發異常。
#You can define what kind of error to raise, and the text to print to the user.
#您能夠定義所引發異常的類型、以及列印給使用者的文字。
#Raise a TypeError if x is not an integer:
#如果 x 不是整數，則引發 TypeError：
try:
  x = "hello"
  if not type(x) is int:
    raise TypeError("Only integers are allowed")
except TypeError as e:
    print(e)

  #TypeError("裡面的文字可以修改")
