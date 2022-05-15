#https://www.w3schools.com/python/python_regex.asp#sub
#Python RegEx (Regular Expression)正則表示式
#The sub() Function ：
print("-----------------------------函數把符合取代為您選擇的文字")
#The sub() Function ：
#函數把符合取代為您選擇的文字
#The sub() function replaces the matches with the text of your choice:
#sub（） 函數把符合取代為您選擇的文字：
#Replace every white-space character with the number 9:
#用數字 9 取代每個空白字元：
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
#把空白取代為9
print(x)
#The9rain9in9Spain
#You can control the number of replacements by specifying the count parameter:
#您可以透過指定 count 參數來控制替換次數：
#Replace the first 2 occurrences:
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
#把"２"空白取代為9
print(x)
#The9rain9in Spain
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 6)
#把"６"空白取代為9,就算超出裡面的空白數,則以裡面的數量為主
print(x)
#The9rain9in Spain

print("---------------------比對物件是包含有關搜尋和結果信息的物件")
#Match Object 比對物件
#A Match Object is an object containing information about the search and the result.
#比對物件是包含有關搜尋和結果信息的物件。
#Note: If there is no match, the value None will be returned, instead of the Match Object.
#註釋：如果沒有比對，則傳回值 None，而不是 Match 物件。
#Do a search that will return a Match Object:
#執行會傳回 Match 物件的搜尋：
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
#<re.Match object; span=(5, 7), match='ai'>

#The Match object has properties and methods used to retrieve 
# information about the search, and the result:
#Match 物件提供了用於取回有關搜尋及結果資訊的屬性和方法：
#.span() returns a tuple containing the start-, and end 
# positions of the match.
#span（） 傳回的tuple包含了比對的開始和結束位置
#.string returns the string passed into the function
#.string 傳入函數的字串
#.group() returns the part of the string where there was a match
#group（） 傳回比對的字串部分
#Print the position (start- and end-position) of the first match occurrence.
#列印首個比對出現的位置（開始和結束位置）。
#The regular expression looks for any words that starts with an upper case "S":
#正規表示式查找以大寫 「C」 開頭的任何單詞：
import re
txt = "The rain in Spain"
x = re.search(r"\bS", txt)
#\b：傳回指定字元位於單詞的開頭或末尾的比對項
print(x.span())#(12, 13)
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
#r：開頭的"r"是確保字串被視為"原始字串"
#\b：傳回指定字元位於單詞的開頭或末尾的比對項
#\w：匹配包括底線的任何單詞字元。等價於“[A-Za-z0-9_]”。
#+：匹配前面的子運算式一次或多次。例如，“zo+”能匹配“zo”以及“zoo”，
# 但不能匹配“z”。+等價於{1,}。
print(x.span())#(12, 17)
#\w：匹配\bS後面那個字
#span()傳回的tuple包含了比對的開始和結束位置
#+：比對了pain(13,14,1,5,16)pain最後位置為17匹配前面的子運算式一次或多次。
# 例如，“zo+”能匹配“zo”以及“zoo”,p一次,a二次,i三次,n四次
import re
txt = "The rain in Spbin"
x = re.search(r"\bS\w", txt)
print(x.span())#(12, 14)
#\w是比對到p,結束位置在p的後面
print("---------------------測試裡面去除檢索的字符,輸出字中是否相同")
#Print the string passed into the function:
#列印傳入函數的字串：
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
x = re.search(r"\bS\w", txt)
print(x.string)
x = re.search(r"\bS", txt)
print(x.string)
x = re.search(r"\s", txt)
print(x.string)
import re
txt = "The rain in Spain"
x = re.search(r"e\b", txt)
print(x.string)
#The rain in Spain
#The rain in Spain
#The rain in Spain
#The rain in Spain

print("--------------------------group（） 傳回比對的字串部分")
#Print the part of the string where there was a match.
#列印匹配的字串部分。
#The regular expression looks for any words that starts with an upper case "S":
#正規表示式查找以大寫 「S」 開頭的任何單詞：
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
#\b：傳回指定字元位於單詞的開頭或末尾的比對項
#\w：匹配包括底線的任何單詞字元。等價於“[A-Za-z0-9_]”。
#+：匹配前面的子運算式一次或多次。例如，“zo+”能匹配“zo”以及“zoo”，
print(x.group())
import re
txt = "The_rain in Spain"
x = re.search(r"\w", txt) #檢查字尾有沒有e
print(x.group())
#Note: If there is no match, the value None will be returned, instead of the Match Object.
#註釋：如果沒有匹配項，則返回值 None，而不是 Match 物件。

