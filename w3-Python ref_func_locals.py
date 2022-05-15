#https://www.w3schools.com/python/ref_func_locals.asp
#Python locals() Function Python locals()函數
#Returns an updated dictionary of the current local symbol table
#返回當前本地符號表的更新字典。
#Dispaly the local symbol table:
#顯示局部符號表：
x = locals()
print(x)
#Definition and Usage 定義和用法
#The locals() function returns the local symbol table as a dictionary.
#locals（） 函數將局部符號表作為字典返回。
#A symbol table contains necessary information about the current program.
#符號表包含有關當前程式的必要資訊。
#Syntax 語法
#locals()
#Parameter參數：Values值
#No parameters無參數
#Get the filename of the current program:
print('-------------分隔線------------')
#取得目前的程式名稱：
x = locals()
print(x["__file__"])
