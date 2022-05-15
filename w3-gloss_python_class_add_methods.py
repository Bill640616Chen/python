#https://www.w3schools.com/python/gloss_python_class_add_properties.asp
#Add Class Properties 繼承函數
#Add a method called to the class:welcomeStudent
#添加到類中的方法：welcomeStudent
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", x.firstname, x.lastname, "to the class of", x.graduationyear)
   #print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
   #用父類的屬性,輸出的結果一樣
x = Student("Mike", "Olsen", 2019)
x.welcome()
#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
#如果在兒童類中添加與父類功能相同的名稱方法，則父級方法的繼承將被推翻。
#Related Pages 相關頁面
#Python Inheritance Tutorial Python 繼承教程
#https://www.w3schools.com/python/python_inheritance.asp
#Create Parent Class 創建父類
#https://www.w3schools.com/python/gloss_python_parent_class.asp
#Create Child Class 創建子類
#https://www.w3schools.com/python/gloss_python_child_class.asp
#Create the __init__() Function 創建__init__（） 功能
#https://www.w3schools.com/python/gloss_python_create_init.asp
#super Function 繼承函數
#https://www.w3schools.com/python/gloss_python_super.asp
#Add Class Properties 添加類屬性
#https://www.w3schools.com/python/gloss_python_class_add_properties.asp
