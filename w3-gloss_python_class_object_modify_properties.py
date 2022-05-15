#https://www.w3schools.com/python/gloss_python_object_modify_properties.asp
#Modify Object Properties 修改物件屬性
#You can modify properties on objects like this:
#您可以修改此類物件上的屬性：
#Set the age of p1 to 40:
#設定 p1 到 40 的年齡：
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)
#Related Pages 相關頁面
#Python Syntax Tutorial Python 語法教程
#https://www.w3schools.com/python/python_classes.asp
#Class 類
#https://www.w3schools.com/python/gloss_python_class.asp
#Create Class 創建類
#https://www.w3schools.com/python/gloss_python_class_create.asp
#The Class __init__() Function 類__init__（） 功能
#https://www.w3schools.com/python/gloss_python_class_init.asp
#Object Methods 物件方法
#https://www.w3schools.com/python/gloss_python_object_methods.asp
#self 自我
#https://www.w3schools.com/python/gloss_python_self.asp
#Delete Object Properties 刪除物件屬性
#https://www.w3schools.com/python/gloss_python_object_delete_properties.asp
#Delete Object 刪除物件
#https://www.w3schools.com/python/gloss_python_object_delete.asp
#Class pass Statement 類pass語句
#https://www.w3schools.com/python/gloss_python_class_pass.asp