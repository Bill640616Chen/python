#dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
from sys import stdin
dict = {1:'I',26:'XXVI',51:'LI',76:'LXXVI',
2:'II',27:'XXVII',52:'LII',77:'LXXVII',
3:'III',28:'XXVIII',53:'LIII',78:'LXXVIII',
4:'IV',29:'XXIX',54:'LIV',79:'LXXIX',
5:'V',30:'XXX',55:'LV',80:'LXXX',
6:'VI',31:'XXXI',56:'LVI',81:'LXXXI',
7:'VII',32:'XXXII',57:'LVII',82:'LXXXII',
8:'VIII',33:'XXXIII',58:'LVIII',83:'LXXXIII',
9:'IX',34:'XXXIV',59:'LIX',84:'LXXXIV',
10:'X',35:'XXXV',60:'LX',85:'LXXXV',
11:'XI',36:'XXXVI',61:'LXI',86:'LXXXVI',
12:'XII',37:'XXXVII',62:'LXII',87:'LXXXVII',
13:'XIII',38:'XXXVIII',63:'LXIII',88:'LXXXVIII',
14:'XIV',39:'XXXIX',64:'LXIV',89:'LXXXIX',
15:'XV',40:'XL',65:'LXV',90:'XC',
16:'XVI',41:'XLI',66:'LXVI',91:'XCI',
17:'XVII',42:'XLII',67:'LXVII',92:'XCII',
18:'XVIII',43:'XLIII',68:'LXVIII',93:'XCIII',
19:'XIX',44:'XLIV',69:'LXIX',94:'XCIV',
20:'XX',45:'XLV',70:'LXX',95:'XCV',
21:'XXI',46:'XLVI',71:'LXXI',96:'XCVI',
22:'XXII',47:'XLVII',72:'LXXII',97:'XCVII',
23:'XXIII',48:'XLVIII',73:'LXXIII',98:'XCVIII',
24:'XXIV',49:'XLIX',74:'LXXIV',99:'XCIX',
25:'XXV',50:'L',75:'LXXV',100:'C',
}


for s in stdin: 
    if int(s) == 0:
        s = 'zero'
        print(s)
    else:
        r = dict.get(int(s))
        print(type(s))
        print(r)
    break

#point = {'x':4,'y':-5}
#4
#print('{x} '.format(**point))
#用format,{}內只能接受字串的鍵,取鍵的值
#n = dict.get(1)
#print(n+n+n)
#III
#list1 = list(dict)
#print(list1) #印出鍵