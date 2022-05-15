#https://www.w3schools.com/python/ref_set_issuperset.asp
#Python Set issuperset() Method 集合issuperset() 方法
#Returns whether this set contains another set or not
#傳回此集合是否包含另一組集合
#Return True if all items set y are present in set x:
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) #檢查y集合裡的項目是否"被"包含在x集合裡
print(z) #True
#Definition and Usage
#The issuperset() method returns True if all items in the specified
#  set exists in the original set, otherwise it retuns False.
#issuperset() method 如果指定的集合中的所有項目存在於原始的集合裡傳回True
# ,否則傳回False
#Syntax
#set.issuperset(set)
#Parameter Values
#Parameter：Description
#set：Required. The set to search for equal items in
#What if not all items are present in the specified set?
#Return False if not all items in set y are present in set x:
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y) #檢查y集合裡的項目是否"被"包含在x集合裡
print(z) #False #因為x裡沒有"a"
