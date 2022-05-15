#https://www.w3schools.com/python/ref_func_complex.asp
#Python complex Function Python complex函數
#Returns a complex number
#返回複數。
#Convert the number 3 and imaginary number 5 into a complex number:
#將數位 3 和虛數 5 轉換為複數：
x = complex(3, 5)
print(x)
#Definition and Usage 定義和用法
#The complex() function returns a complex number by specifying a real number and an imaginary number.
#complex（） 函數通過指定實數和虛數來返回複數。
#Syntax 語法
#complex(real, imaginary)
#Parameter參數：Values值
#Parameter參數：Description描述
#real：Required. A number representing the real part of the complex number. Default 0. The real number can also be a String, like this '3+5j', when this is the case, the second parameter should be omitted.
#real：必需。 代表複數實數部分的數位。 預設值0。
#實數也可以是字串，比如 『3+5j』，在這種情況下，應省略第二個參數。
#imaginary：Optional. A number representing the imaginary part of the complex number. Default 0.
#imaginary：可選。 代表複數的虛數部分。 預設值為 0。
#Convert a string into a complex number:
#將字串轉換為複數：
x = complex('3+5j')
print(x)
