#https://www.w3schools.com/python/ref_func_pow.asp
#Python pow() Function Python pow()函數
#Returns the value of x to the power of y
#返回 x 的 y 次方的值。
#Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
#傳回 4 的 3 次方（與 4 * 4 * 4 相同）：
x = pow(4, 3)
print(x)
#Definition and Usage 定義和用法
#The pow() function returns the value of x to the power of y (xy).
#pow（） 函數 x 的 y 次冪 （xy） 的值。
#If a third parameter is present, it returns x to the power of y, modulus z.
#如果提供第三個參數，則返回 x 的 y 次冪後，取餘 z。
#Syntax 語法
#pow(x, y, z)(基數,指數,餘數)
#Parameter參數：Values值
#Parameter參數：Description描述
#x：A number, the base
#x：數位，基數。
#y：A number, the exponent
#y：數字，指數。
#z：Optional. A number, the modulus
#z：可選。 數位，模數。
#Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):
#傳回 4 的 3 次方取餘 5（等同於 （4 * 4 * 4） % 5）：
x = pow(4, 3, 5)
print(x)

