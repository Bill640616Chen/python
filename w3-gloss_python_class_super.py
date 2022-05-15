#https://www.w3schools.com/python/gloss_python_super.asp
#super() Function 繼承函數
#Python also has a function that will make the child class inherit all the methods and properties from its parent:super()
#Python 還具有使子類從其父類繼承所有方法和屬性的功能：super()
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#By using the function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.super()
#通過使用該功能，您不必使用父元素的名稱，它會自動從父類繼承方法和屬性。super()
#Related Pages 相關頁面
#Python Inheritance Tutorial Python 繼承教程
#https://www.w3schools.com/python/python_inheritance.asp
#Create Parent Class 創建父類
#https://www.w3schools.com/python/gloss_python_parent_class.asp
#Create Child Class 創建子類
#https://www.w3schools.com/python/gloss_python_child_class.asp
#Create the __init__() Function 創建__init__（） 功能
#https://www.w3schools.com/python/gloss_python_create_init.asp
#Add Class Properties 添加類屬性
#https://www.w3schools.com/python/gloss_python_class_add_properties.asp
#Add Class Methods 添加類方法
#https://www.w3schools.com/python/gloss_python_class_add_methods.asp