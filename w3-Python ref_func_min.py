#https://www.w3schools.com/python/ref_func_min.asp
#Python min() Function Python min()函數
#Returns the smallest item in an iterable
#返回可反覆運算物件中的最小專案。
#Return the lowest number:
#返回最小數：
x = min(5, 10)
print(x)
#Definition and Usage 定義和用法
#The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.
#min（） 函數傳回值最小的專案，或 iterable 中值最小的專案。
#If the values are strings, an alphabetically comparison is done.
#如果值是字串，則按字母順序進行比較。
#Syntax 語法
#min(n1, n2, n3, ...)
#min(iterable)
#Parameter參數：Values值
#Parameter參數：Description描述
#n1, n2, n3, ...	One or more items to compare　要比較的一個或多個專案。
#Or:或者：
#Parameter參數：Description描述
#iterable：An iterable, with one or more items to compare
#iterable：iterable 有一個或多個要比較的專案的可反覆運算物件。
#Return the name with the lowest value, ordered alphabetically:
#依字母順序傳回值最小的名字：
x = min("Mike", "John", "Vicky")
print(x)
#Return the item in a tuple with the lowest value:
#傳回元群組中值最小的專案：
a = (1, 5, 3, 9)
x = min(a)
print(x)
#Related Pages 相關頁面
#The max() function, to return the highest value.
#max（） 函數（返回最大值）

