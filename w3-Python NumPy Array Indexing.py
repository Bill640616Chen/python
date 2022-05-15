#https://www.w3schools.com/python/numpy/numpy_array_indexing.asp
#NumPy Array Indexing 陣列索引 
#Access Array Elements 訪問陣列元素
#Array indexing is the same as accessing an array element.
#陣列索引等同於訪問陣列元素。
#You can access an array element by referring to its index number.
#您可以通過引用其索引號來訪問陣列元素。
#The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
#NumPy 陣列中的索引以 0 開頭，這意味著第一個元素的索引為 0，第二個元素的索引為 1，以此類推。
#Get the first element from the following array:
print("---------------------Access Array Elements 訪問陣列元素")
#從以下陣列中取得第一個元素：
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])
#Get the second element from the following array.
#從以下陣列中取得第二個元素：
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[1])
#Get third and fourth elements from the following array and add them.
#從以下陣列中取得第三和第四個元素並將其相加：
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3]) #int可以相加

print("------------------------Access 2-D Arrays訪問 2維 陣列")
#Access 2-D Arrays 訪問 2維 陣列
#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
#要訪問二維陣列中的元素，我們可以使用逗號分隔的整數表示元素的維數和索引。
#Access the 2nd element on 1st dim:
#存取第一維中的第二個元素：
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1]) #2
#arr[0,1],0為第一維,1為第一維裡的位置
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 2nd dim: ', arr[1, 1]) #7
#arr[1,1],1為第二維,1為第二維裡的位置

print("------------------------Access 3-D Arrays訪問 3維 陣列")
#Access 3-D Arrays 訪問 3維 陣列
#To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
#要訪問 3維 陣列中的元素，我們可以使用逗號分隔的整數來表示元素的維數和索引。
#Access the third element of the second array of the first array:
#存取第一個陣列的第二個陣列的第三個元素：
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) #6
#0第一個陣列[[1, 2, 3], [4, 5, 6]]裡的第二個陣列1裡面的第三個元素

print("------------------------------Negative Indexing 負索引")
#Negative Indexing 負索引
#Use negative indexing to access an array from the end.
#使用負索引從尾開始訪問陣列。
#Print the last element from the 2nd dim:
#列印第二個維中的的最後一個元素：
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) #10

print("------------------------Access 4-D Arrays訪問 4維 陣列")
import numpy as np
arr = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]])
print(arr[0, 1, 1, 2]) #12
#2個3維=1個4維,2個4維=1個5維,依此遞增