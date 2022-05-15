#https://www.w3schools.com/python/python_strings_methods.asp
#Python format_map()
#Formats specified values in a string格式在字申裡指定值
#format_map()方法類似於str.format(** mapping)，
# 但str.format(** mapping)創建一個新字典，
# 而str.format_map(mapping)沒有。
#在談論之前format_map()。讓我們看看如何
# str.format(**mapping)適用於Python字典。
point = {'x':4,'y':-5}
print('{x} {y}'.format(**point))
#了解有關如何在Python中格式化字符串的更多信息？</p
#這個format_map(mapping)類似於str.format(**mapping)方法。
#唯一的區別是str.format(**mapping)複製dict然而
# str.format_map(mapping)在方法調用期間製作新字典。
# 如果您正在使用dict子類。
#的語法format_map()是
#str.format_map(mapping)

#format_map參數
#format_map()接受一個論點mapping(dictionary)。
#從format_map()返回值
#format_map()格式化給定的字符串並返回它。
#示例1：format_map()如何工作？
point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))
point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))

#示例2：format_map()如何與dict子類一起使用？
class Coordinate(dict):
    def __missing__(self, key):
      return key
print('({x}, {y})'.format_map(Coordinate(x='6')))
print('({x}, {y})'.format_map(Coordinate(y='5')))
print('({x}, {y})'.format_map(Coordinate(x='6', y='5')))
#2021/12/8完成筆記,原教程網址沒有
#https://vimsky.com/zh-tw/examples/usage/python-programming_methods_string_format_map.html