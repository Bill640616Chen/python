#https://www.w3schools.com/python/ref_set_symmetric_difference.asp
#Python Set symmetric_difference() Method 集合symmetric_difference()方法
#Returns a set with the symmetric differences of two sets
#傳回具有兩組集合對稱差異的一組集合
#Return a set that contains all items from both sets, except items that are present in both sets:
#傳回一組set包含兩個集合的所有項目,除了共同項目以外,其他都有
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print(x.symmetric_difference(y)) #結果跟１２行同
#因為在print傳回值代表物件
z = x.symmetric_difference(y) #有傳回值
print(z) #{'banana', 'google', 'microsoft', 'cherry'}
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference(y) #有傳回值,物件.屬性,屬性不會執行
#只是一個方法,並沒有給它變數,所以不會執行
print(x.symmetric_difference(y))
#{'banana', 'microsoft', 'cherry', 'google'}
print(x) #{'banana', 'cherry', 'apple'},這裡的集合是第13行
#x.symmetric_difference(y)必須要有變數,才能傳回新集合
#Definition and Usage
#The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
#Meaning: The returned set contains a mix of items that are not present in both sets.
#Syntax
#set.symmetric_difference(set)
#Parameter Values
#Parameter：Description
#set：Required. The set to check for matches in