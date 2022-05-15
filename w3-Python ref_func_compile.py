#https://www.w3schools.com/python/ref_func_compile.asp
#Python compile() Function Python compile()函數
#Returns the specified source as an object, ready to be executed
#把指定的源作為物件返回，準備執行。
#Compile text as code, and the execute it:
#將文字編譯為代碼，然後執行：
x = compile('print(55)', 'test', 'eval')
exec(x)
#Definition and Usage 定義和用法
#The compile() function returns the specified source as a code object, ready to be executed.
#compile（） 函數將指定的原始程式碼物件返回，並準備執行。
#Syntax 語法
#compile(source, filename, mode, flag, dont_inherit, optimize)
#Parameter參數：Values值
#Parameter參數：Description描述
#source：Required. The source to compile, can be a String, a Bytes object, or an AST object
#source：必需。 要編譯的資源，可以是字串、位元組或 AST 物件。
#AST 的全文是 Abstract Syntax Tree，中文大多翻作抽象語法樹，主要是將我們 人類 所寫的程式語法，轉換成 程式比較容易閱讀的語法結構，並以樹的資料結構來儲存
#filename：Required. The name of the file that the source comes from. If the source does not come from a file, you can write whatever you like
#filename：必需。 源所來自的文件的名稱。 如果源不是來自檔，則可以編寫任何內容。
#mode：Required. Legal values:
#mode：必需。 合法值：
#eval - if the source is a single expression
#eval - 如果源是單個運算式
#exec - if the source is a block of statements
#exec - 如果源是語句塊
#single - if the source is a single interactive statement
#single - 如果源是單個互動式語句
#flags：Optional. How to compile the source. Default 0
#flags：可選。 如何對源進行編譯。 預設為 0。
#dont-inherit：Optional. How to compile the source. Default False
#dont-inherit：可選。 如何對源進行編譯。 默認為 False。
#optimize：Optional. Defines the optimization level of the compiler. Default -1
#optimize：可選。 定義編譯器的優化級別。 默認為 -1。
#Compile more than one statement, and the execute it:
#編譯一條以上的語句，並執行：
x = compile('print(55)\nprint(88)', 'test', 'exec')
exec(x)
#Related Pages
#The eval() Function
#The exec() Function

