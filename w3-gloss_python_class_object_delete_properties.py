#https://www.w3schools.com/python/gloss_python_object_delete_properties.asp
#Delete Object Properties 刪除物件屬性
#Delete Object Properties
#You can delete properties on objects by using the keyword: del
#您可以使用關鍵字刪除物件上的屬性： del
#Delete the age property from the p1 object:
#從 p1 物件中移除年齡屬性：
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
print(p1.age)
#AttributeError: 'Person' object has no attribute 'age'
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
#Modify Object Properties 修改物件屬性
#https://www.w3schools.com/python/gloss_python_object_modify_properties.asp
#Delete Object 刪除物件
#https://www.w3schools.com/python/gloss_python_object_delete.asp
#Class pass Statement 類pass語句
#https://www.w3schools.com/python/gloss_python_class_pass.asp