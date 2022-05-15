#https://www.w3schools.com/python/python_regex.asp#split
#Python RegEx (Regular Expression)正則表示式
#split() Function split()函數
#The split() function returns a list where the string has been 
# split at each match:
#split() function拆分函數傳回一個清單裡面的字串已經被拆分為每一個比對
#Split at each white-space character:
#拆分每一個空白字元
import re #導入正則表示式
txt = "The rain in Spain"
x = re.split("\s", txt)
#\s：Returns a match where the string contains a white space
# character
#傳回包含空白字元的字串比對
print(x)

print("--------------------------------拆分字串只在第一事件發生時")
#You can control the number of occurrences by specifying the maxsplit parameter:
#你可以控制發生的次數靠著指定最大拆分的參數
#Split the string only at the first occurrence:
#拆分字串只在第一事件發生時
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1) 
#['The', 'rain in Spain']
#\s：傳回包含空白字元的字串比對，１代表刪幾個字元,超出既的數量也沒關係
print(x)
import re
txt = "The rain in Spain"
x = re.split("a", txt, 6) 
print(x)

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
#\w：匹配pain(13,14,1,5,16)pain最後位置為17
#span()傳回的tuple包含了比對的開始和結束位置
#+：匹配前面的子運算式一次或多次。例如，“zo+”能匹配“zo”以及“zoo”
#p一次,a二次,i三次,n四次
