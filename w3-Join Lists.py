#https://www.w3schools.com/python/python_lists_join.asp
#Python Join Lists 加入清單
#Join Two Lists 加入二個清單
#There are several ways to join, or concatenate, two or more lists in Python.
#在 Python 中加入或串聯兩個或多個清單有幾種方法。
#One of the easiest ways are by using the + operator.
#最簡單的方法之一是使用 + 操作員。
print("-------------Join(最簡單的方法之一是使用 + 操作員)")
#Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)            #['a', 'b', 'c', 1, 2, 3]
print(list1 + list2)    #['a', 'b', 'c', 1, 2, 3]


print("-------------Join(建立for迴圈,在迴圈裡建立append方法)")
#Another way to join two lists is by appending all the items 
# from list2 into list1, one by one:
#加入兩個清單的另一種方法是將清單 2 中的所有項目逐個附加到清單 1 中：
#Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x) #把list2的值代入到list1.append(x)
print(list1)

print("-----------------------Join(use the extend() method)")
#Or you can use the extend() method, which purpose is to add elements from one list to another list:
#或者，您可以使用extend（）方法，其目的是將一個清單中的元素添加到另一個清單：
#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2) #跟append一樣,先把值帶給前面的物件
print(list1) #['a', 'b', 'c', 1, 2, 3]
print(list1.extend(list2)) #None,extend擴展方法,是不帶值的
'''list1=['a', 'b', 'c', 1, 2, 3, 1, 2, 3]'''
#雖然輸出是None,但會就地改變list1的值,叫in-place
print(list1.append(list2)) #None,append新增方法,也是不帶值的
'''list1=['a', 'b', 'c', 1, 2, 3, 1, 2, 3, [1, 2, 3]]'''
#append添加在末尾[1, 2, 3]
#雖然輸出是None,但會就地改變list1的值,叫in-place
#append 可以理解成原封不動的放進去,所以在list1是輸出[1, 2, 3]
#extend 則是把 list 裡面的值一個一個放進去
#append & extend 都是 in-place(就地改變值) 的
print(list(list2)) #[1, 2, 3]
print(list1+list(list2))
#['a', 'b', 'c', 1, 2, 3, 1, 2, 3, [1, 2, 3], 1, 2, 3]
print(list1+list()) #list()是空清單
#['a', 'b', 'c', 1, 2, 3, 1, 2, 3, [1, 2, 3]]
print(list2+list()) #[1, 2, 3]
