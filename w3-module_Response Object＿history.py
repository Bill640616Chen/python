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
#history：Returns a list of response objects holding the history of request (url)
#傳回儲存要求歷史記錄的回應物件清單 （url）
import requests
url = 'https://www.w3schools.com/python/demopage.htm'
x = requests.get(url)
print(x.history)
