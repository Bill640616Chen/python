#無法執行
while True:
    try:

        str_1, str_2 = input().split(' ')
    except:
        break

    r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}

    list1 = [r2i[i] for i in str_1]
    list2 = [r2i[i] for i in str_2]

    for c in range(len(list1) - 1):
        if list1[c] < list1[c+1]:
            list1[c] *= -1

    for x in range(len(list2) - 1):
        if list2[x] < list2[x+1]:
            list2[x] *= -1

    num1 = sum(list1)
    num2 = sum(list2)

    if num1 > num2:
        num = num1 - num2
    else:
        num = num2 - num1

    i2r = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
           50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    if num == 0:
        print('ZERO')

    r_str = ''

    while num > 0:
        for key in i2r:
            if num >= key:
                r_str += i2r[key]
                num -= key

    print(r_str)
