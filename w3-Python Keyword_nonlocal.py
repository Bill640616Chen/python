#https://www.w3schools.com/python/ref_keyword_nonlocal.asp
#Python Keyword nonlocal 關鍵字 nonlocal
#To declare a non-local variable
#聲明非局部變數。
#Make a function inside a function, which uses the variable x as a non local variable:
#在函數內部建立一個函數，該函數使用變數 x 作為非局部變數：
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x
print(myfunc1())
#Definition and Usage 定義和用法
#The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
#nonlocal 關鍵字用於在嵌套函數內部使用變數，其中變數不應屬於內部函數。
#Use the keyword nonlocal to declare that the variable is not local.
#請使用關鍵字 nonlocal 聲明變數不是本地變數。
#Same example as above, but without the nonlocal keyword:
print('-------------分隔線------------')
#與上例相同，但不使用 nonlocal 關鍵字：
def myfunc1():
  x = "John"
  def myfunc2():
    x = "hello"
  myfunc2()
  return x
print(myfunc1())
#Related Pages 相關頁面
#The keyword global is used to make global variables.
#關鍵字 global 用於創建全域變數。