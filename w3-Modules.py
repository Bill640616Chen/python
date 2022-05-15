#https://www.w3schools.com/python/python_modules.asp
#Python Modules 模組
#What is a Module? 模組是什麼 就是一個py檔
#Consider a module to be the same as a code library.
#請思考模組與代碼庫相同。
#A file containing a set of functions you want to include 
# in your application.
#一個檔案要包含一組功能,你想要包括在你的應用程式中
#Create a Module 创建模組
#To create a module just save the code you want in a file 
# with the file extension .py:
#如需創建模組，只需將所需代碼保存在文件擴展名为 .py 的文件中：
#Save this code in a file named mymodule.py
#在名為 mymodule.py 的文件中保存代碼：
def greeting(name):
  print("Hello, " + name)

print("------------------------------Use a Module 使用模組")
#Use a Module 使用模組
#Now we can use the module we just created, by using the 
# import statement:
#現在，我們就可以用 import 語句來使用我們剛剛創建的模組：
#Import the module named mymodule, and call the greeting function:

import w3mymodule 
#模組命名不能有符號及空格,否則無法import
w3mymodule.greeting("Jonathan")
#模組.函數(變數):輸入模組,使用模組的函數功能
#Note: When using a function from a module, use the syntax: 
# module_name.function_name.
#註釋：如果使用模組中的函數時，請使用以下語法：
# module_name.function_name. w3mymodule.greeting

print("------------------Variables in Module 模組中的變數")
#Variables in Module 模組中的變數
#The module can contain functions, as already described, 
# but also variables of all types (arrays, dictionaries, 
# objects etc):
#模組可以包含已經描述的函數，但也可以包含各種類型的變數
# （陣列、字典、物件等）：
#Import the module named mymodule, and access the person1 dictionary:
import w3mymodule
a = w3mymodule.person1["age"]
print(a)

print("--------------------------Naming a Module 為模組命名")
#Naming a Module 為模組命名
#You can name the module file whatever you like, but it must have the file extension .py
#您可以隨意對模組文件命名，但是文件擴展名必須是 .py。
#Re-naming a Module 重命名模組
#You can create an alias when you import a module, by using the as keyword:
#您可以在導入模組時使用 as 關鍵字創建別名：
#Create an alias for mymodule called mx:
#為 w3mymodule 創建别名 mx：
import w3mymodule as mx
a = mx.person1["age"]
print(a)

print("---------------------------Built-in Modules 内建模組")
#Built-in Modules 内建模組
#There are several built-in modules in Python, which you can import whenever you like.
#Python 中有幾個內建模組，您可以隨時導入。
#Import and use the platform module:
import platform
x = platform.system()
print(x)
#platform 平台
#This module tries to retrieve as much platform-identifying 
# data as possible. It makes this information available via 
# function APIs.
#此模組嘗試檢索盡可能多的平臺識別數據。它通過功能 APIs 提供此資訊。
#If called from the command line, it prints the platform 
# information concatenated as single string to stdout
# (standard out的縮寫). The output format is useable as part 
# of a filename.
#如果從指令線調用，它將平臺資訊列印為單個字串到標準輸出。
# 輸出格式可作為檔名的一部分使用。
#system() 返回系統/操作系統名稱
#Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.
#返回系統/操作系統名稱，例如"Linux"，"Windows"或"Java"。
#An empty string is returned if the value cannot be determined.
#如果無法確定值，則返回空字串。

print("---------------------------Using the dir() Function")
#Using the dir() Function
#There is a built-in function to list all the function names
# (or variable names) in a module. The dir() function:
#有一個內建函數可以列出模組中的所有函數名（或變數名）。dir()函數：
#List all the defined names belonging to the platform module:
import platform
x = dir(platform)
print(x)
#Note: The dir() function can be used on all modules, 
# also the ones you create yourself.
#註釋：dir() 函數可用於所有模組，也可用於您自己創建的模組。

print("-----------------------Import From Module 從模組輸入")
#Import From Module 從模組輸入
#You can choose to import only parts from a module, by using the from keyword.
#您可以使用 from 關鍵字選擇僅從模組導入部件。
#The module named mymodule has one function and one dictionary:
def greeting(name):
  print("Hello, " + name)
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#Import only the person1 dictionary from the module:
from w3mymodule import person1
print (person1["age"]) #36
#Note: When importing using the from keyword, do not use 
# the module name when referring to elements in the module. 
# Example: person1["age"], not mymodule.person1["age"]
#提示：在使用 from 關鍵字導入時，請勿在引用模組中的元素時使用
# 模組名稱。示例：person1["age"]，而不是mymodule.person1["age"]。

