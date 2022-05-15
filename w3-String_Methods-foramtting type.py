#https://www.w3schools.com/python/ref_string_format.asp
#Python 字串 format() Method
myorder = "I want {} pieces of item {} for {} dollars.".format(3,567,49.95)
print(myorder) #對照w3-格式字申.py#I want 3 pieces of item 567 for 49.95 dollars.
#格式化類型
#在佔位元內部，您可以添加格式類型來格式化結果：
#:<：Left aligns the result (within the available space)左側對齊結果（在可用空間內）
txt = "We have {:<5} chickens."
print(txt.format(271)) 
#We have 271   chickens.5格,所以右邊隔2個空格,271算佔3個位置,與左側對齊
#左側對齊,chickens的左側
#:>：Right aligns the result (within the available space)右對齊結果（在可用空間內）
txt = "We have {:>5} chickens."
print(txt.format(22)) 
#We have    22 chickens.5格,所以左邊隔3個空格,22算佔2個位置,22與右側對齊
#右側對齊,have的右側
#:^：Center aligns the result (within the available space)
#中心對齊結果（在可用空間內）
txt = "We have {:^6} chickens."
print(txt.format(25)) #We have   25   chickens.因為是置中對齊,所以兩邊各3個空格
#:=：Places the sign to the left most position將標誌放在最左邊的位置
txt = "The temperature is {:=10} degrees celsius."
print(txt.format(-5)) #The temperature is -        5 degrees celsius.
#-距離5,有8格,所以—跟5各佔一個位置
#:+：Use a plus sign to indicate if the result is positive or negative
#使用加號表示結果是正面還是陰性(反面)
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7)) 
#The temperature is between -3 and +7 degrees celsius.
#:-：Use a minus sign for negative values only僅使用負值的減號
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7)) 
#The temperature is between -3 and 7 degrees celsius.

txt = "The temperature is between {:+} and {:-} degrees celsius."
print(txt.format(-3, 7)) 
#The temperature is between -3 and 7 degrees celsius.
txt = "The temperature is between {:-} and {:+} degrees celsius."
print(txt.format(-3, 7)) 
#The temperature is between -3 and +7 degrees celsius.
#右邊的{}裡面+-決定輸出有沒有+號,左邊的{},不管改為+-,因為是負數,所以輸出都有-

#:：Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
#使用空間在正數之前插入額外空間（負數前的減號）
txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
#The temperature is between -3 and  7 degrees celsius.插了1格
#:,：Use a comma as a thousand separator使用逗號做為千分點
txt = "The universe is {:,} years old."
print(txt.format(13800000000))
#The universe is 13,800,000,000 years old.
#:_：Use a underscore as a thousand separator使用_做為千分點
txt = "The universe is {:_} years old."
print(txt.format(13800000000))
#The universe is 13_800_000_000 years old.
#:b：Binary format二進位格式
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))#The binary version of 5 is 101
#:c：Converts the value into the corresponding unicode character
#將值轉換為相應的unicode字元
txt = "The binary version of {0} is {0:c}"
print(txt.format(2566))#The binary version of 2566 is ਆ
#:d：Decimal format十進位格式
##Use "d" to convert a number, in this case a binary number, into decimal number format:
#二進位的數字轉換位十進位的數字
txt = "We have {:d} chickens."
print(txt.format(0b101)) #We have 5 chickens.
#:e：Scientific format, with a lower case e科學格式，帶小寫e
#Use "e" to convert a number into scientific number format (with a lower-case e):
txt = "We have {:e} chickens."
print(txt.format(5)) #We have 5.000000e+00 chickens.
#:E：Scientific format, with an upper case E科學格式，帶大寫E
txt = "We have {:E} chickens."
print(txt.format(5)) #have 5.000000E+00 chickens.
#:f：Fix point number format固定點的數字格式
##Use "f" to convert a number into a fixed point number, 
# default with 6 decimals, but use a period followed by a number 
# to specify the number of decimals:
#使用f轉換一個數字到有小數點的數字,預設是6個0,但是使用一個時期，然後是一個數位
# 指定小數點位數
txt = "The price is {:.2f} dollars."
print(txt.format(45)) #The price is 45.00 dollars.指定2位
#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(45)) #The price is 45.000000 dollars.預設6位
#:F：Fix point number format, in uppercase format (show inf and nan as INF and NAN)
#小數點數字格式,用大寫格式
#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x)) #The price is INF dollars.
#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x)) #The price is inf dollars.
#:g：General format
#:G：General format (using a upper case E for scientific notations)
#scientific notations科學註釋
txt = "We have {:g} chickens." #g,G都是同個結果
print(txt.format(5)) #We have 5 chickens.
#:o：Octal format 8進位格式
#Use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10)) #The octal version of 10 is 12
#:x：Hex format, lower case 6進位,小寫
#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255)) #The Hexadecimal version of 255 is ff
#:X：Hex format, upper case 6進位,大寫
#Use "X" to convert the number into upper-case Hex format:
txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255)) #The Hexadecimal version of 255 is FF
#:n：Number format數字格式
txt = "The Hexadecimal version of {0} is {0:n}"
print(txt.format(255)) #The Hexadecimal version of 255 is 255
#:%：Percentage format百分比格式
#Use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25)) #You scored 25.000000%,預設6個0
#Or, without any decimals:沒有任何小數
txt = "You scored {:.0%}"
print(txt.format(0.25)) #You scored 25%,因為0%是沒有小數