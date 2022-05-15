#https://www.w3schools.com/python/ref_func_filter.asp
#Python filter Function Python filter函數
#Use a filter function to exclude items in an iterable object
#使用過濾器函數排除可反覆運算物件中的專案。
#Filter the array, and return a new array with only the values equal to or above 18:
#過濾陣列，並返回一個僅包含等於或大於 22 的值的新陣列：
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)
#Definition and Usage 定義和用法
#The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
#filter（） 函數返回一個反覆運算器，該反覆運算器通過一個函數對專案進行過濾以測試該專案是否可被接受。
#Syntax 語法
#filter(function, iterable)
#Parameter參數：Values值
#Parameter參數：Description描述
#function：A Function to be run for each item in the iterable
#function：測試 iterable 中每個專案的函數。
#iterable：The iterable to be filtered
#iterable：需被過濾的iterable。
