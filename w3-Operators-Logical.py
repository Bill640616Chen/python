#https://www.w3schools.com/python/python_operators.asp
#Python Operators
#Operators are used to perform operations on variables and values.
#操作員用於對變數和值執行操作。
#In the example below, we use the operator to add together two values:+
#In the example below, we use the operator to add together two values:+
print(10 + 5) #15
#Python divides the operators in the following groups:
#Python 將操作員分為以下組
#Logical operators    邏輯操作員
#Logical operators are used to combine conditional statements:
#邏輯操作員用於組合條件語句：
#Operator	Description	                                                
#and 	    Returns True if both statements are true	
#           傳回True,如果兩個陳述式都是True
#Example:x < 5 and  x < 10
x = 5
print(x > 3 and x < 10) #True
a =10
b =20
print(a and b) #20
#如果 x 為 True，x and y 返回 True，否則它返回 y 的計算值。
#a 和 b 為數值變數, 則 and 和 or 為邏輯運算, 判斷是否為0. 0為False, 非0為True. 
#and 運算有包含0, 則返回0; 如果無0, 則返回後值.

#or     	Returns True if one of the statements is true  
#           傳回True,如果其中一個陳述式是True
#Example:x < 5 or x < 4	
x = 5
print(x > 3 or x < 4) #True
a =10
b =20
print(a or b) #10
#如果 x 是非 0，它返回 x 的計算值，否則它返回 y 的計算值。
#or 運算中有包含非0值時, 返回第一個非0值.

#not	    Reverse the result, returns False if the result is true
#           反轉結果，如果結果屬實，則傳回錯誤
#Example:not(x < 5 and x < 10)
x = 5
print(not(x > 3 and x < 10)) #(x > 3 and x < 10)屬實,False
a =10
b =20
print(not(a and b)) #(a and b)True,not後而False
#如果 x 為 True，返回 False 。 如果 x 為 False，它返回 True。