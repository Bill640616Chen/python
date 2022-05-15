#https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
#NumPy Data Types 數據類型
#Data Types in Python 數據類型在Python
#By default Python have these data types:
#預設情況下，Python 擁有以下資料類型：
'''
strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
strings - 用於表示文本數據，文本用引號引起來。 例如 「ABCD」。
integer - used to represent integer numbers. e.g. -1, -2, -3
integer - 用於表示整數。 例如 -1， -2， -3。
float - used to represent real numbers. e.g. 1.2, 42.42
float - 用於表示實數。 例如 1.2， 42.42。
boolean - used to represent True or False.
boolean - 用於表示 True 或 False。
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
complex - 複數。 例如 1.0 + 2.0j，1.5 + 2.5j。
'''
#Data Types in NumPy NumPy中的數據類型
#NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
#NumPy 有一些額外的數據類型，並通過一個字元引用數據類型，例如 i 代表整數，u 代表無符號整數等。
#Below is a list of all data types in NumPy and the characters used to represent them.
#以下是 NumPy 中所有資料類型的清單以及用於表示它們的字元。
#i - integer 整數
#b - boolean 布爾
#u - unsigned integer 無符號整數
#f - float 浮點
#c - complex float 複數浮點
#m - timedelta
#M - datetime
#O - object 物件
#S - string 字串
#U - unicode string unicode 字串
#V - fixed chunk of memory for other type ( void )
#固定的其他類型的記憶體塊 （ void ）
#Checking the Data Type of an Array 檢查陣列的數據類型
#The NumPy array object has a property called dtype that returns the data type of the array:
#NumPy 陣列物件有一個名為 dtype 的屬性，該屬性返回數位資料類型：
#Get the data type of an array object:取得陣列物件的資料類型：
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype) #int32
#Get the data type of an array containing strings:
#取得包含字串的陣列的資料類型：
import numpy as np
arr = np.array(['apple', 'banana22', 'cherry'])
print(arr.dtype) #<U8
#dtype取得包含字串的陣列的資料類型：
#第一個字元(U)指定數據的類型，其餘的字元指定每個項目的位元組數，
#<U8,U代表Unicode,Unicode除外，在Unicode中，它被解釋為字元數。
#<U8,U代表Unicode,以最多位元元素計算banana22共8個字元,所以輸出<U8

print("---取得包含字串的陣列的資料類型-U代表Unicode,以最多位元元素計算")
print(arr.astype(object)) #['apple' 'banana22' 'cherry']
arr = np.char.add(arr, ' foo')
print(arr.dtype) #<U12
#<U12,U代表Unicode,以最多位元元素計算banana22+ foo=8+4=12

print("---------------------------------用已定義的數據類型創建陣列")
#Creating Arrays With a Defined Data Type
#用已定義的數據類型創建陣列
#We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:
#我們使用array（） 函數來建立數位，該函數可以使用可選參數：dtype，它允許我們定義數位元素的預期資料類型：
#Create an array with data type string:
#用資料類型字串建立陣列：
import numpy as np
arr = np.array(["a123", 2, 3, 4], dtype='S')
print(arr) #[b'a123' b'2' b'3' b'4']
print(arr.dtype) #|S4,S代表字串,4代表a123共4個字元,|絕對值
print(type(arr[1])) #<class 'numpy.bytes_'>
#For i, u, f, S and U we can define size as well.
#對於i、u、f、S和U，我們也可以定義大小。
#Create an array with data type 4 bytes integer:
#建立資料類型為 4 位元組整數的陣列：
import numpy as np
arr = np.array([1, 22, 3, 4, 5], dtype='i1')
print(arr)
print(arr.dtype) 
#i1代表int8,i2代表int16,i4代表int32
print(type(arr[0])) #<class 'numpy.int32'>
#http://www.numpy.org.cn/reference/arrays/dtypes.html#%E5%B1%9E%E6%80%A7
print("-------------------------還看不懂--另一個網站的code測試")
dt = np.dtype('>i4')
#位元組順序取決於數據類型的前綴<或>。 <意味著編碼是小端（最小有效
# 位元組存儲在最小位址中）。 >意味著編碼是大端（最大有效位元組存儲
# 在最小位址中）。
# https://www.yiibai.com/numpy/numpy_data_types.html
print(dt)
dt = np.dtype([('name', np.unicode_, 16), ('grades', np.float64, (2,))])
print(dt)
#[('name', '<U16'), ('grades', '<f8', (2,))]
print(type(dt[0]))
#<class 'numpy.dtype[str_]'>

print("---------------假如值無法轉換會怎樣？出現ValueError")
#What if a Value Can Not Be Converted? 假如值無法轉換會怎樣？
#If a type is given in which elements can't be casted then 
# NumPy will raise a ValueError.
#如果給出了不能強制轉換元素的類型，則 NumPy 將引發 ValueError。
#ValueError: In Python ValueError is raised when the type of 
# passed argument to a function is unexpected/incorrect.
#ValueError：在 Python 中，如果傳遞給函數的參數的類型是非預期
# 或錯誤的，則會引發 ValueError。
#A non integer string like 'a' can not be converted to integer (will raise an error):
'''
import numpy as np
arr = np.array(['a', '2', '3'], dtype='i')
ValueError: invalid literal for int() with base 10: 'a'
無法把String轉換為int
'''

print("-------------------------------轉換已有陣列的數據類型")
#Converting Data Type on Existing Arrays
#轉換已有陣列的數據類型
#The best way to change the data type of an existing array, 
# is to make a copy of the array with the astype() method.
#更改現有陣列的數據類型的最佳方法，是使用 astype（） 方法複製該陣列。
#The astype() function creates a copy of the array, and allows 
# you to specify the data type as a parameter.
#astype（） 函數創建數位的副本，並允許您將資料類型指定為參數。
#The data type can be specified using a string, like 'f' for 
# float, 'i' for integer etc. or you can use the data type 
# directly like float for float and int for integer.
#數據類型可以使用字串指定，例如 'f' 表示浮點數，'i' 表示整數等。
# 或者您也可以直接使用數據類型，例如 float 表示浮點數，int 表示整數。
#Change data type from float to integer by using 'i' as 
# parameter value:
#使用 'i' 作為參數值，將資料類型從浮點數更改為整數：
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i') #'i"預設是int32
#astype(資料類型)：轉換資料類型
print(newarr) #[1 2 3]
print(newarr.dtype) #int32

#Change data type from float to integer by using int as parameter value:
#通過使用 int 作為參數值，將數據類型從浮點數更改為整數： 
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int) #int預設是int32
#astype(資料類型)：轉換資料類型
print(newarr) #[1 2 3]
print(newarr.dtype) #int32

#Change data type from integer to boolean:
#將數據類型從整數更改為布爾值： 
import numpy as np
arr = np.array([1, 0, 3, 0.1, -1])
newarr = arr.astype(bool)
#astype(資料類型)：轉換資料類型
print(newarr) #[ True False  True  True  True]
'''
bool 值 （布林值）所代表的正是極基本的單位：
1 = True
0 = False
'''
print(newarr.dtype) #bool