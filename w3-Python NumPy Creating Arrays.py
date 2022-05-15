#https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
#NumPy Creating Arrays 創建 array 
#Create a NumPy ndarray Object 創建 NumPy ndarray 物件
#ndarray(number dimension array)它是多維度的同數據類型的陣列
#NumPy is used to work with arrays. The array object in NumPy is called ndarray.
#NumPy 用於處理陣列。 NumPy 中的陣列物件稱為 ndarray。
#We can create a NumPy ndarray object by using the array() function.
#我們可以使用array（） 函數創建一個 NumPy ndarray 物件。
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
#type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.
#type（）： 這個內置的 Python 函數告訴我們傳遞給它的物件的類型。 像上面的代碼一樣，它表明arr是 numpy.ndarray 類型。
#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:
#要創建 ndarray，我們可以將清單、元組或任何類似數位的對象傳遞給 array（） 方法，然後它將被轉換為 ndarray：
#Use a tuple to create a NumPy array:
#使用元組建立 NumPy 陣列：
import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)

print("-------------------Dimensions in Arrays 陣列中的維度")
#Dimensions in Arrays 陣列中的維度
#A dimension in arrays is one level of array depth (nested arrays).
#陣列的維度是一個陳列深度(陣列中的陳列)的等級
#nested array: are arrays that have arrays as their elements.
#陣列中的陳列：指的是將陣列作為元素的陣列
print("---------------------------------------------0維陣列")
#0-D Arrays 0維度陣列
#0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
#0-D 陣列，或標量（Scalars），是陣列中的元素。 陣列中的每個值都是一個 0-D 陣列。
#Create a 0-D array with value 42
# 0維是一點，沒有長度。
# 1維是線，只有長度。
# 2維是一個平面，是由長度和寬度（或曲線）形成面積。
# 3維是2維加上高度形成「體積面」
#用值42建0-D維度陣列
import numpy as np
arr = np.array(42)
print(arr)
#只有一個值代表是0維只有一點,那一點代表42

print("---------------------------------------------1維陣列")
#1-D Arrays 1維陣列
#An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
#陣列有0維陣列元素,稱做為1維或1維陣列
#These are the most common and basic arrays.
#這是最常見和基礎的陣列。
#Create a 1-D array containing the values 1,2,3,4,5:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
#就算array[1,2]只有二個數字,就是1維,一個數字稱做0維
print(arr)

print("---------------------------------------------2維陣列")
#2-D Arrays 2維陣列
#An array that has 1-D arrays as its elements is called a 2-D array.
#陣列有1維陣列元素,稱做為2維或2維陣列
#These are often used to represent matrix or 2nd order tensors.
#它們通常用於表示矩陣或二階張量。
#NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
#NumPy 有一個專門用於矩陣運算的完整子模組 numpy.mat。
#Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
#建立包含值 1、2、3 和 4、5、6 兩個陣列的 2-D 陣列：
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
#二組陣列是為二維
print(arr)
np.array

print("---------------------------------------------3維陣列")
#3-D arrays 3維陣列
#An array that has 2-D arrays (matrices) as its elements is called 3-D array.
#陣列有2維陣列元素(矩陣),稱做為3維或3維陣列
#These are often used to represent a 3rd order tensor.
#這些通常用來表示第三階張力器
#Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
#用兩個 2-D 陣列創建一個 3-D 陣列，這兩個陣列均包含值 1、2、3 和 4、5、6 的兩個陣列：
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#用兩個2維陣列創建一個3維陣列
print(arr)

print("-----------------------------------------ndim檢查維數")
#Check Number of Dimensions? 檢查維數？
#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
#NumPy 陣列提供了 ndim 屬性，該屬性返回一個整數，該整數會告訴我們陣列有多少維。
#Check how many dimensions the arrays have:
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim) #0
print(b.ndim) #1
print(c.ndim) #2
print(d.ndim) #3

print("----------------------------------ndmin=int更高維的陣列")
#Higher Dimensional Arrays 更高維的陣列
#An array can have any number of dimensions.
#陣列可以擁有任意數量的維。
#When the array is created, you can define the number of dimensions by using the ndmin argument.
#在創建陣列時，可以使用 ndmin 參數定義維數。
#Create an array with 5 dimensions and verify that it has 5 dimensions:
#創建一個有5個維度的陣列，並驗證它擁有5個維度：
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr) #[[[[[1 2 3 4]]]]],根據最外圍的[]有幾個就是幾維
print('number of dimensions :', arr.ndim)
#number of dimensions : 5
#In this array the innermost dimension (5th dim) has 4 elements, 
# the 4th dim has 1 element that is the vector, the 3rd dim 
# has 1 element that is the matrix with the vector, the 2nd dim 
# has 1 element that is 3D array and 1st dim has 1 element 
# that is a 4D array.
#在此陣列中，最裡面的維度（第 5 個 dim）有 4 個元素，第 4 個 dim 
# 有 1 個元素作為向量，第 3 個 dim 具有 1 個元素是與向量的矩陣，
# 第 2 個 dim 有 1 個元素是 3D 陣列，而第 1 個 dim 有 1 個元素，
# 該元素是 4D 陣列。

