#https://www.w3schools.com/python/module_requests.asp
#Python Requests Module 請求模組
#Make a request to a web page, and print the response text:
#向網頁發出請求，並列印回應文本：
import requests
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)
#Definition and Usage 定義和用法
#The module allows you to send HTTP requests using Python.requests
#該模組允許您使用Python發送HTTP請求。requests
#The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
#HTTP 請求返回一個回應物件，其中包含所有響應數據（內容、編碼、狀態等）。
#Download and Install the Requests Module 下載並安裝請求模組
#Navigate your command line to the location of PIP, and type the following:
#將命令行導航到 PIP 的位置，然後鍵入以下內容：
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install requests
#Syntax 語法
#requests.methodname(params)
#Methods 方法
#Method：Description
#delete(url, args)：Sends a DELETE request to the specified url
#向指定的 URL 發送 DELETE 請求。
#get(url, params, args)：Sends a GET request to the specified url
#向指定的 URL 發送 GET 請求。
#head(url, args)：Sends a HEAD request to the specified url
#向指定的 URL 發送 HEAD 請求。
#patch(url, data, args)：Sends a PATCH request to the specified url
#向指定的 URL 發送 PATCH 請求。
#post(url, data, json, args)：Sends a POST request to the specified url
#向指定的 URL 發送 POST 請求。
#put(url, data, args)：Sends a PUT request to the specified url
#向指定的 URL 發送 PUT 請求。
#request(method, url, args)：Sends a request of the specified method to the specified url
#將指定方法的請求發送到指定的 URL。