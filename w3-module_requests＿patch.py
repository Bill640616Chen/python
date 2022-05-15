#https://docs.python-requests.org/en/latest/api/#requests.patch
#Sends a PATCH request. 更新/修改 = >PATCH
#語法：requests.patch(url, data=None, **kwargs)
import requests
x = requests.patch('https://www.w3schools.com/python/demopage.php')
print(x)
'''
Parameters
1.url – URL for the new Request object.
新請求物件的 URL。
2.data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
（自選）字典，要在請求正文中發送的元組、位元組或類似檔的物件的清單。
3.json – (optional) json data to send in the body of the Request.
（可選）要在請求正文中發送的 json 資料。
4.**kwargs – Optional arguments that request takes.
請求採用的可選參數。
Returns
Response object

Return type
requests.Response
'''