#https://www.w3schools.com/python/python_operators.asp
#Python Operators
#Operators are used to perform operations on variables and values.
#操作員用於對變數和值執行操作。
#In the example below, we use the operator to add together two values:+
#In the example below, we use the operator to add together two values:+
print(10 + 5) #15
#Python divides the operators in the following groups:
#Python 將操作員分為以下組
#Identity operators   身份操作員
#Identity operators are used to compare the objects, not if they
#are equal, but if they are actually the same object, with the same memory location:
#身份操作員用於比較物件，而不是等於它們，而是它們實際上是同一物件，具有相同的記憶體位置：
#Operator	Description	                            Example	
#is 	    Returns True if both variables are      x is y
#           the same object		
#           如果兩個變數是同一物件，則傳回True
#is not	    Returns True if both variables are      x is not y
#           not the same object	
#           如果兩個變數不是同一物件，則傳回True
x = ["apple", "banana"] #x就是記憶位址
y = ["apple", "banana"] #y就是記憶位址
z = x
#每次宣告就是向記憶體要一個位址呀
print(x is z) #True
print(x is y) #False,並沒宣告x=y,兩個是不同的記憶位址
print(x == y) #True,比較運算子是比內容而不是比記憶位址

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z) #False
print(x is not y) #True,並沒宣告x=y
print(x != y)     #False,並沒宣告x=y