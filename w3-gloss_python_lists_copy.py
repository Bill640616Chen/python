#https://www.w3schools.com/python/gloss_python_copy_list.asp
#copy 複製
#You cannot copy a list simply by typing , because: will only be a reference to , and changes made in will automatically also be made in .list2 = list1list2list1list1list2
#你不能簡單地通過鍵入來複製清單，因為：將只引用，並在其中做出的更改也會自動進行。list2 = list1list2list1list1list2
#There are ways to make a copy, one way is to use the built-in List method . copy()
#有辦法複製，一種方法是使用內置清單方法。 copy()
#Make a copy of a list with the method:copy()
#使用該方法複製清單：copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#Another way to make a copy is to use the built-in method .list()
#製作副本的另一種方法是使用內置方法。list()
print('-------------分隔線------------')
#Make a copy of a list with the method:list()
#使用該方法複製清單：list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#Related Pages 相關頁面
#Python Lists Tutorial Python 清單教程
#https://www.w3schools.com/python/python_lists.asp
#Lists 清單
#https://www.w3schools.com/python/gloss_python_lists.asp
#Access List Items 訪問清單項目
#https://www.w3schools.com/python/gloss_python_access_list_items.asp
#Change List Item 更改清單項目
#https://www.w3schools.com/python/gloss_python_change_list_item.asp
#Loop List Items 迴圈清單項目
#https://www.w3schools.com/python/gloss_python_loop_list_items.asp
#List Comprehension 清單理解
#https://www.w3schools.com/python/gloss_python_list_comprehension.asp
#Check If List Item Exists 檢查清單項目是否存在
#https://www.w3schools.com/python/gloss_python_check_if_list_item_exists.asp
#List Length 清單長度
#https://www.w3schools.com/python/gloss_python_list_length.asp
#Add List Items 添加清單項目
#https://www.w3schools.com/python/gloss_python_add_list_items.asp
#Remove List Items 刪除清單項目
#https://www.w3schools.com/python/gloss_python_remove_list_items.asp
#Join Two Lists 加入兩個清單
#https://www.w3schools.com/python/gloss_python_join_lists.asp