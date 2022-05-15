#https://www.w3schools.com/python/ref_string_isalnum.asp
#Python 字串 isalnum() Method
#檢查文字中的所有字元是否為字母數字alphanumeric：
txt = "Company12"
x = txt.isalnum() #alnum為alphanumeric簡寫
print(x) #True
#定義和使用
#如果所有字元都是字母數，則方法返回 True，意思是字母字母（a-z）和數位 （0-9）。isalnum()
#不是字母數字的字元示例：（空間）！#%=？等。
#語法
#string.isalnum()
#檢查文字中的所有字元是否為字母數字：
txt = "Company 12"
x = txt.isalnum() #空格不符合
print(x) #False
