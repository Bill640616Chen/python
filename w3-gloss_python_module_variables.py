#https://www.w3schools.com/python/gloss_python_module_variables.asp
#Module Variables 模組變數
#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):
#該模組可以包含函數，如前所述，也可以包含所有類型的變數（陣列，字典，物件等）：
#Save this code in the file mymodule.py
#將此代碼保存在檔中mymodule.py
'''person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
'''
#Import the module named mymodule, and access the person1 dictionary:
#導入名為 mymodule 的模組，並訪問 person1 字典：
import mymodule
a = mymodule.person1["age"]
print(a)
#Related Pages 相關頁面
#Python Modules Tutorial Python 模組教程
#https://www.w3schools.com/python/python_modules.asp
#Create a Module 建立模組
#https://www.w3schools.com/python/gloss_python_module_create.asp
#Renaming a Module 重新命名模組
#https://www.w3schools.com/python/gloss_python_module_rename.asp
#Built-in Modules 內置模組
#https://www.w3schools.com/python/gloss_python_module_built-in.asp
#Using the dir() Function 使用 dir（） 函數
#https://www.w3schools.com/python/gloss_python_module_dir.asp
#Import From Module 從模組導入
#https://www.w3schools.com/python/gloss_python_module_import_from.asp