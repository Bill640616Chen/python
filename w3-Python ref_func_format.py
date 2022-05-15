#https://www.w3schools.com/python/ref_func_format.asp
#Python format Function Python format函數
#Formats a specified value
#格式化指定值。
#Format the number 0.5 into a percentage value:
#把數位 0.5 格式化為百分比值：
x = format(0.5, '%')
print(x)
#Definition and Usage 定義和用法
#The format() function formats a specified value into a specified format.
#format（） 函數把指定值格式化為指定格式。
#Syntax 語法
#format(value, format)
#Parameter參數：Values值
#Parameter參數：Description描述
#value：A value of any format
#value：任何格式的值
#format：The format you want to format the value into.
#format：您要將值格式化為的格式。
#Legal values:合法值：
#'<' - Left aligns the result (within the available space)
#'<' - 左對齊結果（在可用空間內）
#'>' - Right aligns the result (within the available space)
#'>' - 右對齊結果（在可用空間內）
#'^' - Center aligns the result (within the available space)
#'^' - 居中對齊結果（在可用空間內）
#'=' - Places the sign to the left most position
#'=' - 將符號置於最左側
#'+' - Use a plus sign to indicate if the result is positive or negative
#'+' - 使用加號來指示結果是正還是負
#'-' - Use a minus sign for negative values only
#'-' - 負號僅用於負值
#' ' - Use a leading space for positive numbers
#' ' - 在正數前使用空白
#',' - Use a comma as a thousand separator
#',' - 使用逗號作為千位分隔符
#'_' - Use a underscore as a thousand separator
#'_' - 使用下劃線作為千位分隔符
#'b' - Binary format
#'b' - 二進位格式
#'c' - Converts the value into the corresponding unicode character
#'c' - 將值轉換為相應的 unicode 字元
#'d' - Decimal format
#'d' - 十進位格式
#'e' - Scientific format, with a lower case e
#'e' - 科學格式，使用小寫字母 e
#'E' - Scientific format, with an upper case E
#'E' - 科學格式，使用大寫字母 E
#'f' - Fix point number format
#'f' - 定點編號格式
#'F' - Fix point number format, upper case
#'F' - 定點編號格式，大寫
#'g' - General format
#'g' - 通用格式
#'G' - General format (using a upper case E for scientific notations)
#'G' - 通用格式（將大寫 E 用作科學計數法）
#'o' - Octal format
#'o' - 八進位格式
#'x' - Hex format, lower case
#'x' - 十六進位格式，小寫
#'X' - Hex format, upper case
#'X' - 十六進位格式，大寫
#'n' - Number format
#'n' - 數字格式
#'%' - Percentage format
#'%' - 百分百格式
#Format 255 into a hexadecimal value:
#將 255 格式化為十六進位值：
x = format(255, 'x')
print(x)

