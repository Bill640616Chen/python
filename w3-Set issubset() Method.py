#https://www.w3schools.com/python/ref_set_issubset.asp
#Python Set issubset() Method 集合issubset() 方法
#Returns whether another set contains this set or not
#傳回另一組集合是否包含此集合
#適用於x集合數量小於y集合數量
#Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
q = y.issubset(x) #檢查x裡面有沒有y裡所有的項目
print(q) #False
z = x.issubset(y) #檢查y裡面有沒有x裡所有的項目
print(z) #True
#Definition and Usage
#The issubset() method returns True if all items in the set 
# exists in the specified set, otherwise it retuns False.
#issubset() method如果集合的所有項目存在於指定集合的項目就傳回True,
# 否則就傳回False
#Syntax
#set.issubset(set)
#Parameter Values
#Parameter：Description
#set：Required. The set to search for equal items in
#What if not all items are present in the specified set?
#Return False if not all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y) #檢查y裡面有沒有x裡所有的項目
print(z) #False #因為y裡面沒有"a"