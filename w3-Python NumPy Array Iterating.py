#https://www.w3schools.com/python/numpy/numpy_array_iterating.asp
#NumPy Array Iterating 陣列形狀
#Iterating Arrays 陣列迭代
#Iterating means going through elements one by one.
#迭代意味著逐一遍歷元素。
#As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
#當我們在 numpy 中處理多維陣列時，可以使用 python 的基本 for 循環來完成此操作。
#If we iterate on a 1-D array it will go through each element one by one.
#如果我們對 1-D 陣列進行迭代，它將逐一遍歷每個元素。
#Iterate on the elements of the following 1-D array:
#迭代以下一維陣列的元素： 
import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
print("------------------------------------------陣列迭代測試")
import numpy as np
arr = np.array([[1, 2, 3],[4,5,6]])
for x in arr:
  print(x)

print("------------------------------------------迭代 2-D 陣列")
#Iterating 2-D Arrays 迭代 2-D 陣列
#In a 2-D array it will go through all the rows.
#在 2-D 陣列中，它將遍歷所有行。
#Iterate on the elements of the following 2-D array:
#迭代以下二維陣列的元素：
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
#If we iterate on a n-D array it will go through n-1th dimension one by one.
#如果我們迭代一個 n-D 陣列，它將逐一遍歷第 n-1 維。
#To return the actual values, the scalars, we have to iterate the arrays in each dimension.
#如需返回實際值、標量，我們必須迭代每個維中的陣列。
#Iterate on each scalar element of the 2-D array:
#如需返回實際值、標量，我們必須迭代每個維中的陣列。

print("------------------------------------------迭代 3-D 陣列")
#Iterating 3-D Arrays 迭代 3-D 陣列
#In a 3-D array it will go through all the 2-D arrays.
#在 3-D 陣列中，它將遍歷所有 2-D 陣列。
#Iterate on the elements of the following 3-D array:
#迭代以下 3-D 陣列的元素： 
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)
#To return the actual values, the scalars, we have to iterate the arrays in each dimension.
#要返回實際值、標量，我們必須迭代每個維中的陣列。
print("-----------------------------------3維迭代到0維-迭代到標量")
#Iterate down to the scalars:
#迭代到標量： 
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    for z in y: 
      print(z)
#x是3維裡的2維元素,y是2維裡的的1維元素,z是1維裡的0維元素
print("------------------------------------3維迭代到2維-迭代到標量")
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
   print(x)
print("------------------------------------3維迭代到1維-迭代到標量")
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  for y in x:
    print(y)

print("--------------------------------使用 nditer() 迭代陣列")
#Iterating Arrays Using nditer() 使用 nditer() 迭代陣列
#nditer(),是numric dimension Iteraating的縮寫
#The function nditer() is a helping function that can be used 
# from very basic to very advanced iterations. It solves some 
# basic issues which we face in iteration, lets go through it 
# with examples.
#函數 nditer() 是一個輔助函數，從非常基本的迭代到非常高級的迭代都
# 可以使用。它解決了我們在迭代中面臨的一些基本問題，讓我們通過例子
# 進行介紹。
#Iterating on Each Scalar Element 迭代每個標量元素
#In basic for loops, iterating through each scalar of an array 
# we need to use n for loops which can be difficult to write 
# for arrays with very high dimensionality.
#在基本的 for 循環中，迭代遍歷陣列的每個標量，我們需要使用 n 個 for 
# 循環，對於具有高維數的陣列可能很難編寫。
#Iterate through the following 3-D array:
#遍歷以下 3-D 陣列： 
import numpy as np
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)
#nptier(),一口氣從N維迭代為0維

print("--------------------------------迭代不同數據類型的陣列")
#Iterating Array With Different Data Types
#迭代不同數據類型的陣列
#We can use op_dtypes argument and pass it the expected datatype 
# to change the datatype of elements while iterating.
#我們可以使用 op_dtypes 參數，並傳遞期望的數據類型，以在迭代時更改
# 元素的數據類型。
#NumPy does not change the data type of the element in-place 
# (where the element is in array) so it needs some other space 
# to perform this action, that extra space is called buffer, 
# and in order to enable it in nditer() we pass 
# flags=['buffered'].
#NumPy 不會就地更改元素的數據類型（元素位於陣列中），因此它需要一些
# 其他空間來執行此操作，該額外空間稱為 buffer，為了在 nditer() 中
# 啟用它，我們傳參 flags=['buffered']。
#Iterate through the array as a string:
#以字符串形式遍歷陣列： 
import numpy as np
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  #控制迭代器的行為
  #"buffered"在需要時啟用緩衝。
  #op_dtypes：dtype or tuple of dtype(s), optional
  #The required data type(s) of the operands. If copying or 
  # buffering is enabled, the data will be converted to/from 
  # their original types.
  '''
  操作者所需的數據類型。如果啟用了複製或緩衝，數據將被轉換為/從其原始類型
  '''
  #flags=['buffered'],給它額外空問,做op_dtypes=['S']更改類型
print(x)
#b'1',byte的縮寫b,'1'把Int改為String
#b'2',byte的縮寫b,'1'把Int改為String
#b'3',byte的縮寫b,'1'把Int改為String

print("----------------------------------------以不同的步長迭代")
#Iterating With Different Step Size 以不同的步長迭代
#We can use filtering and followed by iteration.
#我們可以使用過濾，然後進行迭代。
#Iterate through every scalar element of the 2D array skipping 1 element:
#每遍歷 2D 陣列的一個標量元素，跳過 1 個元素： 
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  #逗號前的:代表從頭到尾的陣列,然後逗號的後面x:x:2,x:x代表從頭到尾的
  # 索引位置,但是2是要前進2格取值,然後預設是從位置0開始
  #[0:2, 1:4],[先索引陣列,再索引陣列裡的元素]
  print(x)
print("---------------------------------------測試1")
import numpy as np
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],[[10,11,12,13],[14,15,16,17]]])
for x in np.nditer(arr[:, ::2]):#2是step,1是預設值
  #[:(先把3維陣列切開成2維,一個2維陣列算一個元素),
  # ::2(預設索引位置0開始,然後再往右推進2單位)]
    print(x)
print("---------------------------------------測試2")
import numpy as np
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],[[10,11,12,13],[14,15,16,17]]])
for x in np.nditer(arr[:,:, ::2]):
  #[:(先把3維陣列切開,一陣列算一個元素),:(切第二次陣列變一維),
  # ::2(每個一維陣列,預設索引位置0開始,然後再往右推進2單位)]
    print(x)
print("---------------------------------------測試3")
import numpy as np
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],[[10,11,12,13],[14,15,16,17]]])
for x in np.nditer(arr[:,:, :2]):
  #[:(先把3維陣列切開,一陣列算一個元素),:(切第二次陣列變一維),
  # :2(每個一維陣列,預設索引位置0開始,然後索引至2的位置)]
    print(x)

print("---------------使用 ndenumerate（） 進行枚舉反覆運算")
#Enumerated Iteration Using ndenumerate()
#使用 ndenumerate（） 進行枚舉反覆運算
#Enumeration means mentioning sequence number of somethings one by one.
#枚舉是指逐一提及事物的序號。
#Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
#有時，我們在反覆運算時需要元素的相對應索引，對於這些用例，可以使用 ndenumerate（） 方法。
#Enumerate on following 1D arrays elements:
#枚舉以下 1D 陣列元素：
import numpy as np
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

print("-------------------------------------------分隔線")
#Enumerate on following 2D array's elements:
#枚舉以下 2D 陣列元素：
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
#(0(2維的索引位置), 0(1維的索引位置)) 1(0(1維的索引位置的值))