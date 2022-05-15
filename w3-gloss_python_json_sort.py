#https://www.w3schools.com/python/gloss_python_json_sort.asp
#Python JSON Sort 從 Python 轉換為 JSON
#Sort the Result 對結果進行排序
#The method has parameters to order the keys in the result:json.dumps()
#該方法具有用於對結果中的鍵進行排序的參數：json.dumps()
#Use the parameter to specify if the result should be sorted or not:sort_keys
#使用該參數指定是否應對結果進行排序：sort_keys
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
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
#Related Pages 相關頁面
#Python JSON Tutorial
#https://www.w3schools.com/python/python_json.asp
#JSON
#https://www.w3schools.com/python/gloss_python_json.asp
#Parse JSON 解析 JSON
#https://www.w3schools.com/python/gloss_python_json_parse.asp
#Convert into JSON 轉換為 JSON
#https://www.w3schools.com/python/gloss_python_convert_into_JSON.asp
#Format JSON 格式化 JSON
#https://www.w3schools.com/python/gloss_python_format_json.asp
