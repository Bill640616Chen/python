#https://www.w3schools.com/python/gloss_python_parent_class.asp
#Create Parent Class 建立父類
#Any class can be a parent class, so the syntax is the same as creating any other class:
#任何類都可以是父類，因此語法與創建任何其他類相同：
#Create a class named , with and properties, and a method:Personfirstnamelastnameprintname
#建立命名的類別、屬性與屬性以及方法：Personfirstnamelastnameprintname
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
#使用 Person 類建立物件，然後執行 printname 方法：
x = Person("John", "Doe")
x.printname()
#Related Pages 相關頁面
#Python Inheritance Tutorial Python 繼承教程
#https://www.w3schools.com/python/python_inheritance.asp
#Create Child Class 創建子類
#https://www.w3schools.com/python/gloss_python_child_class.asp
#Create the __init__() Function 創建__init__（） 功能
#https://www.w3schools.com/python/gloss_python_create_init.asp
#super Function 繼承函數
#https://www.w3schools.com/python/gloss_python_super.asp
#Add Class Properties 添加類屬性
#https://www.w3schools.com/python/gloss_python_class_add_properties.asp
#Add Class Methods 添加類方法
#https://www.w3schools.com/python/gloss_python_class_add_methods.asp