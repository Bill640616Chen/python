#https://www.w3schools.com/python/gloss_python_json.asp
#Python JSON Parse 
#Parse JSON - Convert from JSON to Python 從 JSON 轉換為 Python
#If you have a JSON string, you can parse it by using the method.json.loads()
#如果您有 JSON 字串，則可以使用該方法對其進行分析。json.loads()
#The result will be a Python dictionary.
#結果將是一個Python字典。
#https://www.w3schools.com/python/python_dictionaries.asp
#Convert from JSON to Python:
#從 JSON 轉換為 Python：
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
#Related Pages 相關頁面
#Python JSON Tutorial
#https://www.w3schools.com/python/python_json.asp
#JSON
#https://www.w3schools.com/python/gloss_python_json.asp
#Convert into JSON 轉換為 JSON
#https://www.w3schools.com/python/gloss_python_convert_into_JSON.asp
#Format JSON 格式化 JSON
#https://www.w3schools.com/python/gloss_python_format_json.asp
#Sort JSON 排序 JSON
#https://www.w3schools.com/python/gloss_python_json_sort.asp