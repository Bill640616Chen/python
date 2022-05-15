#https://www.w3schools.com/python/python_mysql_where.asp
#Python MySQL Where 哪裡
#您可以使用逗號分離的一張或多張表，使用「哪裡」子句包含各種條件，但「哪裡」條款是 SELECT 命令的可選部分。
#您可以使用「哪裡」條款指定任何條件。
#您可以使用AND或OR操作員指定多個條件。
#其中條款可與刪除或更新 SQL 命令一起用於指定條件。
#Select With a Filter 選擇過濾器
#When selecting records from a table, you can filter the selection by using the "WHERE" statement:
#從表中選擇記錄時，您可以使用「哪裡」語句篩選選擇：
#Select record(s) where the address is "Park Lane 38": result:
#選擇位址為「公園巷 38」的記錄：結果：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
#cursor()游標只能用於儲存過程和函數,游標的使用，主要包括游標的宣告、開啟、使用和關閉
#宣告游標:游標只局限於儲存過程中，儲存過程處理完成後，游標就消失了
#開啟游標:要想從游標中提取資料，必須首先開啟游標
#使用游標:使用游標類似高階語言中的陣列遍歷，當第一次使用游標時，此時游標指向結果集的第一條記錄
#關閉游標:釋放游標使用的所有內部記憶體和資源，因此每個游標不再需要時都應該關閉
sql = "SELECT * FROM customers WHERE address ='Park Lane 38' OR (address='Highway 21')"
#SELECT * FROM customers,從customers選擇所有資料
#WHERE address ='Park Lane 38'由欄值查詢哪幾列的資料
#也可以查詢單筆資料
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#用for迴圈來顯示

print("------------------Wildcard Characters 通配符字元")
#Wildcard Characters 通配符字元
#You can also select the records that starts, includes, or ends with a given letter or phrase.
#您還可以選擇以給定字母或短語開頭、包含或結束的記錄。
#Use the %  to represent wildcard characters:
#使用％表示通配符字元：
#Select records where the address contains the word "way":
#選擇位址包含「方式」一詞的記錄：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
#%way%,字串中含有way的
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("-------------Prevent SQL Injection 防止 SQL 注入")
#Prevent SQL Injection 防止 SQL 注入
#也稱SQL隱碼或SQL注碼，是發生於應用程式與資料庫層的安全漏洞。
# 簡而言之，是在輸入的字串之中夾帶SQL指令，在設計不良的程式當
# 中忽略了字元檢查，那麼這些夾帶進去的惡意指令就會被資料庫伺
# 服器誤認為是正常的SQL指令而執行，因此遭到破壞或是入侵。[2]
#有部份人認為SQL注入是只針對Microsoft SQL Server，但只要是
# 支援處理SQL指令的資料庫伺服器，都有可能受到此種手法的攻擊。
#When query values are provided by the user, you should escape the values.
#當使用者提供查詢值時，您應該逃避這些值。
#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
#這是為了防止 SQL 注入，這是一種常見的網路駭客技術，以破壞或濫用您的資料庫。
#The mysql.connector module has methods to escape query values:
#mysql.connector 模組具有逃避查詢值的方法：
#Escape query values by using the placholder %s method:
#使用柏拉圖 %s 方法逃出查詢值：
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = %s "
#SELECT "欄位名" FROM "表格名" %s代表使用字串
#代表address欄的查詢只能用字串
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

print("-----測試只能使用%s,但是id裡面使用int不能防止SQL注入")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE id = %s "
#SELECT "欄位名" FROM "表格名" %s代表使用字串
#代表address欄的查詢只能用字串
id = (20,)
#把id=(int格式),沒被%s限制,依然沒出錯,一次只能一個查詢
mycursor.execute(sql,id)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#('Michael', 'Valley 345', 20)
#%(任何資料格式化)
#%d整型輸出，%ld長整型輸出，
#%o以八進位數形式輸出整數，
#%x以十六進位數形式輸出整數，
#%u以十進位數輸出unsigned型資料（無符號數）。
#%c用來輸出一個字元，
#%s用來輸出一個字串，
#%f用來輸出實數，以小數形式輸出，
#%e以指數形式輸出實數，
#%g根據大小自動選f格式或e格式，且不輸出無意義的零。