n = input()
def password():
    m = ""
    for i in n:
        m = int(ord(i)) - 7
        print(chr(m),end = '')
password()

