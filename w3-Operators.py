#https://www.w3schools.com/python/python_operators.asp
#Python Operators
#Operators are used to perform operations on variables and values.
#操作員用於對變數和值執行操作。
#In the example below, we use the operator to add together two values:+
#In the example below, we use the operator to add together two values:+
print(10 + 5) #15
#Python divides the operators in the following groups:
#Python 將操作員分為以下組
#Arithmetic operators 算術操作員
#Assignment operators 分配操作員
#Comparison operators 比較操作員
#Logical operators    邏輯操作員
#Identity operators   身份操作員
#Membership operators 會員運營商
#Bitwise operators    按位元操作員

#Arithmetic Operators
#Arithmetic operators are used with numeric values to perform common mathematical operations:
#算術操作員使用數位值執行常見的數學操作：
#Operator(操作員)：Name(名稱)	Example(範例)	
#+：Addition	        x + y   加
#-：Subtraction	        x - y   滅
#*：Multiplication   	x * y   乘
#/：Division	        x / y   除
#%：Modulus	            x % y   取餘數
#**：Exponentiation	    x ** y  次方
#//：Floor division	    x // y  取商數

#Assignment Operators
#Operator	Example	    Same As	
#=	        x = 5	    x = 5	
x = 5
print(x) #5
#+=	        x += 3	    x = x + 3
x = 5
x += 3
print(x) #8
#-=	        x -= 3	    x = x - 3
x = 5
x -= 3
print(x) #2
#*=	        x *= 3	    x = x * 3
x = 5
x *= 3
print(x) #15
#/=	        x /= 3	    x = x / 3	
x = 5
x /= 3
print(x) #1.6666666666666667
#%=	        x %= 3	    x = x % 3
x = 5
x%=3
print(x) #2
#//=	        x //= 3 	x = x // 3
x = 5
x//=3
print(x) #1
#**=	        x **= 3	    x = x ** 3
x = 5
x **= 3
print(x) #125

#&=	        x &= 3	    x = x & 3
x = 5 #二位進101,若X=10,若X=15
x &= 3 #二進位11
print(x) #1,若X=10則為2,若X=15則為3
#&：AND,Sets each bit to 1 if both bits are 1
#兩邊輸出為1,結果才為1,否為則0
#若另一邊沒有,輸出為"空"
#101跟11兩邊輪出結果(以直列判斷)為1,二進位的1為十進位的1
#若X=10,則二進位為1010,與11的輸出結果為10,二進位的10為十進位的2
#若X=15,則二位進為1111,與11的輸出結果為11,二進位的11為十進位的3
#101    1010    1111
# 11      11      11
#----   ----    ----
#  1      10      11

#|=	        x |= 3	    x = x | 3	
#|：OR,Sets each bit to 1 if one of two bits is 1
#兩個其中一個輸入為1,輸出就是1
x = 5
x |= 3
print(x) #7,若X=10則為11,若X=15則為15
#兩邊只要一個位元為1,不管0或空,輸出都是1,所以5|3的二進位為111,十進位為7
#若X=10,則二進位為1010,與11的輸出結果為1011,二進位的1011為十進位的11
#若X=15,則二位進為1111,與11的輸出結果為1111,二進位的1111為十進位的15
#101    1010    1111
# 11      11      11
#----   ----    ----
#111    1011    1111

#^=	        x ^= 3  	x = x ^ 3	
#^：XOR,Sets each bit to 1 if only one of two bits is 1
#輸入前或後僅一方為1,輸出為1,只有一方的1可以輸出,對方為空,但相對位置為1
#也是輸出1,若兩方都為1,則輸出為0
x = 5
x ^= 3
print(x) #6,若X=10則為9,若X=15則為12
#若1對應0和空,則輸出1,若1對應1,則輸出0,故5^=3的二進位為110為十進位的6
#若X=10,則二進位為1010,與11的輸出結果為1001,二進位的1001為十進位的9
#若X=15,則二位進為1111,與11的輸出結果為1100,二進位的1111為十進位的12
#101    1010    1111
# 11      11      11
#----   ----    ----
#110    1001    1100

#>>=	        x >>= 3	    x = x >> 3	
#右移動運算子：把">>"左邊的運算數的各二進位全部右移若干位，
#>>右邊的數位指定了移動的位數
x = 5
x >>= 3
print(x) #0,若X=10則為1,若X=15則為1
#上面1對應下為空為1,上下兩邊輸出為1,則為1
#若下面空,輸出為"空",若上下各對應為空,輸出結果為空
#若兩邊對應為空,輸出結果為空5>>=3,其值為0
#若X=10,移三位後,1對1為1,則二進位的1,十進位為1
#若X=15,移三位後,1對1為1,則二進位的1,十進位為1
#   101    1010    1111
# 11      11      11
#----   ----    ----
#          1       1
#測試上面的移動位數的值
x = 5
x >>= 1
print(x) #2,若X=10則為5,若X=15則為7
#上面1對應下面空則為1,上下都是1,則為1
#上面0對應下面1,則為0,若上面1對應下面0,則為1
#若另一邊沒有,輸出為"空",若兩邊對應為空,輸出結果為空
#5>>=1,二進位10為十進位2
#10>>=1,二進位10為十進位5
#15>>=1,二進位10為十進位7
# 101    1010    1111 
# 11      11      11  
#----   ----    ----  
# 10     101     111  

#<<=	        x <<= 3	    x = x << 3
#左移動運算符：運算數的各二進位全部左移若干位，
#由<<右邊的數位指定了移動的位數，高位丟棄(對應是空的)，低位補0。
x = 5
x <<= 3
print(x) #40,
#這裡的高位是指<<= 3,低位是指x = 5,這樣結果才對的上
#上面是低位,下面是高位
#5<<=3,二進位101000為十進位40
#10<<=3,二進位1010000為十進位80
#15<<=3,二進位1111000為十進位120
# 101       1010       1111
#     11         11         11
#-------    -------    ----
# 101000    1010000    1111000