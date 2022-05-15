#https://www.w3schools.com/python/ref_requests_response.asp
#Python requests.Response Object 請求。回應物件
#Make a request to a web page, and return the status code:
#向網頁發出請求，並返回狀態代碼：
import requests
x = requests.get('https://w3schools.com')
print(x.status_code)
#Definition and Usage 定義和用法
#The requests.Response() Object contains the server's response to the HTTP request.
#物件包含伺服器對 HTTP 請求的回應。requests.Response()
#Properties and Methods 屬性和方法
#Property/Method：Description
#json()：Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
#返回結果的 JSON 物件（如果結果是以 JSON 格式編寫的，如果不是，則引發錯誤）
import requests
url = 'https://www.w3schools.com/python/demopage.js'
x = requests.get(url)
print(x.json())