#https://www.w3schools.com/python/python_syntax.asp
#Python Indentation
#Python 程式內縮(縮排)
if 5 > 2:#只能寫邏輯為True，否則無法輸出
  print("Five is greater than two!")
#if 5 > 2:
#print("Five is greater than two!")
#expected an indented block(一定要內縮,否則會有錯誤)
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        a="Five is greater than two!"
        print(a)

if 5 > 2:
 print("Five is greater than two!")
#print("Five is greater than two!")
#您必須在同一代碼塊中使用相同數量的空間，否則 Python 會給您一個錯誤：

#Python 變數
x = 5
#x為變數,5是值,型別int
y = "Hello, World!"
#y為變數,"Hello, World!"是值,型別字串
print(x,y)

a = 1
b = 'abc'
c = 2
print(a,b,c)

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)#Sally,第二次宣告取代了原來的值

#鑄造 如果要指定變數的數據類型，則可以通過鑄造完成。
x = str(3)    # x will be '3',字串
y = int(3)    # y will be 3,int
z = float(3)  # z will be 3.0,float小數點
print(x,y,z)

#獲取類型 您可以通過該函數獲取可變數的數據類型。type
x = 5       #int
y = "John"  #str
z = 3.12    #float
print(type(x))
print(type(y))
print(type(z))

#單報價還是雙報價？字串變數可以通過使用單報價或雙報價進行聲明：
#""是雙報價,''是單報價
x = "John"
# is the same as
x = 'John'
print(x)

#案例敏感 可變名稱對案例敏感。
a = 4
A = "Sally"
#A will not overwrite a
print(a,A)