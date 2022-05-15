#https://www.w3schools.com/python/ref_requests_get.asp
#Python Requests get() Method 讀取 = >GET
#Make a request to a web page, and return the status code:
#向網頁發出請求，並返回狀態代碼：
import requests
x = requests.get('https://w3schools.com')
print(x.status_code)
#Definition and Usage 定義和用法
#The method sends a GET request to the specified url.get()
#該方法將 GET 請求發送到指定的 url。get()
#Syntax 語法
#requests.get(url, params={key: value}, args)
#args means zero or more of the named arguments in the parameter table below. Example:
#args表示以下參數表中的零個或多個命名參數。例：
#requests.get(url, timeout=2.50)
#Parameter Values 參數值
#Parameter：Description
#url：Required. The url of the request
#必填。請求的網址
import requests
#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://w3schools.com/python/demopage.htm')
#print the response text (the content of the requested file):
print(x.text)
print('-------------分隔線url------------')
#params：Optional. A dictionary, list of tuples or bytes to send as a query string.
#Defaul：one
#自選。字典，要作為查詢字串發送的元組或位元組的清單。
#默認無
import requests
url = 'https://w3schools.com/python/demopage.php'
#demonstrate how to use the 'params' parameter:
x = requests.get(url, params = {"model": "Mustang"})
#print the response (the content of the requested file):
print(x.text)
#the file 'demopage.php' looks for a 'model' query string and prints its value.
print('-------------分隔線params------------')
#allow_redirects：Optional. A Boolean to enable/disable redirection.
#Default True (allowing redirects)
#自選。用於啟用/禁用重定向的布爾值。
#預設值為 True（允許重定向）
import requests
#to demonstrate the 'allow_redirects' parameter we use 'http' instead of 'https', w3schools.com automatically redirects http requests to https:
url = 'http://w3schools.com/python/demopage.htm'
#first, make a request without setting the 'allow_redirects' parameter to False:
x = requests.get(url)
print(x.text)
print("----------------")
#then, make a request with the 'allow_redirects' parameter set to False:
x = requests.get(url, allow_redirects=False)
print(x.text)
print('-------------分隔線allow_redirects------------')
#auth：Optional. A tuple to enable a certain HTTP authentication.
#Defaul：None
#自選。用於啟用特定 HTTP 身份驗證的元件。
#默認無
import requests
url = 'https://w3schools.com/python/demopage.php'
#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.get(url, auth = ('user', 'pass'))
print(x.status_code)
print('-------------分隔線auth------------')
#cert：Optional. A String or Tuple specifying a cert file or key.
#Defaul：None
#自選。指定證書檔或金鑰的字串或元組。
#默認無
import requests
try:
    url = 'https://w3schools.com/python/demopage.htm'
    #specify a cert to use as a client side certificate by setting the 'cert' parameter:
    x = requests.get(url, cert='folder/myclient.cert')
    print(x.status_code)
    raise Exception('OSError: Could not find the TLS certificate file, invalid path: folder/myclient.cert')
except Exception as e:
    print(e)
print('-------------分隔線cert------------')
#cookies：Optional. A dictionary of cookies to send to the specified url.
#Defaul：None
#自選。要發送到指定 url 的 Cookie 字典。
#默認無
import requests
url = 'https://w3schools.com/python/demopage2.php'
#use the 'cookies' parameter to send cookies to the server:
x = requests.get(url, cookies = {"favcolor": "Red"})
print(x.text)
#the 'demopage2.php' prints the value of the 'favcolor' cookie.
print('-------------分隔線cookies------------')
#headers：Optional. A dictionary of HTTP headers to send to the specified url.
#Defaul：None
#自選。要發送到指定 url 的 HTTP 標頭的字典。
#默認無
import requests
url = 'https://w3schools.com/python/demopage.asp'
#use the 'headers' parameter to set the HTTP headers:
x = requests.get(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
print(x.text)
#import os
#os.system("pause")
#請按任意鍵繼續 . . .
#quit(),exit(),os.abort()中斷code
#the 'demopage.asp' prints all HTTP Headers
print('-------------分隔線headers------------')
#proxies：Optional. A dictionary of the protocol to the proxy url.
#Defaul：None
#自選。代理url的協定的字典。
#默認無
import requests
try:
    url = 'https://w3schools.com/python/demopage.php'
    #find a free proxy address and send your request via that proxy:
    x = requests.get(url, proxies = { "https" : "https://1.1.0.1:80"})
    #'demopage.php' will print the ip address of the proxy instead of your ip:
    print(x.text)
    raise Exception('連線嘗試失敗，因為連線對象有一段時間並未正確回應，或是連線建立失敗，因為連線的主機無法回應。')
except Exception as e:
    print(e)
print('-------------分隔線proxies------------')
#stream：Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
#Default：False
#自選。布爾指示是否應立即下載回應（False）或流式傳輸（True）。
#默認錯誤
import requests
url = 'https://w3schools.com/images/pulpit.jpg'
#allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.get(url, stream=True)
print(x.status_code)
print('-------------分隔線stream------------')
#timeout：Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
#Defaul：one which means the request will continue until the connection is closed
#自選。一個數位或元組，指示等待用戶端建立連接和/或發送回應的秒數。
#默認值"無"，這意味著請求將繼續，直到連接關閉
import requests
try:
    url = 'https://w3schools.com/python/demopage.php'
    #to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
    x = requests.get(url, timeout=0.001)
    print(x.text)
    raise Exception('Read timed out')
except Exception as e:
    print(e)
print('-------------分隔線timeout------------')
#verify：Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
#Default：True
#自選。用於驗證伺服器 TLS 證書與否的布爾值或字串指示。
#預設值為 True
import requests
try:
    url = 'https://w3schools.com/python/demopage.php'
    #make the request with the path to a TLS certificate:
    x = requests.get(url, verify='folder/tlscertificate')
    print(x.status_code)
    raise Exception('OSError: Could not find a suitable TLS CA certificate bundle, invalid path: folder/tlscertificate')
except Exception as e:
    print(e)
print('-------------分隔線verify------------')
import requests
url = 'https://w3schools.com/python/demopage.php'
#make the request and specify that there will be no verifying:
x = requests.get(url, verify=False)
print(x.status_code)
#Return Value
#The get() method returns a requests.Response object.
#https://www.w3schools.com/python/ref_requests_response.asp
