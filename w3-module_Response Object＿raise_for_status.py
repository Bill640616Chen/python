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
#raise_for_status()：If an error occur, this method returns a HTTPError object
#如果發生錯誤，此方法將返回 HTTPError 物件
import requests
#enter a wrong url:
url = 'https://www.w3schools.com/python/demopagdddddd.htm'
x = requests.get(url)
print(x.raise_for_status())
#如果沒錯誤，傳回None