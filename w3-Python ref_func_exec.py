#https://www.w3schools.com/python/ref_func_exec.asp
#Python exec Function Python exec函數
#Executes the specified code (or object)
#執行指定的代碼（或物件）。
#Execute a block of code:
#執行代碼塊：
x = 'name = "John"\nprint(name)'
exec(x)
#Definition and Usage 定義和用法
#The exec() function executes the specified Python code.
#exec（） 函數執行指定的 Python 代碼。
#The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression
#exec（） 函數接受大量代碼塊，這與 eval（） 函數僅接受單個運算式不同。
#Syntax 語法
#exec(object, globals, locals)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：A String, or a code object
#object：字串或代碼物件。
#globals：Optional. A dictionary containing global parameters
#globals：可選。 包含全域參數的字典。
#locals：Optional. A dictionary containing local parameters
#locals：可選。 包含局部參數的字典。