#https://www.w3schools.com/python/gloss_python_object_methods.asp
#Object Methods __init__()函數
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#物件也可以包含方法。物件中的方法是屬於物件的函數。
#Let us create a method in the Person class:
#讓我們在人員類中創建一種方法：
#Insert a function that prints a greeting, and execute it on the p1 object:
#插入列印問候語的功能，並在 p1 物件上執行：
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
#Note: The parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.self
#注意：參數是該類當前實例的引用，用於訪問屬於該類的變數。self
#Related Pages 相關頁面
#Python Syntax Tutorial Python 語法教程
#https://www.w3schools.com/python/python_classes.asp
#Class 類
#https://www.w3schools.com/python/gloss_python_class.asp
#Create Class 創建類
#https://www.w3schools.com/python/gloss_python_class_create.asp
#The Class __init__() Function 類__init__（） 功能
#https://www.w3schools.com/python/gloss_python_class_init.asp
#self 自我
#https://www.w3schools.com/python/gloss_python_self.asp
#Modify Object Properties 修改物件屬性
#https://www.w3schools.com/python/gloss_python_object_modify_properties.asp
#Delete Object Properties 刪除物件屬性
#https://www.w3schools.com/python/gloss_python_object_delete_properties.asp
#Delete Object 刪除物件
#https://www.w3schools.com/python/gloss_python_object_delete.asp
#Class pass Statement 類pass語句
#https://www.w3schools.com/python/gloss_python_class_pass.asp