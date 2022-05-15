#https://www.w3schools.com/python/python_variables_global.asp
#Global Variables全球變數
#在函數之外創建的變數（如上文所有示例中所示）稱為全球變數。
print("------------------------全球變數可用於函數內外的每個人")
#全球變數可用於功能內外的每個人。
#在函數之外創建一個變數，並在函數內使用它
x = "awesome"#也是叫做全域變數
def myfunc():
  print("Python is " + x)
myfunc()

print("-----如果在函數內創建具有相同名稱的變數，此變數將是本地的")
#如果在函數內創建具有相同名稱的變數，此變數將是本地的，
# 並且只能在函數內使用。同名的全球變數將保持原樣，具有全球性和原始值。
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()#只能取本地(區域)的變數,只能在函數內用
print("Python is " + x)#非函數內,所以取全球變數
#Python is fantastic
#Python is awesome

print("-----------------global給予全球變數,不再屬於本地變數了")
#The global Keyword 全球關鍵字
#通常，當您在函數內創建變數時，該變數是本地的，並且只能在該函數內使用。
#要在函數內創建全球變數，您可以使用關鍵字。global
#如果您使用關鍵字，該變數屬於全球範圍：global
def myfunc():
  global x  #global給予全球變數,不再屬於本地變數了
  x = "fantastic"
myfunc()
print("Python is " + x)
#Python is fantastic
print("------------------這裡宣告了x新的變數取代原來的變數了")
#此外，如果您想要更改函數內的全球變數，請使用關鍵字。global
x = "awesome"
def myfunc():
  global x
  x = "fantastic" #這裡宣告了x新的變數取代原來的變數了
myfunc()
print("Python is " + x)
#Python is fantastic