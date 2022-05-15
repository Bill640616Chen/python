#https://www.w3schools.com/python/ref_requests_head.asp
#Python Requests head() Method
#Make a HEAD request to a web page, and return the HTTP headers:
#向網頁發出 HEAD 請求，並返回 HTTP 標頭：
import requests
x = requests.head('https://www.w3schools.com/python/demopage.php')
print(x.headers)
#Definition and Usage 定義和用法
#The head() method sends a HEAD request to the specified url.
#該方法將 HEAD 請求發送到指定的 url。head()
#HEAD requests are done when you do not need the content of the file, but only the status_code or HTTP headers.
#當您不需要文件的內容，而只需要status_code或 HTTP 標頭時，將完成 HEAD 請求。
#Syntax 語法
#requests.head(url, args)
#args means zero or more of the named arguments in the parameter table below. Example:
#args表示以下參數表中的零個或多個命名參數。例：
#requests.head(url, timeout=2.50)
#Parameter Values
#Parameter：Description
print('-------------分隔線------------')
#url：Required. The url of the request
#必填。請求的網址
import requests
#the required first parameter of the 'head' method is the 'url':
x = requests.head('https://www.w3schools.com/python/demopage.php')
#print the response headers (the HTTP headers of the requested file):
print(x.headers)
print('-------------分隔線url------------')
#allow_redirects	
#Optional. A Boolean to enable/disable redirection.
#Default：False (not allowing redirects)
#自選。用於啟用/禁用重定向的布爾值。
#預設值：False（不允許重定向）
import requests
url = 'https://w3schools.com/python/demopage.php'
x = requests.head(url, allow_redirects=True)
#The server will redirect this url to 'https://w3schools.com/python/demopage.php'
#and since the head method by default do not allow redirects, we must use allow_redirects=True.
print(x.status_code)
import requests
url = 'https://w3schools.com/python/demopage.php'
x = requests.head(url)
#Since the server will redirect this url to 'https://w3schools.com/python/demopage.php'
#AND the head method by default do not allow redirects, we will get an 301 status code.
print(x.status_code) #禁止轉向,所以是301
print('-------------分隔線allow_redirects------------')
#auth：Optional. A tuple to enable a certain HTTP authentication.
#Default：None
#身份驗證：可選。用於啟用特定 HTTP 身份驗證的元件。
#默認值：無
import requests
url = 'https://www.w3schools.com/python/demopage.php'
#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.head(url, auth = ('user', 'pass'))
print(x.status_code)
print('-------------分隔線auth------------')
#cert：Optional. A String or Tuple specifying a cert file or key.
#Default：None
#證書：可選。指定證書檔或金鑰的字串或元組。
#默認值：無
import requests
try:
    url = 'https://www.w3schools.com/python/demopage.htm'
    #specify a cert to use as a client side certificate by setting the 'cert' parameter:
    x = requests.head(url, cert='folder/myclient.cert')
    print(x.status_code)
    raise Exception('Error')
except Exception as e:
    print(e)
print('-------------分隔線cert------------')
#cookies：Optional. A dictionary of cookies to send to the specified url.
#Default：None
#餅乾：可選。要發送到指定 url 的 Cookie 字典。
#默認值：無
import requests
url = 'https://www.w3schools.com/python/demopage.php'
#use the 'cookies' parameter to send cookies to the server:
x = requests.head(url, cookies = {"favcolor": "Red"})
print(x.status_code)
print('-------------分隔線cookies------------')
#headers：Optional. A dictionary of HTTP headers to send to the specified url.
#Default：None
#標頭：可選。要發送到指定 url 的 HTTP 標頭的字典。
#默認值：無
import requests
url = 'https://www.w3schools.com/python/demopage.asp'
#use the 'headers' parameter to set the HTTP headers:
x = requests.head(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
print(x.status_code)
print('-------------分隔線headers------------')
#proxies：Optional. A dictionary of the protocol to the proxy url.
#Default：None
#代理：可選。代理url的協定的字典。
#默認值：無
import requests
try:
    url = 'https://www.w3schools.com/python/demopage.php'
    #find a free proxy address and send your request via that proxy:
    x = requests.head(url, proxies = { "https" : "https://1.1.0.1:80"})
    print(x.status_code)
    raise Exception('Error')
except Exception as e:
    print(e)
print('-------------分隔線proxies------------')
#stream：Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
#Default：False
#流：可選。布爾指示是否應立即下載回應（False）或流式傳輸（True）。
#默認值：假
import requests
url = 'https://www.w3schools.com/images/pulpit.jpg'
#allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.head(url, stream=True)
print(x.status_code)
print('-------------分隔線stream------------')
#timeout：Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
#Default：None which means the request will continue until the connection is closed
#超時：可選。一個數位或元組，指示等待用戶端建立連接和/或發送回應的秒數。
#默認值：無，這意味著請求將繼續，直到連接關閉
import requests
try:
    url = 'https://w3schools.com/python/demopage.php'
    #to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
    x = requests.head(url, timeout=0.001)
    print(x.status_code)
    raise Exception('Error')
except Exception as e:
    print(e)
print('-------------分隔線timeout------------')
#verify：Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
#Default：True
#驗證：可選。用於驗證伺服器 TLS 證書與否的布爾值或字串指示。
#默認值：真
import requests
url = 'https://www.w3schools.com/python/demopage.php'
#make the request with the path to a TLS certificate:
x = requests.head(url, verify=False)
print(x.status_code)
print('-------------分隔線verify------------')
#Return Value
#The head() method returns a requests.Response object.

