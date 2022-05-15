#https://docs.python-requests.org/en/latest/api/#requests.patch
#Sends a PUT request. 如果該記錄存在，則更新，否則將創建新記錄 = >PUT
#語法：requests.put(url, data=None, **kwargs)
import requests
x = requests.put('https://www.w3schools.com/python/demopage.php')
print(x)
'''
Parameters
1.url – URL for the new Request object.
新請求物件的 URL。
2.data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
（可選）要在請求正文中發送的字典、元組列表、字節或類似文件的對象。
3.json – (optional) json data to send in the body of the Request.
（可選）要在請求正文中發送的 json 數據。
4.**kwargs – Optional arguments that request takes.
request 需要的可選參數。

Returns
Response object

Return type
requests.Response
'''