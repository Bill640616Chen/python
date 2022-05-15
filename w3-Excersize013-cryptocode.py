#使用 cryptocode 庫在 Python 中加密字串
#術語 cryptocode 是一個簡單的庫，它允許我們在 Python 3 或更高版本中
#安全且簡單地加密和解密字串。記住這個庫需要手動安裝；可以使用 pip 命令來完成。
#下面的程式使用 cryptocode 庫來加密 Python 中的字串：
print('---------------cryptocode---------------')
import cryptocode
str_encoded = cryptocode.encrypt("I am okay","wow")
## And then to decode it:
str_decoded = cryptocode.decrypt(str_encoded, "wow")
print(str_decoded)
#函式中的第一個引數是需要加密的字串。第二個引數需要是金鑰，用於解密目的。
#使用 Cryptography 包在 Python 中加密字串

#Cryptography 是一個 Python 包，可用於實現對稱金鑰加密。對稱金鑰加密是我們
#在編碼和解碼過程中使用相同金鑰的一種方式。
#需要安裝 Cryptography 庫才能使用此方法進行加密；這可以通過使用 pip 命令來完成。
#以下程式碼使用 cryptography 包函式在 Python 中加密字串：
print('---------------cryptography---------------')
from cryptography.fernet import Fernet
str1 = "*CDC is the trademark of the Control Data Corporation."
key = Fernet.generate_key()
fernet = Fernet(key)
enctex = fernet.encrypt(str1.encode())
dectex = fernet.decrypt(enctex).decode()
print("The primordial string: ", str1)
print("The Encrypted message: ", enctex)
print("The Decrypted message: ", dectex)
#在上面的程式碼中，我們從 cryptography.fernet 模組中匯入了 Fernet。然後，
# 我們生成將用於編碼和解碼目的的加密金鑰。Fernet 類使用加密金鑰進行例項化。
# 然後使用 Fernet 例項對字串進行加密。最後，用 Fernet 類例項解密。
#對稱金鑰加密是加密字串的一種輕鬆方式。唯一的缺點是它的安全性相對較低。任何
# 擁有金鑰的人都可以閱讀加密文字。