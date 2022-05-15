#https://www.w3schools.com/python/gloss_python_remove_set_items.asp
#Remove Item from Set 從集中刪除項目
#To remove an item in a set, use the , or the method.remove()discard()
#要刪除集合中的項目，請使用該方法或方法。remove()discard()
#Remove "banana" by using the method:remove()
#使用該方法刪除「香蕉」：remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#Note: If the item to remove does not exist, will raise an error.remove()
#注意：如果要刪除的項目不存在，將引發錯誤。remove()
print('-------------分隔線------------')
#Remove "banana" by using the method:discard()
#使用該方法刪除「香蕉」：discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#Note: If the item to remove does not exist, will NOT raise an error.discard()
#注意：如果要刪除的項目不存在，則不會引發錯誤。discard()
#You can also use the , method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.pop()
#您也可以使用 「方法」刪除項目，但此方法將刪除最後一個項目。請記住，套裝是無序的，因此您不會知道刪除哪些項目。pop()
#The return value of the method is the removed item.pop()
#該方法的返回值是刪除的項目。pop()
print('-------------分隔線------------')
#Remove the last item by using the method:pop()
#使用該方法移除最後一個項目：pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
#Note: Sets are unordered, so when using the method, you will not know which item that gets removed.pop()
#注意：集合是無序的，所以當使用該方法時，您將不知道哪些項目被刪除。pop()
print('-------------分隔線------------')
#The method empties the set:clear()
#該方法清空了集合：clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
print('-------------分隔線------------')
#The keyword will delete the set completely:del
#關鍵字將完全刪除集合：del
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
#Related Pages 相關頁面
#Python Sets Tutorial Python 集合教程
#https://www.w3schools.com/python/python_sets.asp
#Set 集合
#https://www.w3schools.com/python/gloss_python_set.asp
#Access Set Items 訪問集合項目
#https://www.w3schools.com/python/gloss_python_access_set_items.asp
#Add Set Items 添加集合項目
#https://www.w3schools.com/python/gloss_python_add_set_items.asp
#Loop Set Items 迴圈集合項目
#https://www.w3schools.com/python/gloss_python_loop_set_items.asp
#Check if Set Item Exists 檢查是否存在集合項目
#https://www.w3schools.com/python/gloss_python_check_if_set_item_exists.asp
#Set Length 集合長度
#https://www.w3schools.com/python/gloss_python_set_length.asp
#Join Two Sets 合併兩個集合
#https://www.w3schools.com/python/gloss_python_join_sets.asp
