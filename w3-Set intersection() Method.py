#https://www.w3schools.com/python/ref_set_intersection.asp
#Python Set intersection() Method 集合intersection() Method方法
#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) #會傳回一個集合
print(z) #{'apple'}
#print(x.intersection(y)) #會傳回一個集合
#Return the intersection of two sets as a new set.
#(i.e. all elements that are in both sets.)

#Definition and Usage
#The intersection() method returns a set that contains the similarity between two or more sets.
#Meaning: The returned set contains only items that exist in both sets
# , or in all sets if the comparison is done with more than two sets.
#傳回集合只有同時存在兩個集合的項目,或者如果用兩套以上完成比較在所有集合裡
#Syntax
#set.intersection(set1, set2 ... etc)
#Parameter Values
#Parameter：escription
#set1：Required. The set to search for equal items in
#set2：Optional. The other set to search for equal items in.
#You can compare as many sets you like. 可以比較很多項目
#Separate the sets with a comma 要用逗號分開集合
#Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(x.intersection(y, z)) #{'c'}
print(result) #{'c'}
#如果其中一個集合沒有共同的元素,則傳回set()