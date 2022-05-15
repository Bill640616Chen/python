#https://www.w3schools.com/python/python_lists_sort.asp
#Python Sort Lists 排序列表
#Sort List Alphanumerically 按字母順序排列清單
#List objects have a sort() method that will sort the list 
# alphanumerically, ascending, by default:
#清單物件有一個排序（）方法，將按字母數位對清單進行排序，預設情況下會提升：
print("---------------依字母順序對清單進行排序：")
#Sort the list alphabetically: 依字母順序對清單進行排序：
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

print("------------------依數字對清單進行排序：")
#Sort the list numerically: 依數字對清單進行排序：
thislist = [100, 50, 65, 82, 23]
list1 = ["aa","bb"]
thislist.sort() #只能先用方法排序完,才能輸出
print(thislist) #[23, 50, 65, 82, 100]
print(thislist.sort()) #None
#sort方法是無值的,所以沒辦法寫在一起

print("------------------Sort Descending 排序下降測試-1")
#Sort Descending 排序下降
#To sort descending, use the keyword argument reverse = True:
#要排序下降，請使用關鍵字參數 reverse = True:
#Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']
print(thislist.sort(reverse = False)) #None
thislist.sort(reverse = False)
print(thislist) #['banana', 'kiwi', 'mango', 'orange', 'pineapple']

print("------------------Sort Descending 排序下降測試-2")
#Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) #[100, 82, 65, 50, 23]
