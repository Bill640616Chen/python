#https://www.w3schools.com/python/ref_string_encode.asp
#Python 字串 encode () Method
#UTF-8 編碼字串：
txt = "My name is Ståle"
x = txt.encode()
print(x) #b'My name is St\xc3\xa5le'
#定義和使用
#該方法使用指定的編碼對字串進行編碼。如果沒有指定編碼，將使用UTF-8。encode()
#string.encode(encoding=encoding, errors=errors)
#參數值
#Parameter(參數)：Description(描述)
#encoding(編碼)：Optional(自選) A String specifying the encoding to use. Default is UTF-8
#errors(錯誤)：Optional(自選) A String specifying the error method. Legal values are:
#指定錯誤方法的字串。合法值包括：
#'backslashreplace'	- uses a backslash instead of the character that could not be encoded
#使用反斜線而不是無法編碼的字元
#'ignore'	        - ignores the characters that cannot be encoded
#忽略無法編碼的字元
# 'namereplace'	    - replaces the character with a text explaining the character
#用解釋字元的文本替換字元
# 'strict'      	- Default, raises an error on failure
#默認，導致故障錯誤,此參數無法輸出
#'replace'      	- replaces the character with a questionmark
#用問號替換字元
#'xmlcharrefreplace'- replaces the character with an xml character
#用 xml 字元替換字元
#這些範例使用 ascii 編碼和無法編碼的字元，顯示具有不同錯誤的結果：
txt = "My name is Ståle"
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
#b'My name is St\\xe5le'
#b'My name is Stle'
#b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
#b'My name is St?le'
#b'My name is St&#229;le'