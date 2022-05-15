#https://www.w3schools.com/python/python_sets_join.asp
#Python Join Sets 加入集合
#Join Two Sets
#There are several ways to join two or more sets in Python.
#在python裡有很多方法把2個集合或更多集合加入
#You can use the union() method that returns a new set containing
# all items from both sets, or the update() method that inserts
# all the items from one set into another:
print("--------------------Join(union() method returns a new set )")
#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) #{'c', 1, 2, 'a', 3, 'b'}
#print(set1.union(set2))輸出一樣

print("--------------------Join(update() method inserts the items)")
#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) #{'c', 1, 2, 'a', 3, 'b'}
#同一時間輸出時,與union是佔相同記憶體的,結果相同
print(set1.update(set2)) #None,代表in place了
#Note: Both union() and update() will exclude any duplicate items.
#筆記：union() and update()這2個方法都排除重複的項目

print("-------------Join(intersection_update()只會保留2個集合共有的值)")
#Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.
#intersection_update()只會保留2個集合共有的值,不會傳回值
#Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x.intersection_update(y)) #none，print()裡是的要能傳回值
print(x) #{'apple'}，intersection_update(y)賦值給x
print("----傳回一個新set--Join(intersection()只會保留2個集合共有的值)")
#The intersection() method will return a new set, that only contains the items that are present in both sets.
#此方法會傳回一個新set
#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(x.intersection(y)) #{'apple'}
print(z) #{'apple'}
#print(x.intersection(y))輸出有值

print("---------------------Join(Keep All, But NOT the Duplicates)")
#Keep All, But NOT the Duplicates 保留全部,但不含共有的
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
#Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) #{'cherry', 'google', 'banana', 'microsoft'}
#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

#Return a set that contains all items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) #{'google', 'cherry', 'banana', 'microsoft'}
#print(x.symmetric_difference(y))輸出有值