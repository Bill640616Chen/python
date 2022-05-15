#https://docs.python-requests.org/en/latest/api/#requests.patch
#Constructs and sends a Request.
#語法：requests.request(method, url, **kwargs)
import requests
x = requests.request('https://www.w3schools.com/python/demopage.php')
print(x)
'''
Parameters
1.method – method for the new Request object: , , , , , , or .GETOPTIONSHEADPOSTPUTPATCHDELETE
新要求物件的方法：、 、 、 、 或 。GET OPTION SHEAD POST PUT PATCH DELETE
2.url – URL for the new Request object.
新請求物件的 URL。
3.params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request.
（可選）字典，要在Request的查詢字串中發送的元組或位元組或位元組的清單。
4.data – (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
（可選）字典，要在請求正文中發送的元組，位元組或類似檔的物件的清單。
5.json – (optional) A JSON serializable Python object to send in the body of the Request.
（可選）要在請求正文中發送的 JSON 可序列化的 Python 物件。
6.headers – (optional) Dictionary of HTTP Headers to send with the Request.
（可選）要與請求一起發送的 HTTP 標頭字典。
7.cookies – (optional) Dict or CookieJar object to send with the Request.
（可選）Dict 或 CookieJar 物件，與請求一起發送。
8.files – (optional) Dictionary of (or ) for multipart encoding upload. can be a 2-tuple , 3-tuple or a 4-tuple , where is a string defining the content type of the given file and a dict-like object containing additional headers to add for the file.'name': file-like-objects{'name': file-tuple}file-tuple('filename', fileobj)('filename', fileobj, 'content_type')('filename', fileobj, 'content_type', custom_headers)'content-type'custom_headers
（選擇） 字典 （或 ）用於分段編碼上傳。 可以是 2 元組、3 元組或 4 元組，其中是定義給定檔內容類型的字串，以及包含要為檔添加的其他標頭的類似 dict 的物件。
9.auth – (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
（可選）Auth 元組，用於啟用 Basic/Digest/Custom HTTP Auth。
10.timeout (float or tuple) – (optional) How many seconds to wait for the server to send data before giving up, as a float, or a (connect timeout, read timeout) tuple.
（可選）在放棄之前等待伺服器發送數據的秒數，作為浮點數或（連接超時，讀取超時）元組。
11.allow_redirects (bool) – (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to .True
（可選） 布林值。啟用/禁用 GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD 重定向。缺省值為 。True
12.proxies – (optional) Dictionary mapping protocol to the URL of the proxy.
（可選）字典映射協定到代理的 URL。
13.verify – (optional) Either a boolean, in which case it controls whether we verify the server’s TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to .True
（可選）布爾值（在這種情況下，它控制我們是否驗證伺服器的 TLS 證書）或字串（在這種情況下，它必須是 CA 捆綁包的路徑才能使用）。缺省值為 。True
14.stream – (optional) if , the response content will be immediately downloaded.False
（可選）布爾值（在這種情況下，它控制我們是否驗證伺服器的 TLS 證書）或字串（在這種情況下，它必須是 CA 捆綁包的路徑才能使用）。缺省值為 。True
15.cert – (optional) if String, path to ssl client cert file (.pem). If Tuple, (‘cert’, ‘key’) pair.
（可選）如果為字串，則為ssl客戶端憑證檔 （.pem） 的路徑。如果元組，（"證書"，"金鑰"）對。
Returns
Response object

Return type
requests.Response
'''