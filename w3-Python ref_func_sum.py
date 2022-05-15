#https://www.w3schools.com/python/ref_func_sum.asp
#Python sum() Function Python sum()函數
#Sums the items of an iterator
#對反覆運算器的項目進行求和。
#Add all items in a tuple, and return the result:
#將所有項添加到一個元組中，並返回結果：
a = (1, 2, 3, 4, 5)
x = sum(a)
print(x)
#Definition and Usage 定義和用法
#The sum() function returns a number, the sum of all items in an iterable.
#sum（） 函數返回一個數位，即 iterable 中所有專案的總和。
#Syntax 語法
#sum(iterable, start)
#Parameter參數：Values值
#Parameter參數：Description描述
#iterable：Required. The sequence to sum
#必需。 需求和的序列。
#start：Optional. A value that is added to the return value
#可選。 添加到返回值的值。
#Start with the number 7, and add all the items in a tuple to this number:
#以數位 6 開頭，並將元組中的所有專案加到該數位：
a = (1, 2, 3, 4, 5)
x = sum(a, 7)
print(x)
