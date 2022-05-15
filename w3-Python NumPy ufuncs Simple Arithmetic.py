#https://www.w3schools.com/python/numpy/numpy_ufunc_simple_arithmetic.asp
#Simple Arithmetic
#簡單的算術
#You could use arithmetic operators + - * / 
# directly between NumPy arrays, but this section 
# discusses an extension of the same where we have 
# functions that can take any array-like objects 
# e.g. lists, tuples etc. and perform arithmetic 
# conditionally.
#您可以使用算術操作員 + - * / 直接在 NumPy 陣列之間，
# 但此部分討論了相同的擴展，其中我們有功能可以接收任何
# 類似陣列的物件，如清單、tuple等，並有條件地執行算術。
#Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.
#算術條件：意味著我們可以定義算術操作應該發生的條件。
#All of the discussed arithmetic functions take a where parameter in which we can specify that condition.
#所有討論的算術函數都採取參數，我們可以在其中指定該條件。
print("---------------------------Addition 加法")
#Addition 加法
#The add() function sums the content of two arrays, and return the results in a new array.
#添加（）功能將兩個陣列的內容相匯總，並將結果返回到新陣列中。
#Add the values in arr1 to the values in arr2:
#將 arr1 中的值新增到 arr2 中的值中：
import numpy as np
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2)
print(newarr)
#The example above will return [30 32 34 36 38 40] which is the sums of 10+20, 11+21, 12+22 etc.
#以上示例將返回 [30 32 34 36 38 40] 這是 10+20、11+21、12+22 等金額。

print("------------------------Subtraction 減法")
#Subtraction 減法
#The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.
#減去（）函數減去一個陣列中的值與來自另一個陣列的值，並在新陣列中返回結果。
#Subtract the values in arr2 from the values in arr1:
#從 arr1 中的值中減去 arr2 中的值：
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)
print(newarr)
#The example above will return [-10 -1 8 17 26 35] which is the result of 10-20, 20-21, 30-22 etc.
#以上示例將返回 [-10 -1 8 17 26 35]，這是 10-20、20-21、30-22 等結果。

print("-----------------------Multiplication 乘法")
#Multiplication 乘法
#The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.
#乘法（） 函數將來自一個陣列的值與來自另一個陣列的值相乘，並將結果返回到一個新的陣列中。
#Multiply the values in arr1 with the values in arr2:
#將 arr1 中的值與 arr2 中的值乘以：
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)
print(newarr)
#The example above will return [200 420 660 920 1200 1500] which is the result of 10*20, 20*21, 30*22 etc.
#以上示例將返回 [200 420 660 920 1200 1500]，這是 10*20、20*21、30*22 等結果。

print("-------------------------------Division 除法")
#Division 除法
#The divide() function divides the values from one array with the values from another array, and return the results in a new array.
#除（） 函數將值從一個陣列中除以從另一個陣列的值，並將結果返回到一個新的陣列中。
#Divide the values in arr1 with the values in arr2:
#將 arr1 中的值除以 arr2 中的值：
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
newarr = np.divide(arr1, arr2)
print(newarr)
#The example above will return [3.33333333 4. 3. 5. 25. 1.81818182] which is the result of 10/3, 20/5, 30/10 etc.
#以上示例將返回 [3.33333333 4.3. 5.25. 1.81818182] 這是 10/3、20/5、30/10 等結果。

print("----------------------------------Power 次方")
#Power 次方
#The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.
#次方()函數將值從第一個陣列提升到第二個陣列值的功率，並將結果返回到新的陣列中。
#Raise the valules in arr1 to the power of values in arr2:
#用arr2當次方,提升arr1的值
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])
newarr = np.power(arr1, arr2)
print(newarr)
#The example above will return [1000 3200000 729000000 6553600000000 2500 0] which is the result of 10*10*10, 20*20*20*20*20, 30*30*30*30*30*30 etc.
#以上示例將返回 [1000 3200000 729000000 65536000000 2500 0] 這是 10*10*10 的結果， 20*20*20*20*20，30*30*30*30*30等。

print("-------------------mod--Remainder 取餘運算")
#Remainder 取餘運算
#Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.
#mod()取餘數和remainder()取餘數函數傳回第一陣列對應第二陣列的餘值,然後再把結果傳到一個新的陣列
#Return the remainders:
#傳回餘數
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.mod(arr1, arr2)
print(newarr)
#The example above will return [1 6 3 0 0 27] which
#  is the remainders when you divide 10 with 3 
# (10%3), 20 with 7 (20%7) 30 with 9 (30%9) etc.
#以上示例將返回 [1 6 3 0 0 27] 這是剩餘部分，當您將 
# 10 與 3（10%3），20 與 7（20%7） 30 與 9 （30%9） 等。

print("------------------------Remainder 取餘運算")
#You get the same result when using the remainder() function:
#使用remainder()功能時，您會獲得相同的結果：
#Return the remainders:
#傳回餘數
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.remainder(arr1, arr2)
print(newarr)

print("----------------Quotient and Mod 商數與餘數")
#Quotient and Mod 商數與餘數
#The divmod() function return both the quotient and the the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.
#divmod()函數同時傳回商數與餘數,傳回2個陣列的值,第1個是商數,第二個是餘數
#Return the quotient and mod:
#傳回商數與餘數
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
newarr = np.divmod(arr1, arr2)
print(newarr)
#The example above will return:
#以上範例將返回：
#(array([3, 2, 3, 5, 25, 1]), array([1, 6, 3, 0, 0, 27]))
#（陣列（[3、2、3、5、25、1]）、陣列（[1、6、3、0、0、27]）
#The first array represents the quotients, (the integer value when you divide 10 with 3, 20 with 7, 30 with 9 etc.
#第一個陣列表示商（當您將 10 與 3、20 與 7、30 與 9 等除以時，整數值）。
#The second array represents the remainders of the same divisions.
#第二個陣列表示相同部門的餘數部分。

print("----------------------Absolute Values 絕對值")
#Absolute Values 絕對值
#Both the absolute() and the abs() functions functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()
#absolute()和abs()函數功能都是做相同的絕對值操作元素,但我們應該使用absolute()以避免與python's內置的math.abs()混淆。
#Return Absolute Values:
#傳回絕對值
import numpy as np
arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)
print(newarr)
#The example above will return [1 2 1 2 3 4].
#以上示例將返回 [1 2 1 2 3 4]。
