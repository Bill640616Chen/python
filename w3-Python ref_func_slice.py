#https://www.w3schools.com/python/ref_func_slice.asp
#Python slice() Function Python slice()函數
#Returns a slice object
#返回 slice 物件。
#Create a tuple and a slice object. Use the slice object to get only the two first items of the tuple:
#創建一個元組和一個 slice 物件。 使用 slice 物件僅獲取元組的前兩項：
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])
#從索引位置2裁切,列印出2以前的值
#Definition and Usage 定義和用法
#The slice() function returns a slice object.
#slice（） 函數返回 slice 物件（切片）。
#A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.
#slice 對象用於指定如何對序列進行裁切。 您可以指定在哪裡開始裁切以及在哪裡結束裁切。 您還可以指定步進，例如只切每隔一個專案。
#Syntax 語法
#slice(start, end, step)
#Parameter參數：Values值
#Parameter參數：Description描述
#start：Optional. An integer number specifying at which position to start the slicing. Default is 0
#start：可選。 整數，指定在哪個位置開始裁切。 預設為 0。
#end：An integer number specifying at which position to end the slicing
#end：可選。 整數，指定在哪個位置結束裁切。
#step：Optional. An integer number specifying the step of the slicing. Default is 1
#step：可選。 整數，指定裁切的步進值。 預設為 1。
#Create a tuple and a slice object. Start the slice object at position 3, and slice to position 5, and return the result:
print('-------------分隔線------------')
#創建一個元組和一個切片物件。 在位置 3 處啟動切片物件，並在位置 5 處裁切，並返回結果：
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])
#Create a tuple and a slice object. Use the step parameter to return every third item:
print('-------------分隔線------------')
#創建一個元組和一個切片物件。 使用 step 參數返回每第三個專案：
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

