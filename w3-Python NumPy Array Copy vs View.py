#https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp
#NumPy Array Copy vs View 陣列副本 vs 視圖 
#The Difference Between Copy and View 副本和視圖之間的區別
#The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
#副本和陣列視圖之間的主要區別在於副本是一個新陣列，而這個視圖只是原始陣列的視圖。
#The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
#副本擁有數據，對副本所做的任何更改都不會影響原始陣列，對原始陣列所做的任何更改也不會影響副本。
#The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
#視圖不擁有數據，對視圖所做的任何更改都會影響原始陣列，而對原始陣列所做的任何更改都會影響視圖。
#COPY:副本：
#Make a copy, change the original array, and display both arrays:
print("--------------------進行複制，更改原始陣列並顯示兩個陣列：")
#進行複制，更改原始陣列並顯示兩個陣列：
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42 #更改位置0的值
print(arr) #[42  2  3  4  5]
print(x) #[1 2 3 4 5]
#The copy SHOULD NOT be affected by the changes made to the original array.
#該副本不應受到對原始陣列所做更改的影響。 

print("-----視圖所做的任何更改都會影響原始陣列------VIEW: 視圖：")
#VIEW: 視圖：
#Make a view, change the original array, and display both arrays:
#創建視圖，更改原始陣列，然後顯示兩個陣列：
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view() 
arr[0] = 42
print(arr) #[42  2  3  4  5]
print(x) #[42  2  3  4  5]
#The view SHOULD be affected by the changes made to the original array.
#視圖應該受到對原始陣列所做更改的影響。 

print("-----改視圖,原始跟著變--創建視圖，更改視圖，並顯示兩個陣列：")
#Make Changes in the VIEW: 在視圖中進行更改：
#Make a view, change the view, and display both arrays:
#創建視圖，更改視圖，並顯示兩個陣列：
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr) #[31  2  3  4  5]
print(x) #[31  2  3  4  5]
#The original array SHOULD be affected by the changes made to the view.

print("--------------------------檢查陣列是否擁有數據")
#Check if Array Owns it's Data 檢查陣列是否擁有數據
#As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
#如上所述，副本擁有數據，而視圖不擁有數據，但是我們如何檢查呢？
#Every NumPy array has the attribute base that returns None if the array owns the data.
#每個 NumPy 陣列都有一個屬性 base，如果該陣列擁有數據，則這個 base 屬性返回 None。
#Otherwise, the base  attribute refers to the original object.
#否則，base 屬性將引用原始對象。
#Print the value of the base attribute to check if an array owns it's data or not:
#打印 base 屬性的值以檢查陣列是否擁有自己的數據：
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() #副本沒有數據
y = arr.view() #視圖是原始的副本,不是數據
print(x.base) #None
print(y.base) #[1 2 3 4 5]
#The copy returns None. 副本返回 None。
#The view returns the original array. 視圖返回原始陣列。 
