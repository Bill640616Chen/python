#https://www.w3schools.com/python/ref_func_globals.asp
#Python globals Function Python globals函數
#Returns the current global symbol table as a dictionary
#以字典返回當前全域符號表。
#Display the global symbol table:
#顯示全域符號表：
x = globals()
print(x)
#Definition and Usage 定義和用法
#The globals() function returns the global symbol table as a dictionary.
#globals（） 函數將全域符號表作為字典返回。
#A symbol table contains necessary information about the current program
#符號表包含有關當前程式的必要資訊。
#Syntax 語法
#globals()
#Parameter參數：Values值
#No parameters 無參數
print('-------------------分隔線------------------')
#Get the filename of the current program:
#取得目前的程式名稱：
x = globals()
print(x["__file__"])
