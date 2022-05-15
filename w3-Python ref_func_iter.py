#https://www.w3schools.com/python/ref_func_iter.asp
#Python iter() Function Python iter()函數
#Returns an iterator object 返回反覆運算器物件。
#Create an iterator object, and print the items:
#建立反覆運算器物件，並列印專案：
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
#apple
#banana
#cherry
#Definition and Usage 定義和用法
#The iter() function returns an iterator object.
#iter（） 傳回反覆運算器物件。
#Syntax 語法
#iter(object, sentinel)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：Required. An iterable object
#object：必需。 可反覆運算物件。
#sentinel：Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentinel
#sentinel：可選。 如果對像是可調用物件，則當返回值與前哨相同時，反覆運算將停止。
#Related Pages 相關頁面
#The reversed() function returns a reversed iterator object.
#reversed（） 函數（返回反轉的反覆運算器物件）

