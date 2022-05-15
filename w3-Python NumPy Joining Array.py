#https://www.w3schools.com/python/numpy/numpy_array_join.asp
#NumPy Joining Array 陣列連接
#Joining NumPy Arrays 連接 NumPy 陣列
#Joining means putting contents of two or more arrays in 
# a single array.
#連接意味著將兩個或多個數位的內容放在單個陣列中。
#In SQL we join tables based on a key, whereas in NumPy 
# we join arrays by axes.
#在 SQL 中，我們基於鍵來連接表，而在 NumPy 中，我們按軸連接數位。
#We pass a sequence of arrays that we want to join to the 
# concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.
print("-----------------------用concatenate（）連維兩個陣列")
#我們傳遞了一系列要與軸一起連接到 concatenate（） 函數的陣列。
# 如果未顯式傳遞軸，則將其視為 0。
#Join two arrays
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
print("-----------------------用concatenate（）連維兩個陣列2")
import numpy as np
arr1 = np.array([[1, 2, 3],[9,10,10]])
arr2 = np.array([[4, 5, 6],[5,6,7]])
arr3 = np.array([[1, 2, 3],[4, 5, 6]])
arr = np.concatenate((arr1, arr2,arr3))
print(arr)
#ValueError: all the input arrays must have same number 
# of dimensions,
#要合併的陣列必須是相同維數
print("-----------------axis=1-用concatenate（）axis軸:INT")
# 陣列合併,必這是相同維數,2維併了,還是2維,裡面的都是1維
#Join two 2-D arrays along rows (axis=1):
#沿著行 （axis=1） 連接兩個 2-D 陣列：
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
print(arr1)
arr2 = np.array([[5, 6], [7, 8]])
print(arr2)
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
#concatenate:連接
#當axis=0時，代表每一縱行去做運算
#當axis=1時，代表每一橫列去做運算
#axis：int,可以是0或負數/0和-2,1和-1的結果一樣,其他數字會超出
#當是None時,則全部變成1維
#軸的確定可以根據嵌套關係來確定，軸的順序就是括號的從外到內：
#The axis to take 1d slices along. If axis is None, the 
# destination array is treated as if a flattened 1d view 
# had been created of it.
#軸沿 1d 切片。如果軸為無，則目的地陣列被視為已創建扁平的 1d 視圖。

print("-------------------------------使用堆疊函數連接陣列")
#Joining Arrays Using Stack Functions
#使用堆疊函數連接陣列
#Stacking is same as concatenation, the only difference is 
# that stacking is done along a new axis.
#堆疊與連接相同，唯一的不同是堆疊是沿著新軸完成的。
#We can concatenate two 1-D arrays along the second axis 
# which would result in putting them one over the other, 
# ie. stacking.
#我們可以沿著第二個軸連接兩個一維陣列，這將導致它們彼此重疊，
# 即，堆疊（stacking）。
#We pass a sequence of arrays that we want to join to 
# the stack() method along with the axis. If axis is not 
# explicitly passed it is taken as 0.
#我們傳遞了一系列要與軸一起連接到 concatenate（） 方法的陣列。
# 如果未顯式傳遞軸，則將其視為 0。
import numpy as np
arr1 = np.array([1, 2, 3])
print(arr1)
arr2 = np.array([4, 5, 6])
print(arr2)
arr = np.stack((arr1, arr2), axis=1)
#axis=1,stack上下元素疊起來,輸出為橫列
#當axis=1時，代表每一橫列去做運算
#axis=0,stack變橫向堆疊,輸出為橫列
#當axis=0時，代表每一縱行去做運算
print(arr)

print("------------hstack-Stacking Along Rows 橫向堆疊")
#Stacking Along Rows 橫向堆疊
#NumPy provides a helper function: hstack() to stack along rows.
#NumPy 提供了一個輔助函數：hstack（） 橫向堆疊。
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

print("------------vstack-Stacking Along Columns 縱向堆疊")
#Stacking Along Columns 縱向堆疊
#NumPy provides a helper function: vstack()  to stack along columns.
#NumPy 提供了一個輔助函數：vstack（） 縱向堆疊。
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

print("------------vstack-Stacking Along Height (depth) 縱向堆疊")
#Stacking Along Height (depth) 沿高度堆疊（深度）
#NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
#NumPy 提供了一個輔助函數：dstack（） 沿高度堆疊，該高度與深度相同。
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)