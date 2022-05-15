#https://www.w3schools.com/python/ref_string_isalpha.asp
#Python 字串 isalpha() Method
#檢查文字中的所有字元是否都是字母：
txt = "CompanyX"
x = txt.isalpha() #alpha是alphabet的簡寫
print(x) #True
#定義和使用
#如果所有字元都是字母字母（a-z），則方法返回正確。isalpha()
#不是字母字母的字元示例：（空間）！等。
#語法
#string.isalpha()
#檢查文字中的所有字元是否為字母：
txt = "Company10"
x = txt.isalpha()
print(x) #False
