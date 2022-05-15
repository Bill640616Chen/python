#https://www.w3schools.com/python/gloss_python_format_json.asp
#Python Format JSON 從 Python 轉換為 JSON
#Format the Result 設置結果格式
#The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
#上面的示例列印了一個 JSON 字串，但它不是很容易閱讀，沒有縮進和換行符。
#The method has parameters to make it easier to read the result:json.dumps()
#該方法具有參數，以便於讀取結果：json.dumps()
#Use the parameter to define the numbers of indents:indent
#使用該參數定義縮進數：indent
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
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
#You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
#您還可以定義分隔符，預設值為 （"， "， "： "），這意味著使用逗號和空格分隔每個物件，並使用冒號和空格將鍵與值分開：
print('-------------分隔線------------')
#Use the parameter to change the default separator:separators
#使用該參數變更預設分隔符：separators
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
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
#Related Pages 相關頁面
#Python JSON Tutorial
#https://www.w3schools.com/python/python_json.asp
#JSON
#https://www.w3schools.com/python/gloss_python_json.asp
#Parse JSON 解析 JSON
#https://www.w3schools.com/python/gloss_python_json_parse.asp
#Convert into JSON 轉換為 JSON
#https://www.w3schools.com/python/gloss_python_convert_into_JSON.asp
#Sort JSON 排序 JSON
#https://www.w3schools.com/python/gloss_python_json_sort.asp