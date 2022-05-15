#https://www.w3schools.com/python/ref_set_difference_update.asp
#Python Set difference_update() Method 集合difference_update()方法
#Remove the items that exist in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) 
print(x.difference_update(y)) #None,difference_update(y)不會傳回值
print(x) #{'banana', 'cherry'}
#Definition and Usage
#The difference_update() method removes the items that exist in both sets.
#difference_update() method移出的項目是同時存在兩個集合中
#The difference_update() method is different from the difference() 
# method, because the difference() method returns a new set, without 
# the unwanted items, and the difference_update() method removes 
# the unwanted items from the original set.
#difference_update() method跟difference() method不同,因為difference() 
# method會傳回一個集合,沒有不需要的項目,並difference_update() method
# 會從原始的集合移除不需要的項目

