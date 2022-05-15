#https://www.w3schools.com/python/gloss_python_regex_match.asp
#Python RegEx Match Object 正規表示式符合物件
#A Match Object is an object containing information about the search and the result.
#匹配物件是包含有關搜尋和結果的信息的物件。
#Do a search that will return a Match Object:
#執行將傳回符合物件的搜尋：
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
#Note: If there is no match, the value None will be returned, instead of the Match Object.
#注意：如果沒有匹配項，則將返回該值，而不是 Match 物件。None
#The Match object has properties and methods used to retrieve information about the search, and the result:
#Match 物件具有用於檢索有關搜尋的資訊和結果的屬性和方法：
#.span() returns a tuple containing the start-, and end positions of the match.
#.span()返回一個元組，其中包含匹配項的開始位置和結束位置。
#returns the string passed into the function
#返回字串傳遞到函數
#.group() returns the part of the string where there was a match
#.group()返回字串中存在匹配項的部分.string.group()
#Print the position (start- and end-position) of the first match occurrence.
#列印第一個匹配匹配項的位置（開始位置和結束位置）。
print('-------------分隔線------------')
#The regular expression looks for any words that starts with an upper case "S":
#正規表示式查找以大寫字母「S」開頭的任何單詞：
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print('-------------分隔線------------')
#Print the string passed into the function:
#列印傳遞到函數中的字串：
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
#Print the part of the string where there was a match.
#列印字串中存在匹配項的部分。
print('-------------分隔線------------')
#The regular expression looks for any words that starts with an upper case "S":
#正規表示式查找以大寫字母「S」開頭的任何單詞：
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
#Note: If there is no match, the value None will be returned, instead of the Match Object.
#注意：如果沒有匹配項，則將返回該值，而不是 Match 物件。None
#Related Pages 相關頁面
#Python RegEx Tutorial Python 正則表達式教程
#https://www.w3schools.com/python/python_regex.asp
#RegEx 正則表達式
#https://www.w3schools.com/python/gloss_python_regex.asp
#RegEx Functions 正則表達式函數
#https://www.w3schools.com/python/gloss_python_regex_functions.asp
#Metacharacters in RegEx 正則表達式中的元字元
#https://www.w3schools.com/python/gloss_python_regex_metacharacters.asp
#RegEx Special Sequences 正則表達式特殊序列
#https://www.w3schools.com/python/gloss_python_regex_sequences.asp
#RegEx Sets 正則表達式集
#https://www.w3schools.com/python/gloss_python_regex_sets.asp
