#https://www.w3schools.com/python/ref_func_all.asp
#Python all() Function Python all()函數
#Returns True if all items in an iterable object are true
#如果可反覆運算物件中的所有項均為 true，則返回 True。
#Check if all items in a list are True:
#檢查是否清單中的所有專案均為 True：
mylist = [True, True, True]
x = all(mylist)
print(x)
#Definition and Usage 定義和用法
#The all() function returns True if all items in an iterable are true, otherwise it returns False.
#如果iterable 中的所有專案均為 true，則 all（） 函數返回 True，否則返回 False。
#If the iterable object is empty, the all() function also returns True.
#如果該可反覆運算物件為空，all（） 函數也返回 True。
#Syntax 語法
#all(iterable)
#Parameter參數：Values值
#Parameter參數：Description描述
#An iterable object (list, tuple, dictionary)
#iterable：iterable 可反覆運算物件（清單、元組、字典）
#Check if all items in a list are True:
#檢查清單中的所有專案是否為 True：
mylist = [0, 1, 1]
x = all(mylist)
print(x)
#Check if all items in a tuple are True:
#檢查元組中的所有專案是否為 True：
mytuple = (0, True, False)
x = all(mytuple)
print(x)
#Check if all items in a set are True:
#檢查集合中的所有專案是否為 True：
myset = {0, 1, 0}
x = all(myset)
print(x)
#Check if all items in a dictionary are True:
#檢查字典中的所有專案是否為 True：
mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)
print(x)
#Note: When used on a dictionary, the all() function checks if all the keys are true, not the values.
#注意：在字典上使用時，all（） 函數將檢查所有鍵是否為真，而不是值。
#Related Pages 相關頁面
#The any() Function any（） 函數

