#https://www.w3schools.com/python/python_howto_remove_duplicates.asp
#How to Remove Duplicates From a Python List 如何從 Python 清單中刪除重複項
#Learn how to remove duplicates from a List in Python.
#學習如何從 Python 中的 List 中刪除重複項。
print("-------從清單中移除任何重複項目")
#Remove any duplicates from a List:
#從清單中移除任何重複項目：
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)
#First we have a List that contains duplicates:
#首先，我們有一個包含重複項的 List：

print("-------包含重複項的清單")
#A List with Duplicates
#包含重複項的清單
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)
#Create a dictionary, using the List items as keys. This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
#使用清單項作為鍵創建字典。 這將自動刪除任何重複項，因為詞典不能有重複的鍵。

print("-------創建字典")
#Create a Dictionary 創建字典
mylist = ["a", "b", "a", "c", "c"]
mylist = list( dict.fromkeys(mylist) )
print(mylist)
#Then, convert the dictionary back into a list:
#然後，將字典轉換回清單：

print("-------轉換為 List")
#Convert Into a List 轉換為 List
mylist = ["a", "b", "a", "c", "c"]
mylist = list( dict.fromkeys(mylist) )
print(mylist)
#Now we have a List without any duplicates, and it has the same order as the original List.
#現在我們有一個沒有任何重複的 List，它與原始 List 擁有相同的順序。

print("-------列印 List")
#Print the List to demonstrate the result
#列印清單以演示結果：
#Print the List 列印 List
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

print("-------創建函數")
#Create a Function 創建函數
#If you like to have a function where you can send your lists, and get them back without duplicates, you can create a function and insert the code from the example above.
#如果您希望有一個函數可以發送清單，然後它們返回的無重複項，則可以創建函數並插入上例中的代碼。
def my_function(x):
  return list(dict.fromkeys(x))
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)

print("-------創建函數")
#Create a function that takes a List as an argument.
#創建一個以 List 作為參數的函數。
#Create a Function
def my_function(x):
  return list(dict.fromkeys(x))
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)
#Create a dictionary, using this List items as keys.
#使用此 List 項作為鍵創建字典。

print("-------創建字典")
#Create a Dictionary 創建字典
def my_function(x):
  return list( dict.fromkeys(x) )
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)
#Convert the dictionary into a list.
#將字典轉換為清單：

print("-------轉換為清單")
#Convert Into a List 轉換為清單
def my_function(x):
  return list( dict.fromkeys(x) )
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)
#Return the list 傳回清單：

print("-------返回清單")
#Return List 返回清單
def my_function(x):
  return list(dict.fromkeys(x))
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)
#Call the function, with a list as a parameter:
#使用清單作為參數來呼叫函數：

print("-------調用函數")
#Call the Function 調用函數
def my_function(x):
  return list(dict.fromkeys(x))
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)
#Print the result:列印結果：

print("-------列印結果")
#Print the Result 列印結果
def my_function(x):
  return list(dict.fromkeys(x))
mylist = my_function(["a", "b", "a", "c", "c"])
print(mylist)
