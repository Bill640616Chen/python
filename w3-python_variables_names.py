#https://www.w3schools.com/python/python_variables_names.asp
#可變名稱
#變數可以有一個簡短的名稱（如 x 和 y）或一個更描述性的名稱
# （年齡、車名、total_volume）。Python 變數的規則：
#可變名稱必須從字母或下劃線字元開始
#可變名稱不能從數字開始
#可變名稱只能包含字母數位字元和下劃線（A-z、0-9 和 * ）
#可變名稱對案例敏感（年齡、年齡和年齡是三個不同的變數）

#合法可變名稱
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#非法可變名稱
'''2myvar = "John"
my-var = "John"
my var = "John"
'''

#多字可變名稱
#具有多個單詞的可變名稱可能難以讀取。
#有幾種技術，你可以使用，使他們更可讀性：
#駱駝箱
#每個單詞，除了第一個，以大寫字母開頭：
myVariableName = "John"
#帕斯卡爾案
#每個單字都以大寫字母開頭：
MyVariableName = "John"
#蛇案
#每個單字由底線字元分開：
my_variable_name = "John"