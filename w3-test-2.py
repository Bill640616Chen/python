def format(a):
    o = ord(a)-7
    return chr(o)
string = input()
ans = ""
for i in range(len(string)):
    ans += format(string[i])
print(ans)