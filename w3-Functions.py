#https://www.w3schools.com/python/python_functions.asp
#Python function 函數
#A function is a block of code which only runs when it is called.
#函數是代碼塊，只有在調用時才運行。
#You can pass data, known as parameters, into a function.
#您可以將資料（稱為參數）傳遞到函數中。
#A function can return data as a result.
#因此，一個功能可以傳回數據。
#Creating a Function 建立一個函數
#In Python a function is defined using the def keyword:
#在 Python 中，使用 def 關鍵字定義一個函數：
def my_function():
  print("Hello from a function")
#用def定義一個函數的功能
#my_function()函數名稱
#print("Hello from a function")函數的功能

print("-----------------------------------呼叫函數")
#Calling a Function 呼叫函數
#To call a function, use the function name followed by parenthesis:
#要呼叫函數，使用函數名稱也要跟著後面的()：
def my_function():
  print("Hello from a function")
my_function()
#Hello from a function

print("-----------------------------Arguments 參數")
#Arguments 參數
#Information can be passed into functions as arguments.
#信息可以傳遞到函數裡作為參數
#Arguments are specified after the function name, inside 
# the parentheses. You can add as many arguments as you 
# want, just separate them with a comma.
#在函數名稱後,參數是被指定的,在括孤內。您可以隨需要添加盡可能多
# 的參數，只需用逗號將其分開即可。
#The following example has a function with one argument
#  (fname). When the function is called, we pass along a 
# first name, which is used inside the function to print 
# the full name:
print("------------------函數名稱()裡的東西叫Arguments參數")
#下列示例具有一個參數（fname）的函數。當函數調用時，我們傳遞一
# 個名字，該名稱在函數內用於列印全名：
def my_function(fname): #fname是Arguments參數
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
#Arguments are often shortened to args in Python documentations.
#在 Python 文件中，參數通常被縮短為 args(阿格斯)。

#Parameters or Arguments?
#The terms parameter and argument can be used for the same 
# thing: information that are passed into a function.
#參數和參數的術語可用於同一件事：傳遞到資訊函數中。
#From a function's perspective: 從函數的角度來看：
#A parameter is the variable listed inside the parentheses 
# in the function definition.
#參數parameter是函數定義括弧內列出的變數。
#An argument is the value that is sent to the function when
# it is called.
#參數argument是調用功能時發送到函數的值。

print("----------------------Number of Arguments 參數數字")
#Number of Arguments 參數數字
#By default, a function must be called with the correct 
# number of arguments. Meaning that if your function 
# expects 2 arguments, you have to call the function 
# with 2 arguments, not more, and not less.
#預設狀況下,一個函數一定要被正確的參數數字呼叫。意思是說你的
# 函數預期有2個參數,你必須呼叫有2個參數的函數,不可多也不可少
#This function expects 2 arguments, and gets 2 arguments:
#這個函數預期有2個參數而且得到2個參數
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
#If you try to call the function with 1 or 3 arguments, you will get an error:
#如果你試著呼叫1個或3個參數的函數,會出現錯誤
#This function expects 2 arguments, but gets only 1:
#def my_function(fname, lname):
#  print(fname + " " + lname)
#my_function("Emil")
#TypeError: my_function() missing 1 required positional 
# argument: 'lname'

print("-----------Arbitrary Arguments, *args 任何參數 *args")
#Arbitrary Arguments, *args 任何參數 *args
#If you do not know how many arguments that will be passed
# into your function, add a * before the parameter name in 
# the function definition.
#如果您不知道有多少參數將傳遞到您的函數中，請在函數定義中的參數
# 名稱之前添加一個 * 。
#This way the function will receive a tuple of arguments, 
# and can access the items accordingly:
#這個方法可以使函數收到一個很多參數tuple序列，並可以相應地訪問項目：
#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids): 
#*kids 代表99行呼叫函數裡的每一個參數
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#如果使用*args(tuple型態的參數),則取值必須用索引tuple的方式取值
#呼叫函數也必須是tuple型態的參數("Emil", "Tobias", "Linus")
#my_function("Emil", "Tobias", "Linus")
#在函數裡功能print("The youngest child is " + kids[2])
#kids[2]代表只要索引位置2的參數代入
#所以輸出結果為The youngest child is Linus
#def my_function(*kids): 
#  print("The youngest child is " + kids)
#my_function("Emil", "Tobias", "Linus")
#can only concatenate str (not "tuple") to str
#只能串聯 str （而不是 "tuple"） 到 str

#Arbitrary Arguments are often shortened to *args in Python 
# documentations.
#任意參數通常縮短為 Python 文件中的 *args
#呼叫的函數裡是tuple型態的參數

print("---------------------Keyword Arguments 關鍵字參數")
#Keyword Arguments 關鍵字參數
#You can also send arguments with the key = value syntax.
#你也可以傳送key=value的語法至參數
#This way the order of the arguments does not matter
#這個方法,參數的順序不重要
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child2 = "Emil", child3 = "Tobias", child1 = "Linus")

print("-------------------------任意關鍵字參數數量,**kwargs")
#The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
#在 Python 文件中，「關鍵字參數」一詞通常被縮短為 kwargs。
#Arbitrary Keyword Arguments, **kwargs
#任意關鍵字參數,**kwargs
#If you do not know how many keyword arguments that will 
# be passed into your function, add two asterisk: ** before 
# the parameter name in the function definition.
#如果您不知道有多少關鍵字參數將傳遞到您的函數中，請在函數定義中
# 的參數名稱之前添加兩個星號：**。
#This way the function will receive a dictionary of 
# arguments, and can access the items accordingly:
#這個方法函數將會收到參數的字典型態,而可以訪問字典的項目
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
#如果關鍵字參數的數量未知，在參數名稱之前添加雙**：
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
#如果使用**kwargs(字典型態的參數),則取值必須用索引字典的方式取值
#呼叫函數也必須是字典型態的參數(fname = "Tobias", lname = "Refsnes")
#鍵=值,不用鍵:值
#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
#在 Python 文件中，任意 Kword 參數通常被縮短為 **kwargs。
#呼叫的函數裡是字典型態的參數

print("--------------------Default Parameter Value 預設參數值")
#Default Parameter Value 預設參數值
#The following example shows how to use a default parameter 
# value.
#下面的示例顯示了如何使用預設參數值。
#If we call the function without argument, it uses the 
# default value:
#如果我們在沒有參數的情況下調用該函數，則它使用預設值：
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()#裡面沒變數,預設值為函數名稱裡Norway
my_function("Brazil")

print("--------------------------------將清單作為參數傳遞")
#Passing a List as an Argument 將清單作為參數傳遞
#You can send any data types of argument to a function 
# (string, number, list, dictionary etc.), and it will 
# be treated as the same data type inside the function.
#您可以將任何數據類型的參數發送到函數（字串、數字、清單、字典等）
# ，並將將其視為函數內的相同數據類型。
#E.g. if you send a List as an argument, it will still be 
# a List when it reaches the function:
#例如，如果您發送清單作為參數，則當清單到達函數時，它仍將是清單
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
tuple1 = ("apple", "banana", "cherry")
my_function(fruits)
my_function(tuple1)

print("--------------------------------Return Values 傳回值")
#Return Values 傳回值
#To let a function return a value, use the return statement:
#要讓一個函數返回值，請使用返回語句：
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#The pass Statement pass陳述式
#function definitions cannot be empty, but if you for some 
# reason have a function definition with no content, put in 
# the pass statement to avoid getting an error.
#函數定義不能是空的，但如果由於某種原因沒有內容的函數定義，
# 請在函數的內容放入pass陳述式以避免出錯。
def myfunction():
  pass

