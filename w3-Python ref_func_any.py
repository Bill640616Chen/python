#https://www.w3schools.com/python/ref_func_any.asp
#Python any() Function Python any()函數
#Returns True if any item in an iterable object is true
#如果可反覆運算物件中的任何項為 true，則返回 True。
#Check if any of the items in a list are True:
#檢查清單中的任何專案是否為 True：
mylist = [False, True, False]
x = any(mylist)
print(x)
#Definition and Usage 定義和用法
#The any() function returns True if any item in an iterable are true, otherwise it returns False.
#如果iterable中的任何一項為 true，則 any（） 函數返回 True，否則返回 False。
#If the iterable object is empty, the any() function will return False.
#如果可反覆運算物件為空，則 any（） 函數將返回 False。
#Syntax 語法
#any(iterable)
#Parameter參數：Values值
#Parameter參數：Description描述
#iterable：An iterable object (list, tuple, dictionary)
#iterable：iterable 可反覆運算物件（清單、元組、字典）
#Check if any item in a tuple is True:
#檢查元組中的任何專案是否為 True：
mytuple = (0, 1, False)
x = any(mytuple)
print(x)
#Check if any item in a set is True:
#檢查集合中的任何專案是否為 True：
myset = {0, 1, 0}
x = any(myset)
print(x)
#Check if any item in a dictionary is True:
#檢查字典中的任何專案是否為 True：
mydict = {0 : "Apple", 1 : "Orange"}
x = any(mydict)
print(x)
#Note: When used on a dictionary, the any() function checks if any of the keys are true, not the values.
#註釋：在字典上使用時，any（） 函數將檢查是否有任何鍵為真，而不是值。
#Related Pages 相關頁面
#The all() Function all（） 函數
#any()預設非boolean值為True