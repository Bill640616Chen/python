#https://www.w3schools.com/python/numpy/numpy_ufunc.asp
#NumPy ufuncs 通用函数
#What are ufuncs? 什麼是 ufuncs？
#ufuncs stands for "Universal Functions" and they are NumPy functions that operates on the ndarray object.
#ufuncs 指的是"通用函數"（Universal Functions），它們是對 ndarray 對象進行操作的 NumPy 函數。
#Why use ufuncs? 為什麼要使用 ufuncs？
#ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
#ufunc 用於在 NumPy 中實現矢量化，這比反覆運算元素要快得多。
#They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
#它們還提供廣播和其他方法，例如減少、累加等，它們對計算非常有説明。
#ufuncs also take additional arguments, like:
#ufuncs 還接受其他參數，比如：
#where boolean array or condition defining where the operations should take place.
#where 布爾值陣列或條件，用於定義應在何處進行操作。
#dtype defining the return type of elements.
#dtype 定義元素的返回類型。
#out output array where the return value should be copied.
#out 返回值應被複製到的輸出陣列。
#What is Vectorization? 什麼是向量化？
#Converting iterative statements into a vector based operation is called vectorization.
#將反覆運算語句轉換為基於向量的操作稱為向量化。
#It is faster as modern CPUs are optimized for such operations.
#由於現代 CPU 已針對此類操作進行了優化，因此速度更快。
#Add the Elements of Two Lists
#對兩個清單的元素進行相加：
#list 1: [1, 2, 3, 4]
#list 2: [4, 5, 6, 7]
#One way of doing it is to iterate over both of the lists and then sum each elements.
#一種方法是遍歷兩個清單，然後對每個元素求和。
#Without ufunc, we can use Python's built-in zip() method:
print("----------------------------如果沒有 ufunc")
#如果沒有 ufunc，我們可以使用 Python 的內置 zip（） 方法：
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z) #[5, 7, 9, 11]
#NumPy has a ufunc for this, called add(x, y) that will produce the same result.
#對此，NumPy 有一個 ufunc，名為 add（x， y），它會輸出相同的結果。
#With ufunc, we can use the add() function:
print("---------通過 ufunc，我們可以使用 add（） 函數")
#通過 ufunc，我們可以使用 add（） 函數：
import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z) #[ 5  7  9 11]
