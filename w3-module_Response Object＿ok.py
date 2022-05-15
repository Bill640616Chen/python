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
#ok：Returns True if status_code is less than 400, otherwise False
#如果 status_code 小於 400，則返回 True，否則返回 False
import requests
url = 'https://www.w3schools.com/python/demopage.htm'
x = requests.get(url)
print(x.ok)
