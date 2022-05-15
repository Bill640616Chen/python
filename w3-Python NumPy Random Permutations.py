#https://www.w3schools.com/python/numpy/numpy_random_permutation.asp
#Random Permutations 隨機排列
#Random Permutations of Elements 元素的隨機排列
#A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
#排列是指元素的排列。例如[3、2、1]是[1、2、3]的排列，反之亦然。
#The NumPy Random module provides two methods for this: shuffle() and permutation().
#NumPy 隨機模組為此提供了兩種方法： shuffle() 和 permutation()。
#Shuffling Arrays 洗牌陣列
#Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
#洗牌意味著改變原位元素的排列。即在陣列本身中。
#Randomly shuffle elements of following array:
print("---------------------shuffle---隨機洗牌以下陣列的元素")
#隨機洗牌以下陣列的元素：
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
#The shuffle() method makes changes to the original array.
#洗牌方法對原始陣列進行更改排列序

print("---------------------permutation--------生成陣列排列")
#Generating Permutation of Arrays 生成陣列排列
#ExampleGenerate a random permutation of elements of following array:
#產生以下陣列元素的隨機排列：
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
#The permutation() method returns a re-arranged array (and leaves the original array un-changed).
#排列 （） 方法返回重新排列的陣列（並且未更改原始陣列）。
