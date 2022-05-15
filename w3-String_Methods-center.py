#https://www.w3schools.com/python/ref_string_center.asp
#Python 字串 center() Method
#列印「香蕉」一詞，佔據20個字元的空間，中間是「香蕉」：
txt = "banana"
x = txt.center(20)
print(x) #       banana       ,banana共6個字元,前後各7個空白字元,共20字元
#定義和使用
#該方法將以字元字元（空間預設值）作為填充字元對齊字元的中心對齊字串。center()
#語法
#string.center(length, character) 
#參數值
#Parameter(參數)：Description(描述)
#length：Required. The length of the returned string
#長度：必填，返回字串的長度
#character：Optional. The character to fill the missing space on each side. Default is " " (space)
#字元：自選，填補每邊缺失空間的字元。預設值為 " （空間）只能有一個字元
#使用字母「O」作為填充字元：
txt = "banana"
x = txt.center(20, "O")
print(x) #OOOOOOObananaOOOOOOO,用字母O填補原來的空白空間,一邊7個
#print(txt.center(20,'O'))也可以