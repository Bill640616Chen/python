#https://www.w3schools.com/python/ref_set_isdisjoint.asp
#Python Set isdisjoint() Method 集合isdisjoint() 方法
#返回兩組是否有交叉點
#Return True if no items in set x is present in set y:
#傳回True，如果在x,y的集中裡都沒有項目
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) #True
print(z) #True
#Definition and Usage
#The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
#isdisjoint() method如果兩個都集合沒共同的項目就傳回True,否則就傳回False
#Syntax
#set.isdisjoint(set)
#Parameter Values
#Parameter：Description
#set：Required. The set to search for equal items in
#What if no items are present in both sets? 傳回True
#Return False if one ore more items are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z) #False
print(x.isdisjoint(y)) #False