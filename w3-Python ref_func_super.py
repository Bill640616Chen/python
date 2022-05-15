#https://www.w3schools.com/python/ref_func_super.asp
#Python super() Function Python super()函數
#Returns an object that represents the parent class
#返回表示父類的物件。(繼承父類)
#Create a class that will inherit all the methods and properties from another class:
#建立一個將從另一個類繼承所有方法和屬性的類：
class Parent:
  def __init__(self, txt):
    self.message = txt
  def printmessage(self):
    print(self.message)
class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)
x = Child("Hello, and welcome!")
x.printmessage()
#Definition and Usage 定義和用法
#The super() function is used to give access to methods and properties of a parent or sibling class.
#super（） 函數用於提供對父類或同胞類的方法和屬性的訪問。
#The super() function returns an object that represents the parent class.
#super（） 函數返回代表父類的物件。
#Syntax 語法
#super()
#Parameter參數：Values值
#No parameters 無參數