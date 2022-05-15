#https://www.w3schools.com/python/python_operators.asp
#Python Operators
#Operators are used to perform operations on variables and values.
#操作員用於對變數和值執行操作。
#In the example below, we use the operator to add together two values:+
#In the example below, we use the operator to add together two values:+
print(10 + 5) #15
#Python divides the operators in the following groups:
#Python 將操作員分為以下組
#Membership operators 會員運營商
#Membership operators are used to test if a sequence is presented in an object:
#成員操作員用於測試物件中是否顯示序列：
#Operator	Description	                                     Example
#in 	    Returns True if a sequence with the specified    x in y
#           value is present in the object	
#           如果物件中存在具有指定值的序列，則傳回True
#not in	    Returns True if a sequence with the specified    x not in y
#           value is not present in the object	
#           如果物件中不存在具有指定值的序列，則傳回True
x = ["apple", "banana"]
print("banana" in x) #True
x = ["apple", "banana"]
print("pineapple" not in x) #False