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
#reason：Returns a text corresponding to the status code
#返回與狀態代碼對應的文字
import requests
url = 'https://www.w3schools.com/python/demopage.htm'
x = requests.get(url)
print(x.reason)
#如果沒該網址,傳回Not Found