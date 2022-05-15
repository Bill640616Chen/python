#https://www.w3schools.com/python/python_howto_reverse_string.asp
#How to Reverse a String in Python 如何在Python中反轉字串
#Learn how to reverse a String in Python.
#瞭解如何在 Python 中反轉字串。
#There is no built-in function to reverse a String in Python.
#在Python中沒有內置的函數來反轉字串。
#The fastest (and easiest?) way is to use a slice that steps backwards, -1.
#最快（也是最簡單的？）方法是使用向後退的切片。-1
#print("-------分隔線-------")
#Reverse the string "Hello World":
#反轉字串「Hello World」：
txt = "Hello World"[::-3]
print(txt)
#[起始:結束:步數(正數由前數,負數由後數,不能為0)]
#We have a string, "Hello World", which we want to reverse:
#我們有一個字串，「Hello World」，我們想反轉它：

print("-------分隔線-------")
#The String to Reverse 要反轉的字串
txt = "Hello World" [::-1]
print(txt)
#Create a slice that starts at the end of the string, and moves backwards.
#創建一個從字串末尾開始並向後移動的切片。
#In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards.
#在此特定示例中，slice 語句表示從字串的末尾開始，到位置 0 結束，隨步長移動，負一，這意味著向後退一步。[::-1]-1

print("-------分隔線-------")
#Slice the String 對字串進行切片
txt = "Hello World" [::-1]
print(txt)
#Now we have a string txt that reads "Hello World" backwards.
#現在我們有一個反向讀取「Hello World」的字串。txt
#Print the String to demonstrate the result
#列印字串以演示結果

print("-------分隔線-------")
#Print the List 列印清單
txt = "Hello World"[::-1]
print(txt)

print("-------分隔線-------")
#Create a Function 創建函數
#If you like to have a function where you can send your strings, and return them backwards, you can create a function and insert the code from the example above.
#如果您希望有一個函數，您可以在其中發送字串並向後返回它們，則可以創建一個函數並插入上面範例中的代碼。
def my_function(x):
  return x[::-1]
mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt)
#Create a function that takes a String as an argument.
#創建一個將字串作為參數的函數。

print("-------分隔線-------")
#Create a Function 創建函數
def my_function(x):
  return x[::-1]
mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt)
#Slice the string starting at the end of the string and move backwards.
#從字串末尾開始對字串進行切片，然後向後移動。

print("-------分隔線-------")
#Slice the String 對字串進行切片
def my_function(x):
  return x [::-1]
mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt)
#Return the backward String 返回向後字串

print("-------分隔線-------")
#Return the String 返回字串
def my_function(x):
  return x[::-1]
mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt )
#Call the function, with a string as a parameter:
#呼叫該函數，並將字串作為參數：

print("-------分隔線-------")
#Call the Function 調用函數
def my_function(x):
  return x[::-1]
mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt)
#Print the result:列印結果：

print("-------分隔線-------")
#Print the Result 列印結果
def my_function(x):
  return x[::-1]
mytxt = my_function("I wonder how this text looks like backwards")
print(mytxt)
