#https://www.w3schools.com/python/numpy/numpy_array_reshape.asp
#NumPy Array Reshaping 陣列重組
#Reshaping arrays 陣列重組
#Reshaping means changing the shape of an array.
#重塑意味著更改陣列的形狀。
#The shape of an array is the number of elements in each dimension.
#陣列的形狀是每個維中元素的數量。
#By reshaping we can add or remove dimensions or change number of elements in each dimension.
#通過重塑，我們可以添加或刪除維度或更改每個維度中的元素數量。
#Reshape From 1-D to 2-D
#從 1-D 重塑為 2-D
#Convert the following 1-D array with 12 elements into a 2-D array.
#將以下具有 12 個元素的 1-D 陣列轉換為 2-D 陣列。
print("----------------------------------------從 1D 更改為 2D")
#The outermost dimension will have 4 arrays, each with 3 elements:
#最外面的維度將有 4 個陣列，每個陣列包含 3 個元素： 
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) 
print(newarr)

print("----------------------------------------從 1D 更改為 3D")
#Reshape From 1-D to 3-D 從 1-D 重塑為 3-D
#Convert the following 1-D array with 12 elements into a 3-D array.
#將以下具有 12 個元素的 1-D 陣列轉換為 3-D 陣列。
#The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:
#最外面的維度將具有 2 個陣列，其中包含 3 個陣列，每個陣列包含 2 個元素： 
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

print("-----------------------------我們可以重塑成任何形狀嗎？")
#Can We Reshape Into any Shape? 我們可以重塑成任何形狀嗎？
#Yes, as long as the elements required for reshaping are equal in both shapes.
#是的，只要重塑所需的元素在兩種形狀中均相等。
#We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.
#我們可以將 8 元素 1D 陣列重塑為 2 行 2D 陣列中的 4 個元素，但是我們不能將其重塑為 3 元素 3 行 2D 陣列，因為這將需要 3x3 = 9 個元素。
#Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):
#嘗試將具有 8 個元素的 1D 陣列轉換為每個維度中具有 3 個元素的 2D 陣列（將產生錯誤）： 
'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(3, 3)
print(newarr)
'''
#ValueError: cannot reshape array of size 8 into shape (3,3)

print("----------------------------------返回副本還是視圖？")
#Returns Copy or View? 返回副本還是視圖？
#Check if the returned array is a copy or a view:
#檢查返回的陣列是副本還是視圖： 
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)
#x.base is None
#[1 2 3 4 5 6 7 8]
#The example above returns the original array, so it is a view.
#上面的例子返回原始陣列，因此它是一個視圖。

print("--------------------------Unknown Dimension 未知的維")
#Unknown Dimension 未知的維
#You are allowed to have one "unknown" dimension.
#您可以使用一個“未知”維度。
#Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
#這意味著您不必在 reshape 方法中為維度之一指定確切的數字。
#Pass -1 as the value, and NumPy will calculate this number for you.
#傳遞 -1 作為值，NumPy 將為您計算該數字。
#Convert 1D array with 8 elements to 3D array with 2x2 elements:
#將 8 個元素的 1D 陣列轉換為 2x2 元素的 3D 陣列：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1) #-n的結果都一樣
print(newarr)
#Note: We can not pass -1 to more than one dimension.
#註釋：我們不能將 -1 傳遞給一個以上的維度。 

print("---------------------展平陣列：將多維陣列轉換為 1D 陣列")
#Flattening the arrays 展平陣列
#Flattening array means converting a multidimensional array into a 1D array.
#展平陣列（Flattening the arrays）是指將多維陣列轉換為 1D 陣列。
#We can use reshape(-1) to do this.
#我們可以使用 reshape(-1) 來做到這一點。(-N)也可以
#Convert the array into a 1D array:
#把陣列轉換為 1D 陣列：
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
#Note: There are a lot of functions for changing the shapes of 
# arrays in numpy flatten, ravel and also for rearranging the 
# elements rot90, flip, fliplr, flipud etc. These fall under 
# Intermediate to Advanced section of numpy.
#註釋：有很多功能可以更改 numpy flatten、ravel 中陣列形狀，
# 還可以重新排列元素 rot90、flip、fliplr、flipud 等。這些功能屬於 
# numpy 的中級至高級部分。 
