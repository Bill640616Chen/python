#https://www.w3schools.com/python/ref_requests_post.asp
#Python Requests post() Method 建立新記錄 = >POST
#Make a POST request to a web page, and return the response text:
#向網頁發出 POST 請求，並返回回應文本：
import requests
url = 'https://w3schools.com/python/demopage.htm'
myobj = {'somekey': 'somevalue'}
x = requests.post(url, data = myobj)
print(x.text)
#Definition and Usage 定義和用法
#The post() method sends a POST request to the specified url.
#該方法將POST請求發送到指定的url。post()
#The post() method is used when you want to send some data to the server.
#當您要向伺服器發送一些數據時，將使用此方法。post()
#Syntax 語法
#requests.post(url, data={key: value}, json={key: value}, args)
#args means zero or more of the named arguments in the parameter table below. Example:
#args表示以下參數表中的零個或多個命名參數。例：
#requests.post(url, data = myobj, timeout=2.50)
#Parameter Values 參數值
#Parameter：Description
print('-------------分隔線------------')
#url：Required. The url of the request
#必填。請求的網址
import requests
url = 'https://w3schools.com/python/demopage.htm'
x = requests.post(url)
#print the response text (the content of the requested file):
print(x.text)
print('-------------分隔線url------------')
#data：Optional. A dictionary, list of tuples, bytes or a file object to send to the specified url
#自選。要發送到指定 url 的字典、元組清單、位元組或檔案物件
import requests
url = 'https://w3schools.com/python/demopage.htm'
myobj = {'somekey': 'somevalue'}
x = requests.post(url, data = myobj)
#print the response text (the content of the requested file):
print(x.text)
print('-------------分隔線data------------')
#json：Optional. A JSON object to send to the specified url
#自選。要發送到指定網址的 JSON 物件
import requests
url = 'https://w3schools.com/python/demopage.htm'
myjson = {'somekey': 'somevalue'}
x = requests.post(url, json = myjson)
#print the response text (the content of the requested file):
print(x.text)
print('-------------分隔線json------------')
#files：Optional. A dictionary of files to send to the specified url
#自選。要發送到指定 url 的檔案字典
import requests
try:
    url = 'https://w3schools.com/python/demopage.htm'
    myfiles = {'file': open('myfirstreact.png' ,'rb')}
    x = requests.post(url, files = myfiles)
    raise Exception ('Error')
except Exception as e:
    print(e)
#print the response text (the content of the requested file):
print(x.text)
print('-------------分隔線files------------')
#allow_redirects：Optional. A Boolean to enable/disable redirection.
#Default：True (allowing redirects)
#自選。用於啟用/禁用重定向的布爾值。
#True（允許重定向）。
import requests
#to demonstrate the 'allow_redirects' parameter we use 'http' instead of 'https', w3schools.com automatically redirects http requests to https:
url = 'http://w3schools.com/python/demopage.htm'
myobj = {'somekey': 'somevalue'}
#first, make a request without setting the 'allow_redirects' parameter to False:
x = requests.post(url, data = myobj)
print(x.text)
print("----------------")
#then, make a request with the 'allow_redirects' parameter set to False:
x = requests.post(url, data = myobj, allow_redirects=False)
print(x.text)
print('-------------分隔線allow_redirects------------')
#auth：Optional. A tuple to enable a certain HTTP authentication.
#Default：None
#自選。用於啟用特定 HTTP 身份驗證的元件。
#默認值：無
import requests
url = 'http://w3schools.com/python/demopage.htm'
myobj = {'somekey': 'somevalue'}
#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.post(url, data = myobj, auth = ('user', 'pass'))
print(x.status_code)
print('-------------分隔線auth------------')
#cert：Optional. A String or Tuple specifying a cert file or key.
#Default：None
#指定證書檔或金鑰的字串或元組。
#默認值：無
import requests
try:
    url = 'http://w3schools.com/python/demopage.htm'
    myobj = {'somekey': 'somevalue'}
    #specify a cert to use as a client side certificate by setting the 'cert' parameter:
    x = requests.post(url, data = myobj, cert='folder/myclient.cert')
    raise Exception('Error')
except Exception as e:
    print(e)
print(x.status_code)
print('-------------分隔線cert------------')
#cookies：Optional. A dictionary of cookies to send to the specified url.
#Default：None
#自選。要發送到指定 url 的 Cookie 字典。
#默認值：無
import requests
url = 'http://w3schools.com/python/demopage.htm'
myobj = {'somekey': 'somevalue'}
#use the 'cookies' parameter to send cookies to the server:
x = requests.post(url, data = myobj, cookies = {"favcolor": "Red"})
print(x.text)
#the 'demopage2.php' prints the value of the 'favcolor' cookie.
print('-------------分隔線cookies------------')
#headers：Optional. A dictionary of HTTP headers to send to the specified url.
#Default：None
#可選。要發送到指定 url 的 HTTP 標頭的字典。
#默認值：無
import requests
url = 'http://w3schools.com/python/demopage.htm'
myobj = {'somekey': 'somevalue'}
#use the 'headers' parameter to set the HTTP headers:
x = requests.post(url, data = myobj, headers = {"HTTP_HOST": "MyVeryOwnHost"})
print(x.text)
#the 'demopage.asp' prints all HTTP Headers
print('-------------分隔線headers------------')
#proxies：Optional. A dictionary of the protocol to the proxy url.
#Default：None
#自選。代理url的協定的字典。
#默認值：無
import requests
try:
    url = 'http://w3schools.com/python/demopage.htm'
    myobj = {'somekey': 'somevalue'}
    #find a free proxy address and send your request via that proxy:
    x = requests.post(url, data = myobj, proxies = { "https" : "https://1.1.0.1:80"})
    #'demopage.php' will print the ip address of the proxy instead of your ip:
    raise Exception ('Error')
except Exception as e:
    print(e)
print(x.text)
print('-------------分隔線proxies------------')
#stream：Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
#Default：False
#自選。布爾指示是否應立即下載回應（False）或流式傳輸（True）。
#默認值：假
import requests
url = 'http://w3schools.com/python/demopage.htm'
myobj = {'somekey': 'somevalue'}
#allow the response to be streamed by setting the 'stream' parameter to True:
x = requests.post(url, data = myobj, stream=True)
print(x.status_code)
print('-------------分隔線stream------------')
#timeout：Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
#Default：None which means the request will continue until the connection is closed
#自選。一個數位或元組，指示等待用戶端建立連接和/或發送回應的秒數。
#默認值無，這意味著請求將繼續，直到連接關閉
import requests
try:
    url = 'http://w3schools.com/python/demopage.htm'
    myobj = {'somekey': 'somevalue'}
    #to demonstrate the 'timeout' parameter, we set the timeout to 0.001 to guarantee that the connection will be timed out:
    x = requests.post(url, data = myobj, timeout=0.001)
    print(x.text)
    raise Exception('Error')
except Exception as e:
    print(e)
print('-------------分隔線timeout------------')
#verify：Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
#Default：True
#自選。用於驗證伺服器 TLS 證書與否的布爾值或字串指示。
#默認值：真
import requests
try:
    url = 'http://w3schools.com/python/demopage.htm'
    myobj = {'somekey': 'somevalue'}
    #make the request with the path to a TLS certificate:
    x = requests.post(url, data = myobj, verify='folder/tlscertificate')
    print(x.status_code)
    raise Exception('Error')
except Exception as e:
    print(e)
print('-------------分隔線verify------------')
import requests
url = 'http://w3schools.com/python/demopage.htm'
myobj = {'somekey': 'somevalue'}
#make the request and specify that there will be no verifying:
x = requests.post(url, data = myobj, verify=False)
print(x.status_code)
#Return Value
#A requests.Response object.
#https://www.w3schools.com/python/ref_requests_response.asp
