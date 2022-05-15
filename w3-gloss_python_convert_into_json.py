#https://www.w3schools.com/python/gloss_python_convert_into_JSON.asp
#Convert From Python to JSON 從 Python 轉換為 JSON
#If you have a Python object, you can convert it into a JSON string by using the method.json.dumps()
#如果您有一個 Python 物件，則可以使用該方法將其轉換為 JSON 字串。json.dumps()
#Convert from Python to JSON:
#從 Python 轉換為 JSON：
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
#You can convert Python objects of the following types, into JSON strings:
#您可以將以下類型的 Python 物件轉換為 JSON 字串：
#dict 字典
#list 清單
#tuple 元組
#string 字串
#int int
#float 浮點
#True 真
#False 假
#None 沒有
print('-------------分隔線------------')
#Convert Python objects into JSON strings, and print the values:
#將 Python 物件轉換為 JSON 字串，並列印值：
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
#當您從 Python 轉換為 JSON 時，Python 物件將轉換為等效的 JSON （JavaScript）：
#Python：JSON
#dict：Object
#list：Array
#tuple：Array
#str：String
#int：Number
#float：Number
#True：true
#False：false
#None：null
print('-------------分隔線------------')
#Convert a Python object containing all the legal data types:
#轉換包含所有合法資料類型的 Python 物件：
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
#Related Pages 相關頁面
#Python JSON Tutorial
#https://www.w3schools.com/python/python_json.asp
#JSON
#https://www.w3schools.com/python/gloss_python_json.asp
#Parse JSON 解析 JSON
#https://www.w3schools.com/python/gloss_python_json_parse.asp
#Format JSON 格式化 JSON
#https://www.w3schools.com/python/gloss_python_format_json.asp
#Sort JSON 排序 JSON
#https://www.w3schools.com/python/gloss_python_json_sort.asp