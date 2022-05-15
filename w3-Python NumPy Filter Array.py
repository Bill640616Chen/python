#https://www.w3schools.com/python/numpy/numpy_array_filter.asp
#NumPy Filter Array 陣列過濾
#Filtering Arrays 陣列過濾
#Getting some elements out of an existing array and creating a new array out of them is called filtering.
#從現有陣列中取出一些元素並從中創建新陣列稱為過濾（filtering）。
#In NumPy, you filter an array using a boolean index list.
#在 NumPy 中，我們使用boolean索引清單來過濾數位。
#A boolean index list is a list of booleans corresponding to indexes in the array.
#boolean索引清單是與陣列中的索引相對應的boolean值清單。
#If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
#如果索引處的值為 True，則該元素包含在過濾後的陣列中;如果索引處的值為 False，則該元素將從過濾後的數位中排除。
#Create an array from the elements on index 0 and 2:
print("--------------用索引 0 和 2、4 上的元素建立一個陣列：")
#用索引 0 和 2上的元素建立一個陣列：
import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
#用boolean當索引取元素建立一個陣列,只要是False,元素就會被過濾掉
print(newarr)
#The example above will return [41, 43], why?
#上例將返回 [41, 43]，為什麼？
#Because the new filter contains only the values where the filter array had the value True, in this case, index 0 and 2.
#因為新篩檢程式僅包含過濾器陣列有值 True 的值，所以在這種情況下，索引為 0 和 2。

print("--------------------------------------創建過濾器陣列")
#Creating the Filter Array 創建過濾器陣列
#In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.
#在上例中，我們對 True 和 False 值進行了硬編碼，但通常的用途是根據條件創建篩檢程式陣列。
#Create a filter array that will return only values higher than 42:
#建立一個僅傳回大於 42 的值的過濾器陣列：
import numpy as np
arr = np.array([41, 42, 43, 44])
# Create an empty list
#建立一個空清單
filter_arr = []
# go through each element in arr
#遍歷arr 中的每個元素
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
#如果元素大於 42，則將值設置為 True，否則為 False：
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
#[False, False, True, True]
print(newarr)
#[43 44]

print("--------建立過濾器陣列，該陣列僅傳回原始數位中的偶數元素")
#Create a filter array that will return only even elements from the original array:
#建立過濾器陣列，該陣列僅傳回原始數位中的偶數元素：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Create an empty list
#建立一個空清單
filter_arr = []
# go through each element in arr
#遍歷arr 中的每個元素
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
#如果元素可以被 2 整除，則將值設置為 True，否則設置為 False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
#[False, True, False, True, False, True, False]
print(newarr)
#[2 4 6]

print("-----------------------------直接從陣列建立過濾器")
#Creating Filter Directly From Array 直接從陣列建立過濾器
#The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.
#上例是 NumPy 中非常常見的任務，NumPy 提供了解決該問題的好方法。
#We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.
#我們可以在條件中直接替換陣列而不是iterable變數，它會如我們期望地那樣工作。
#Create a filter array that will return only values higher than 42:
#建立一個僅傳回大於 42 的值的過濾器陣列：
import numpy as np
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
#[False False  True  True]
print(newarr)
#[43 44]

print("------------------變數測試----直接從陣列建立過濾器")
import numpy as np
x = np.array([1,2,3,4])
filter_x = x > 1
newarr = x[filter_x]
print(filter_x)
print(newarr)

print("-------建立過濾器陣列，該陣列僅傳回原始數位中的偶數元素")
#Create a filter array that will return only even elements from the original array:
#建立過濾器陣列，該陣列僅傳回原始數位中的偶數元素：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)