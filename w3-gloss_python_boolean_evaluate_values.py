#https://www.w3schools.com/python/gloss_python_evaluate_boolean_values.asp
#evaluate_boolean_values 評估布林斯值
#The function allows you to evaluate any value, and give you or in return,bool()TrueFalse
#該功能允許您評估任何價值，並給予您或作為回報，bool()TrueFalse
#Evaluate a string and a number:
#評估字串與數位：
print(bool("Hello"))
print(bool(15))
print('-------------分隔線------------')
#Evaluate two variables:
#評估兩個變數：
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
#Most Values are True
#大多數值都是真實的
#Almost any value is evaluated to if it has some sort of content.True
#幾乎任何值都被評估為是否有某種內容。True
#Any string is , except empty strings.True
#任何字串都是，除了空字串。True
#Any number is , except .True0
#任何號碼都是，除了.True0
#Any list, tuple, set, and dictionary are , except empty ones.True
#任何清單、圖、集和字典都是，空的除外。True
print('-------------分隔線------------')
#The following will return True:
#以下將返回 True：
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
#Some Values are False
#有些值是錯誤的
#In fact, there are not many values that evaluates to , except empty values, such as , , , , the number , and the value . And of course the value evaluates to .False()[]{}""0NoneFalseFalse
#事實上，除了空值（如"數位"和"值"）之外，評估到的值並不多。當然，價值評估。False()[]{}""0NoneFalseFalse
print('-------------分隔線------------')
#The following will return False:
#以下將傳回錯誤：
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print('-------------分隔線------------')
#One more value, or object in this case, evaluates to , and that is if you have an object that is made from a class with a function that returns or : False__len__0False
#在這種情況下，還有一個值或物件會評估到，即如果您有一個物件，該物件是由具有返回功能的類構成的，或者：False__len__0False
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
#Related Pages 相關頁面
#Python Booleans Tutorial Python 布爾斯教程
#https://www.w3schools.com/python/python_booleans.asp
#boolean_values 布爾斯值
#https://www.w3schools.com/python/gloss_python_boolean_values.asp
#Return Boolean Value 返回布爾值
#https://www.w3schools.com/python/gloss_python_return_boolean.asp