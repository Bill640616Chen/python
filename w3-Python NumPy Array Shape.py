#https://www.w3schools.com/python/numpy/numpy_array_shape.asp
#NumPy Array Shape 陣列形狀
#Shape of an Array 陣列的形狀
#The shape of an array is the number of elements in each dimension.
#陣列的形狀是每個維中元素的數量。
#Get the Shape of an Array 獲取陣列的形狀
#NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
#NumPy 陣列有一個名為 shape 的屬性，該屬性返回一個元組，每個索引具有相應元素的數量。
#Print the shape of a 2-D array:
print("------------------------------------打印 2維 陣列的形狀：")
#打印 2維 陣列的形狀：
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) #(2, 4)
#The example above returns (2, 4), which means that the array has 2 dimensions, and each dimension has 4 elements.
#上面的例子返回 (2, 4)，這意味著該陣列有 2 個維，每個維有 4 個元素。
 
print("------------------------------------打印 3維 陣列的形狀：")
#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
#利用 ndmin 使用值 1,2,3,4 的向量創建有 5 個維度的數組，並驗證最後一個維度的值為 4： 
import numpy as np
arr = np.array([1, 2, 3, 4, 5], ndmin=3)
print(arr)
print('shape of array :', arr.shape)

#What does the shape tuple represent?
#元組的形狀代表什麼？
#Integers at every index tells about the number of elements 
# the corresponding dimension has.
#每個索引處的整數表明相應維度擁有的元素數量。
#In the example above at index-4 we have value 4, so we can 
# say that 5th ( 4 + 1 th) dimension has 4 elements.
#上例中的索引 4，我們的值為 4，因此可以說第 5 個 ( 4 + 1 th) 
# 維度有 4 個元素。 

print("------------------------------------打印 4維 陣列的形狀：")
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6], ndmin=4)
print(arr)
print('shape of array :', arr.shape)

print("------------------------------------打印 5維 陣列的形狀：")
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

print("------------------------------------打印 6維 陣列的形狀：")
import numpy as np
arr = np.array([1, 2], ndmin=6)
print(arr)
print('shape of array :', arr.shape)
#shape of array : (1, 1, 1, 1, 1, 2)
#第1個1是2維,依此類推,共6維,2是代表元素數量

print("--------使用正確的 reshape 方法將陣列的形狀從 1D 更改為 2D")
#Use the correct NumPy method to change the shape of an array from 1-D to 2-D.
#使用正確的 NumPy 方法將陣列的形狀從 1D 更改為 2D。
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) #分成4個元組,每1組3個元素
print(newarr)

#Use a correct NumPy method to change the shape of an array from 2-D to 1-D.
#使用正確的 reshape 方法將陣列的形狀從 2D 更改為 1-D。
print("----------------------------------------從 2D 更改為 1D")
arr = np.array([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]])
newarr = arr.reshape(-10) #只要是負數都是一樣的意思
print(newarr)

print("----------------------------------------從 6D 更改為 1D")
ar = np.array([[[[[[1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]]]]]])
newa = ar.reshape(2,2,2,3,1,-1)
#6維先切為2個5維(1-12,13-24),5變4(1-6,7-12),4變3(1-3,4-6),
# 3變2(1,2,3)因為只剩三個元素,所以只能拆3個2維,2變1,-1是直接變1維
print(newa)
'''
[[[[[[ 1]],[[ 2]],[[ 3]]],[[[ 4]],[[ 5]],[[ 6]]]],[[[[ 7]],[[ 8]],[[ 9]]],[[[10]],[[11]],[[12]]]]]

,[[[[[13]],[[14]],[[15]]],[[[16]],[[17]],[[18]]]],[[[[19]],[[20]],[[21]]],[[[22]],[[23]],[[24]]]]]]
'''
