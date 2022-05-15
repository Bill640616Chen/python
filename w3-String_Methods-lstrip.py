#https://www.w3schools.com/python/ref_string_lstrip.asp
#Python 字串 lstrip() Method
#Returns a left trim version of the string返回字串的左邊修剪版本
#刪除字串左側的空間：
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
#of all fruits banana      is my favorite
#定義和使用
#該方法刪除任何主角（空間是要刪除的預設領導字元）lstrip()
#語法
#string.lstrip(characters)
#參數值
#Parameter(參數)：Description(描述)
#characters(字元)：Optional(自選).
#A set of characters to remove as leading characters
#要刪除為主角的字元集
#刪除主角：
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw") #banana
print(x)