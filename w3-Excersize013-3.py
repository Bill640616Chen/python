#只有輸入沒有轉換成羅馬數字
table={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
add=[['IV','IX','V','I'],['XL','XC','L','X'],['CD','CM','D','C'],['','','','M']]

def trans_to_num(n):
  std=0
  ans=0
  for i in range(len(n)-1,-1,-1):
    if table[n[i]]>=std:
      ans+=table[n[i]]
      std=table[n[i]]
    else:
      ans-=table[n[i]]
  return ans

def trans_to_chr(n):
  n=str(n)
  cnt=0
  ans=''
  if n=='0':
    return 'ZERO'
  for i in range(len(n)-1,-1,-1):
    i=n[i]
    if i=='4':
      ans=add[cnt][0]+ans
    elif i=='9':
      ans=add[cnt][1]+ans
    else:

      if int(i)>=4:

        ans=(add[cnt][2]+(add[cnt][3]*(int(i)-5)))+ans

      else:

        ans=add[cnt][3]*int(i)+ans
    cnt+=1
  return ans

try:
  while True:
    a,b=map(trans_to_num,input().split())
    print(trans_to_chr(abs(a-b)))
except KeyError:
  pass 
