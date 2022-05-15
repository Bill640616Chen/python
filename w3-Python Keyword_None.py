#https://www.w3schools.com/python/ref_keyword_none.asp
#Python Keyword None 關鍵字 None
#Represents a null value
#表示 null 值。
#Assign the value None to a variable:
#賦值 None 給一個變數：
x = None
print(x)
#Definition and Usage 定義和用法
#The None keyword is used to define a null value, or no value at all.
#None 關鍵字用於定義 null 值，或根本沒有值。
#None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None.
#None 與 0、False 或空字串不同。 None 是其自身的數據類型（NoneType），並且只有 None 可以是 None。
#If you do a boolean if test, what will happen? Is None True or False:
print('-------------分隔線------------')
#如果您進行布爾型 if 測試，將會發生什麼？ None 是 True 還是 False：
x = None
if x:
  print("Do you think None is True?")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")
