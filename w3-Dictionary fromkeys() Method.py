#https://www.w3schools.com/python/ref_dictionary_fromkeys.asp
#Python Dictionary fromkeys() Method 字典fromkeys()方法
#Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
#fromkeys(x, y)先把x(tuple)跟y(值)分別為鍵與值
#然後再把fromkeys(x, y)，dict字典化
#執行完dict.fromkeys(x, y),賦予一個變數(或稱名字)
#輸出出來,就是有鍵值的字典
#fromkey(x, y)最多只能放二個參數

#Definition and Usage
#The fromkeys() method returns a dictionary with the specified keys and the specified value.

#Syntax
#dict.fromkeys(keys, value)
#Parameter Values
#Parameter：Description
#keys：Required. An iterable specifying the keys of the new dictionary
#在可迭代的字典裡指定鍵
#value：Optional. The value for all keys. Default value is None
#非必填值,預設值是None
#Same example as above, but without specifying the value:
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)
#{'key1': None, 'key2': None, 'key3': None}
a = {'key1': 1, 'key2': 2, 'key3': 3}
list1 = list(a)
print(list1) #轉換只能取鍵
tuple1 = tuple(a)
print(tuple1) #轉換只能取鍵
set1 = set(a)
print(set1) #轉換只能取鍵