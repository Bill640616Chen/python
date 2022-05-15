#https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
#NumPy Array Slicing 陣列裁切 
#Slicing arrays
#Slicing in python means taking elements from one given index to another given index.
#python 中裁切的意思是將元素從一個給定的索引帶到另一個給定的索引。
#We pass slice instead of index like this: [start:end].
#我們像這樣傳遞切片而不是索引：[start：end]。
#We can also define the step, like this: [start:end:step].
#我們還可以定義步長，如下所示：[start：end：step]。
#If we don't pass start its considered 0
#如果我們不傳遞 start，則將其視為 0。
#If we don't pass end its considered length of array in that dimension
#如果我們不傳遞 end，則視為該維度內陣列的長度。
#If we don't pass step its considered 1
#如果我們不傳遞 step，則視為 1。
#Slice elements from index 1 to index 5 from the following array:
print("--------------------------[1:5]第一個:左邊的索引位置含值,右邊不含")
#從下面的陣列中裁切索引 1 到索引 5 的元素：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #[2 3 4 5]位置5的值不算
#Note: The result includes the start index, but excludes the end index.
#註釋：結果包括了開始索引，但不包括結束索引。
#Slice elements from index 4 to the end of the array:
print("--------------------------[4:]第一個:左邊的索引位置含值,右邊不含")
#裁切陣列中索引 4 到結尾的元素：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:]) #[5 6 7]
#Slice elements from the beginning to index 4 (not included):
print("--------------------------[:4]第一個:左邊的索引位置含值,右邊不含")
#裁切從開頭到索引 4（不包括）的元素：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4]) #[1 2 3 4]

print("-----------------------[-3:-1]第一個:左邊的索引位置含值,右邊不含")
#Negative Slicing 負裁切
#Use the minus operator to refer to an index from the end:
#使用減號運算子從末尾開始引用索引：
#Slice from the index 3 from the end to index 1 from the end:
#從末尾開始的索引 3 到末尾開始的索引 1，對陣列進行裁切：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1]) #[5 6]

#STEP 步長
#Use the step value to determine the step of the slicing:
#請使用 step 值確定裁切的步長：
#Return every other element from index 1 to index 5:
print("-----------[1:5:2]第一個:左邊的索引位置含值,右邊不含,從起始往右2")
#從索引 1 到索引 5，返回相隔的元素：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) #[2 4]
print("--------------[::2]第一個:左邊的索引位置含值,右邊不含,從起始往右2")
#Return every other element from the entire array:
#傳回陣中相隔的元素：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2]) #起始沒寫,預設為0,[1 3 5 7]

print("------裁切 2維 陣列-[1, 1:4]第一個:左邊的索引位置含值,右邊不含,從起始往右")
#Slicing 2-D Arrays 裁切 2維 陣列
#From the second element, slice elements from index 1 to index 4 (not included):
#從第二個元素開始，對從索引 1 到索引 4（不包括）的元素進行切片：
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) #[7 8 9]
#Note: Remember that second element has index 1.
#註釋：請記得第二個元素的索引為 1。
#Use the built-in help function to view a function's docstring:
#help(np.sort)
#From both elements, return index 2:
print("------裁切 2維 陣列-[0:2, 2]第一個:左邊的索引位置含值,右邊不含,從起始往右")
#從兩個元素中傳回索引 2：
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1]) #[2 7]
#[0:2, 1],0:2是指二維陣列的索引位置,1是陣列裡的索引位置的值
print("------裁切 2維 陣列-[:1, 1]第一個:左邊的索引位置含值,右邊不含,從起始往右")
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[:1, 1]) #[2]
#[:1, 1],:1是指二維陣列的索引位置,1是陣列裡的索引位置的值

#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
#從兩個元素裁切索引 1 到索引 4（不包括），這將返回一個 2-D 陣列：
import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) #[[2 3 4] [7 8 9]]
