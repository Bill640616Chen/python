#https://www.w3schools.com/python/ref_set_difference.asp
#Python Set difference() Method 集合difference()方法
#Return a set that contains the items that only exist in set x, and not in set y:
#傳回一個集合含只存在x裡，沒有存在y裡的值
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) #x(只存在x裡項目).difference(y)不存在y裡的項目
print(z) #{'banana', 'cherry'}
#Definition and Usage
#The difference() method returns a set that contains the difference between two sets.
#Meaning: The returned set contains items that exist only in the first set, and not in both sets.
#Syntax
#set.difference(set)
#Parameter Values
#Parameter：Description
#set：Required. The set to check for differences in
#Reverse the first example. Return a set that contains the items that only exist in set y, and not in set x:
#把範例反過來
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z) #{'google', 'microsoft'}
print(y.difference(x)) #{'google', 'microsoft'}因為difference會傳回set