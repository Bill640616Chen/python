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
#apparent_encoding：Returns the apparent encoding
#返回明顯的編碼
#close()：Closes the connection to the server
#關閉與伺服器的連接
#content：Returns the content of the response, in bytes
#返回回應的內容（以位元組為單位）
#cookies：Returns a CookieJar object with the cookies sent back from the server
#返回一個 CookieJar 物件，其中包含從伺服器發回的 Cookie
#elapsed：Returns a timedelta object with the time elapsed from sending the request to the arrival of the response
#返回一個 timedelta 物件，其中包含從發送請求到到達回應所經過的時間
#encoding：Returns the encoding used to decode r.text
#返回用於解碼 r.text 的編碼
#headers：Returns a dictionary of response headers
#返回回應標頭的字典
#history：Returns a list of response objects holding the history of request (url)
#傳回儲存要求歷史記錄的回應物件清單 （url）
#is_permanent_redirect：Returns True if the response is the permanent redirected url, otherwise False
#如果回應是永久重定向的 url，則返回 True，否則為 False
#is_redirect：Returns True if the response was redirected, otherwise False
#如果回應已重定向，則返回 True，否則為 False
#iter_content()：Iterates over the response
#迴圈訪問回應
#iter_lines()：Iterates over the lines of the response
#反覆運算回應的行
#json()：Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
#返回結果的 JSON 物件（如果結果是以 JSON 格式編寫的，如果不是，則引發錯誤）
#links：Returns the header links
#返回標頭連結
#next：Returns a PreparedRequest object for the next request in a redirection
#為重定向中的下一個請求返回 PreparedRequest 物件
#ok：Returns True if status_code is less than 400, otherwise False
#如果 status_code 小於 400，則返回 True，否則返回 False
#raise_for_status()：If an error occur, this method returns a HTTPError object
#如果發生錯誤，此方法將返回 HTTPError 物件
#reason：Returns a text corresponding to the status code
#返回與狀態代碼對應的文字
#request：Returns the request object that requested this response
#返回請求此回應的請求物件
#status_code：Returns a number that indicates the status (200 is OK, 404 is Not Found)
#返回一個指示狀態的數位（200 表示正常，404 表示未找到）
#text：Returns the content of the response, in unicode
#以 unicode 格式返回回應的內容
#url：Returns the URL of the response
#返回回應的 URL
