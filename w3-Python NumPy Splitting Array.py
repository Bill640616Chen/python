#https://www.w3schools.com/python/numpy/numpy_array_split.asp
#NumPy Splitting Array 陣列拆分
#Splitting NumPy Arrays 拆分 NumPy 陣列
#Splitting is reverse operation of Joining.
#拆分是連接的反向操作。
#Joining merges multiple arrays into one and Splitting breaks one array into multiple.
#連接（Joining）是將多個陣列合併為一個，拆分（Spliting）將一個陣列拆分為多個。
#We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
#我們使用 array_split（） 分割陣列，將要分割的陣列和分割數傳遞給它。
#Split the array in 3 parts:
print("---------------將陣列分為 3 部分array_split(arr, 3)")
#將陣列分為 3 部分：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
#array_split(arr, 3)等於array_split(arr, 3, axis=1)
print(newarr)
#Note: The return value is an array containing three arrays.
#註釋：返回值是一個包含三個陣列的陣列。
#If the array has less elements than required, it will adjust from the end accordingly.
#如果陣列中的元素少於要求的數量，它將從末尾進行相應調整。
#Split the array in 4 parts:
print("---------------將陣列分為 4 部分array_split(arr, 4)")
#將陣列分為 4 部分：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)
#[array([1, 2]), array([3, 4]), array([5]), array([6])]
#Note: We also have the method split() available but it 
# will not adjust the elements when elements are less in 
# source array for splitting like in example above, 
# array_split() worked properly but split() would fail.
#提示：我們也有split（） 方法可用，但是當源陣列中的元素較少用
# 於拆分時，它將不會調整元素，如上例那樣，array_split（） 
# 正常工作，但split（） 會失敗。

#Split Into Arrays 拆分為陣列
#The return value of the array_split() method is an array containing each of the split as an array.
#array_split（） 方法的返回值是一個包含每個分割的陣列。
#If you split an array into 3 arrays, you can access them from the result just like any array element:
#如果將一個陣列拆分為 3 個陣列，則可以像使用任何陣列元素一樣從結果中訪問它們：
#Access the splitted arrays:
print("-------------------------------------拜訪分割的陣列")
#拜訪分割的陣列：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0]) #索引拆分的陣列
print(newarr[1]) #索引拆分的陣列
print(newarr[2]) #索引拆分的陣列

#Splitting 2-D Arrays 分割二維陣列
#Use the same syntax when splitting 2-D arrays.
#拆分二維陣列時，請使用相同的語法。
#Use the array_split() method, pass in the array you want to split and the number of splits you want to do.
#使用 array_split（） 方法，傳入要分割的陣列和想要分割的數目。
#Split the 2-D array into three 2-D arrays.
print("-------array_split(arr, 3)--把這個 2-D 拆分為三個 2-D 陣列")
#把這個 2-D 拆分為三個 2-D 陣列。
import numpy as np
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
#The example above returns three 2-D arrays.
#上例返回三個 2-D 陣列。
#Let's look at another example, this time each element in the 2-D arrays contains 3 elements.
#讓我們看另一個例子，這次 2-D 陣列中的每個元素包含 3 個元素。
#Split the 2-D array into three 2-D arrays.
print("-------array_split(arr, 3)--把這個 2-D 拆分為三個 2-D 陣列")
#把這個 2-D 拆分為三個 2-D 陣列。
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)
#The example above returns three 2-D arrays.
#上例返回三個 2-D 陣列。
#In addition, you can specify which axis you want to do the split around.
#此外，您可以指定要進行拆分的軸。
#The example below also returns three 2-D arrays, but they are split along the row (axis=1).
#下面的例子還返回三個 2-D 陣列，但它們沿行 （axis=1） 分割。
#Split the 2-D array into three 2-D arrays along rows.
print("-------array_split(arr, 3, axis=1)--把這個 2-D 拆分為三個 2-D 陣列")
#沿行把這個 2-D 拆分為三個 2-D 陣列。
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
#An alternate solution is using hsplit() opposite of hstack()
#另一種解決方案是使用與 hstack（） 相反的 hsplit（）。
#Use the hsplit() method to split the 2-D array into three 2-D arrays along rows.
print("-------hsplit(arr, 3)--把這個 2-D 拆分為三個 2-D 陣列")
#使用 hsplit（） 方法將 2-D 陣列沿著行分成三個 2-D 陣列。
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)
newarr = np.hsplit(arr, 3)
print(newarr)
#Note: Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
#提示：vsplit（） 和 dsplit（） 可以使用與 vstack（） 和 dstack（） 類似的替代方法。