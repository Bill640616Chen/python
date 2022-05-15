#https://www.w3schools.com/python/ref_func_max.asp
#Python max() Function Python max()函數
#Returns the largest item in an iterable
#返回可反覆運算物件中的最大專案。
#Return the largest number:
#傳回最大數：
x = max(5, 10)
print(x)
#Definition and Usage 定義和用法
#The max() function returns the item with the highest value, or the item with the highest value in an iterable.
#max（） 函數返回有最大值的專案，或者iterable中有最大值的專案。
#If the values are strings, an alphabetically comparison is done.
#如果值是字串，則按字母順序進行比較。
#Syntax 語法
#max(n1, n2, n3, ...)
#Parameter參數：Values值
#Parameter參數：Description描述
#n1, n2, n3, ...	One or more items to compare 一個或多個要比較的專案。
#Or:或者：
#max(iterable)
#Parameter參數：Description描述
#iterable：An iterable, with one or more items to compare
#iterable 可反覆運算物件，包含一個或多個供比較的專案。
#Return the name with the highest value, ordered alphabetically:
#返回擁有最高值的名字，按字母順序排列：
x = max("Mike", "John", "Vicky")
print(x)
#Return the item in a tuple with the highest value:
#傳回tuple中具有最高值的專案：
a = (1, 5, 3, 9)
x = max(a)
print(x)
#Related Pages 相關頁面
#The min() function, to return the lowest value.
#min（） 函數（返回最低值）
