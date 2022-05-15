#https://www.w3schools.com/python/gloss_python_class_add_properties.asp
#Add Class Properties 繼承函數
#Add a property called to the class:graduationyearStudent
#新增到類別的屬性：graduationyearStudent
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
x = Student("Mike", "Olsen")
print(x.graduationyear)
#In the example below, the year should be a variable, and passed into the class when creating student objects. To do so, add another parameter in the __init__() function:2019Student
#在下面的示例中，該年應該是一個變數，並在創建學生對象時傳遞到課堂中。為此，在__init__（）函數中添加另一個參數：2019Student
#Add a parameter, and pass the correct year when creating objects:year
#新增參數，並在建立物件時通過正確的年份：year
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
x = Student("Mike", "Olsen", 2019)
#因為子類__init__改可放4個變數,故x=Person("Mike", "Olsen", 2019)
#會出現錯誤,是因為父類只能放3變數
print(x.graduationyear)
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
#Add Class Methods 添加類方法
#https://www.w3schools.com/python/gloss_python_class_add_methods.asp