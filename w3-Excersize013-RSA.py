#使用 RSA 演算法在 Python 中加密字串
#Python 中的 RSA 演算法實現了非對稱金鑰加密。非對稱金鑰加密在加密
# 和解密過程中使用兩個不同的金鑰。

#這兩個金鑰是公鑰和私鑰。公鑰是公開的，用於加密過程。任何擁有公鑰的
#人都可以加密和傳送資料；只有接收者擁有私鑰。此外，有權訪問它的人也
#可以解密資料。

#需要先安裝 rsa 庫才能使用此方法。你可以使用一般的 pip 命令來安裝這個庫。

#以下程式碼使用 RSA 演算法在 Python 中加密字串：

import rsa
pubkey, privkey = rsa.newkeys(512)
#產生公鑰與私鑰
str1 = "I am okay"
enctex = rsa.encrypt(str1.encode(),pubkey)
dectex = rsa.decrypt(enctex, privkey).decode()
print("The primordial string: ", str1)
print("The Encrypted message: ", enctex)  #加密
print("The Decrypted message: ", dectex)  #解密

#在上面的程式碼中，匯入了 rsa 模組，並在 rsa.newkeys() 函式的幫助下生成
#了公鑰和私鑰。然後，使用 public key 對字串進行加密。然後可以僅使用私鑰
# 解密該字串。在這個程式的情況下，公鑰和私鑰分別是 pubkey 和 privkey。

#非對稱金鑰加密提供比對稱金鑰加密更好的安全性。與前者一樣，特定的私鑰只能由接收者訪問並用於解密目的。而後者中只有一個金鑰，這使得解密過程更容易，並且在傳送方和接收方中間受到第三方攻擊的安全性較低。