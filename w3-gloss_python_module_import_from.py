#https://www.w3schools.com/python/gloss_python_module_import_from.asp
#Import From Module 從模組導入
#You can choose to import only parts from a module, by using the keyword.from
#您可以選擇僅從模組中導入部件，方法是使用關鍵字。from
#The module named has one function and one dictionary:mymodule
#命名的模組有一個函數和一個字典：mymodule
'''def greeting(name):
  print("Hello, " + name)
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
'''
#Import only the person1 dictionary from the module:
#僅從模組中匯入 person1 字典：
from mymodule import person1
print (person1["age"])
#Note: When importing using the keyword, do not use the module name when referring to elements in the module. Example: , notfromperson1["age"] mymodule.person1["age"]
#注意：使用關鍵字導入時，在引用模組中的元素時不要使用模組名稱。範例：，而不是from person1["age"] mymodule.person1["age"]
#Related Pages 相關頁面
#Python Modules Tutorial Python 模組教程
#https://www.w3schools.com/python/python_modules.asp
#Create a Module 建立模組
#https://www.w3schools.com/python/gloss_python_module_create.asp
#Variables in Modules 模組中的變數
#https://www.w3schools.com/python/gloss_python_module_variables.asp
#Renaming a Module 重新命名模組
#https://www.w3schools.com/python/gloss_python_module_rename.asp
#Built-in Modules 內置模組
#https://www.w3schools.com/python/gloss_python_module_built-in.asp
#Using the dir() Function 使用 dir（） 函數
#https://www.w3schools.com/python/gloss_python_module_dir.asp
