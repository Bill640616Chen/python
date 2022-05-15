#https://www.w3schools.com/python/python_booleans.asp
#Python Booleans
#Booleans represent one of two values: or .True False
#Booleans代表2種值其中之一或是True False
#Boolean Values(Boolean值)
#In programming you often need to know if an expression is or .TrueFalse
#在程式設計中，您通常需要知道如果一個表達式"是"或者".TrueFalse"
#You can evaluate any expression in Python, and get one of two answers, or .TrueFalse
#您可以評估 Python 中的任何表達方式，並取得兩個答案之一，或者 .TrueFalse
#When you compare two values, the expression is evaluated and Python returns the Boolean answer:
#當您比較兩個值時，會評估該表示值，Python 會傳回 Boolean 答案：
print(10 > 9)  #True
print(10 == 9) #False
print(10 < 9)  #False
#When you run a condition in an if statement, Python returns or :TrueFalse
#當你運行一個條件在一個如果陳述裡,Python 傳回或：TrueFalse
#Print a message based on whether the condition is or :TrueFalse
#列印一個訊息基於是否該條件是或者 :TrueFalse
a = 200
b = 33
if b > a: #如果b>a
  print("b is greater than a")
else: #否則
  print("b is not greater than a")
  #b is not greater than a
#Evaluate Values and Variables評估值和變數
#The function allows you to evaluate any value, and give you or in return,bool()TrueFalse
#該功能允許您評估任何價值，並給予您或作為傳回，bool（）TrueFalse
#Evaluate a string and a number:
#評做字串和數字
print(bool("Hello")) #True
print(bool(15))      #True
#Evaluate two variables:
#評估兩個變數
x = "Hello"
y = 15
print(bool(x))       #True
print(bool(y))       #True

#Most Values are True
#大部分的值都是True
#Almost any value is evaluated to if it has some sort of content.True
#幾乎任何值都被評估if有某種內容。True
#Any string is , except empty strings.True
#任何字串都是True，除了空字串不是True。
#Any number is , except .True0
#任何號碼都是True，除了0不是True
#Any list, tuple, set, and dictionary are , except empty ones.True
#任何列表,元組,集合和字典都是True,除了空的不是True
#The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
print(bool("abc")) #True
print(bool(" ")) #True,空白也是
print(bool(123)) #True
print(bool(["apple", "cherry", "banana"])) #True
print(bool([""])) #True,列表裡有空字串
print(bool({""})) #True,字典裡有空字串,無鍵值也沒關係
#Some Values are False一些值是False
#In fact, there are not many values that evaluate to , 
# except empty values, such as , , , , the number , and the value . 
# And of course the value evaluates to .
#事實上，沒有多少值可以評估到，除了空值，諸如數字和值，當然價值評估
#False () [] {} "" 0 None False False
print(bool(False)) #False
print(bool(None)) #False
print(bool(0)) #False,數字0
print(bool("")) #False,空字串
print(bool(())) #False,空tuple
print(bool([])) #False,空list
print(bool({})) #False,空dict
#One more value, or object in this case, evaluates to , and that is if you have an object that is made from a class with a function that returns or :
#在這種情況下，還有一個值或物件會評估到，即如果您有一個物件，該物件是由具有傳回功能的類構成的，或者：
#False __len__ 0 False
# __len__(為了讓len()工作正常,類必須提供一個特殊方法,傳回元素的個數)
class myclass():
#class是一個關鍵字，告訴系統我們要定義一個類，class後面加一個空格然後加類名。
  def __len__(self): #(self)為值
    #類內部定義的函數一般稱為方法 def
    return 0 #改為1後,列印結果為True
    #如果您分配了一個值，則返回值為無值，在這種情況下，要返回0，
    #則價值0將由函數返回，當返回關鍵字和值達到時，功能將結束。
myobj = myclass() 
print(bool(myobj)) #False

#理解
#class myclass():
#def __len__(self):
#return 0
#我突然想到這樣理解,class(類別)mycalss(汽車):def __len__(self)
#是定義方向盤怎麼動,所以要傳回一個值回來,才知道方向盤的狀況Return 0，代表動不了QQ
#田為這個汽車(myclass)裡的零件__len__(self)傳回來0,所以myclass()=0
#myobj(車子的型號) = 0
#print(bool(myobj)) #False 報表印出來,當然是False

#Functions can Return a Boolean
#You can create functions that returns a Boolean Value:
#Print the answer of a function:
def myFunction() : #def(定義)裡是都是功能
  return True
print(myFunction()) #True
#You can execute code based on the Boolean answer of a function:
#你可以根據函式回傳的是或否的答案來執行不同程式
#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True
if myFunction(): #if條件都為True
  print("YES!")
else:
  print("NO!")
  #YES!
#Python also has many built-in functions that return a boolean value, 
#like the function, which can be used to determine if an object is of a certain data type:isinstance()
#Python 還具有許多內置功能，可返回布爾值，如該函數，可用於確定物件是否具有特定資料類型：靜置（）
#Check if an object is an integer or not:
#檢查該物件是否是int
x = 200
print(isinstance(x, int)) #True
def myFunction() :
  return False
if myFunction(): #if條件都為True
  print("YES!")
else:
  print("NO!") #NO!