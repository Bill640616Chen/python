#https://www.w3schools.com/python/ref_func_sorted.asp
#Python sorted() Function Python sorted()函數
#Returns a sorted list
#返回排序列表。
#Sort a tuple:
#對元組排序：
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)
#Definition and Usage 定義和用法
#The sorted() function returns a sorted list of the specified iterable object.
#sorted（） 函數傳回指定的可反覆運算物件的排序列表。
#You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
#您可以指定升序或降序。 字串按字母順序排序，數位按數位排序。
#Note: You cannot sort a list that contains BOTH string values AND numeric values.
#註釋：您無法對同時包含字串值和數位值的清單進行排序。
#Syntax 語法
#sorted(iterable, key=key, reverse=reverse)
#Parameter參數：Values值
#Parameter參數：Description描述
#iterable：Required. The sequence to sort, list, dictionary, tuple etc.
#iterable：必需。 要排序的序列，清單、字典、元組等等。
#key：Optional. A Function to execute to decide the order. Default is None
#key：可選。 執行以確定順序的函數。 預設為 None。
#reverse：Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
#reverse：可選。 布爾值。 False 將按升序排序，True 將按降序排序。 默認為 False。
#Sort numeric:
print('-------------分隔線------------')
#數值排序：
a = (1, 11, 2)
x = sorted(a)
print(x)
#Sort ascending:
print('-------------分隔線------------')
#升序排序：
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a)
print(x)
#Sort descending:
print('-------------分隔線------------')
#降序排序：
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)
#排序完傳回值,均是清單