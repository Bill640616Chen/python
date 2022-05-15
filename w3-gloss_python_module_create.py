#https://www.w3schools.com/python/gloss_python_module_create.asp
#Create Module 建立模組
#What is a Module? 什麼是模組？
#Consider a module to be the same as a code library.
#將模組視為與代碼庫相同。
#A file containing a set of functions you want to include in your application.
#包含要包含在應用程式中的一組函數的檔案。
#Create a Module創建模組
#To create a module just save the code you want in a file with the file extension :.py
#要創建一個模組，只需將所需的代碼保存在檔案擴展名為的檔案中：.py
#Save this code in a file named mymodule.py
#將此代碼保存在名為mymodule.py
def greeting(name):
  print("Hello, " + name)
#Use a Module 使用模組
#Now we can use the module we just created, by using the statement:import
#現在，我們可以使用剛剛創建的模組，方法是使用以下語句：import
#Import the module named mymodule, and call the greeting function:
#導入名為 mymodule 的模組，並調用 greeting 函數：
import mymodule
mymodule.greeting("Jonathan")
#Note: When using a function from a module, use the syntax: module_name.function_name.
#注意：使用模組中的函數時，請使用語法：module_name.function_name。
#Related Pages 相關頁面
#Python Modules Tutorial Python 模組教程
#https://www.w3schools.com/python/python_modules.asp
#Variables in Modules 模組中的變數
#https://www.w3schools.com/python/gloss_python_module_variables.asp
#Renaming a Module 重新命名模組
#https://www.w3schools.com/python/gloss_python_module_rename.asp
#Built-in Modules 內置模組
#https://www.w3schools.com/python/gloss_python_module_built-in.asp
#Using the dir() Function 使用 dir（） 函數
#https://www.w3schools.com/python/gloss_python_module_dir.asp
#Import From Module 從模組導入
#https://www.w3schools.com/python/gloss_python_module_import_from.asp