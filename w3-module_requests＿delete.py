#Phttps://www.w3schools.com/python/ref_requests_delete.asp
#Python Requests delete() Method
#Make a DELETE request to a web page, and return the response text:
#向網頁發出 DELETE 請求，並返回回應文本：
import requests
x = requests.delete('https://w3schools.com/python/demopage.php')
print(x.text)
#Definition and Usage 定義和用法
#The delete() method sends a DELETE request to the specified url.
#該方法將 DELETE 請求發送到指定的 URL。delete()
#DELETE requests are made for deleting the specified resource (file, record etc).
#發出刪除請求以刪除指定的資源（文件、記錄等）。
#Syntax 語法
#requests.delete(url, args)
#args means zero or more of the named arguments in the parameter table below. Example:
#args表示以下參數表中的零個或多個命名參數。例：
#requests.delete(url, timeout=2.50)
#Parameter Values 參數值
#Parameter：Description
print('-------------分隔線------------')
#url：Required. The url of the request 必填。請求的網址
import requests
#the required first parameter of the 'delete' method is the 'url':
x = requests.delete('https://w3schools.com/python/demopage.php')
#print the response text (the content of the requested file):
print(x.text)
print('-------------分隔線------------')
#allow_redirects：Optional. A Boolean to enable/disable redirection.
#自選。用於啟用/禁用重定向的布爾值。
#Default True (allowing redirects)
#預設值為 True（允許重定向）
import requests
url = 'https://w3schools.com/python/demopage.php'
#Sometimes the server redirects a request, could be if the file does not exist etc., set the 'allow_redirects' parameter to False to deny redirects:
x = requests.delete(url, allow_redirects=False)
#print the response text (the content of the requested file):
print(x.text)
print('-------------分隔線------------')
#auth：Optional. A tuple to enable a certain HTTP authentication.
#自選。用於啟用特定 HTTP 身份驗證的元件。
#Default None
#默認無
import requests
url = 'https://w3schools.com/python/demopage.php'
#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.delete(url, auth = ('user', 'pass'))
print(x.status_code)
print('-------------分隔線------------')
#cert：Optional. A String or Tuple specifying a cert file or key.
#可選。指定證書檔或金鑰的字串或元組。
#Default None
#默認無
'''
import requests
url = 'https://w3schools.com/python/demopage.htm'
#specify a cert to use as a client side certificate by setting the 'cert' parameter:
x = requests.delete(url, cert='folder/myclient.cert')
print(x.status_code)
'''
print('-------------分隔線------------')
#cookies：Optional. A dictionary of cookies to send to the specified url.
#可選。要發送到指定 url 的 Cookie 字典。
#Default None
#默認無
import requests
url = 'https://w3schools.com/python/demopage2.php'
#use the 'cookies' parameter to send cookies to the server:
x = requests.delete(url, cookies = {"favcolor": "Red"})
print(x.status_code)
print('-------------分隔線------------')
#headers：Optional. A dictionary of HTTP headers to send to the specified url.
#可選。要發送到指定 url 的 HTTP 標頭的字典。
#Default None
#默認無
import requests
url = 'https://w3schools.com/python/demopage.asp'
#use the 'headers' parameter to set the HTTP headers:
x = requests.delete(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
print(x.status_code)
print('-------------分隔線------------')
#proxies：Optional. A dictionary of the protocol to the proxy url.
#可選。代理url的協定的字典。
#Default None
#默認無
'''
import requests
url = 'https://w3schools.com/python/demopage.php'
#find a free proxy address and send your request via that proxy:
x = requests.delete(url, proxies = { "https" : "https://1.1.0.1:80"})
print(x.status_code)
連線嘗試失敗，因為連線對象有一段時間並未正確回應，或是連線建立失敗
，因為連線的主機無法回應。
'''
print('-------------分隔線------------')
#stream：Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
#可選。布爾指示是否應立即下載回應（False）或流式傳輸（True）。
#Default False
#默認錯誤
import requests
url = 'https://w3schools.com/images/pulpit.jpg'
#allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.delete(url, stream=True)
print(x.status_code)
print('-------------分隔線------------')
#timeout	：Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
#自選。一個數位或元組，指示等待用戶端建立連接和/或發送回應的秒數。
#Default None which means the request will continue until the connection is closed
#默認值"無"，這意味著請求將繼續，直到連接關閉
'''
import requests
url = 'https://w3schools.com/python/demopage.php'
#to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
x = requests.delete(url, timeout=0.001)
print(x.text)
'''
print('-------------分隔線------------')
#verify：Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
#自選。用於驗證伺服器 TLS 證書與否的布爾值或字串指示。
#Default True
#預設值為 True
'''
import requests
url = 'https://w3schools.com/python/demopage.php'
#make the request with the path to a TLS certificate:
x = requests.delete(url, verify='folder/tlscertificate')
print(x.status_code)
OSError: Could not find a suitable TLS CA certificate bundle, invalid path: folder/tlscertificate
'''
print('-------------分隔線------------')
import requests
url = 'https://w3schools.com/python/demopage.php'
#make the request and specify that there will be no verifying:
x = requests.delete(url, verify=False)
print(x.status_code)
#Return Value 返回值
#The delete() method returns a requests.Response object.
#delete（） 方法返回一個請求。回應物件。
#https://www.w3schools.com/python/ref_requests_response.asp


