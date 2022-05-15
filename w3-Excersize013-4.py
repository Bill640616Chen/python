#ValueError: '2' is not in list
while True:
      num=input()
      if num=='#':
            break
      num=num.split()
      A=['I','V','X','L','C','D','M']
      a=[1,5,10,50,100,500,1000]
      bb=0
      cc=0
      for i in num[0]: 
            aa=A.index(i)
            aa=a[aa]
            bb+=aa
      for ii in range(len(num[0])-1):
            ii=num[0][ii:ii+2] 
            if ii=='CM':
                  bb-=200
            elif ii =='CD':
                  bb-=200
            elif ii=='XC':
                  bb-=20
            elif ii=='XL':
                  bb-=20
            elif ii=='IX':
                  bb-=2
            elif ii=='IV':
                  bb-=2

      ii=0  
      for j in num[1]:
            oo=A.index(j)
            oo=a[oo]
            cc+=oo
      for ii in range(len(num[1])-1):
            ii=num[1][ii:ii+2] 
            if ii=='CM':
                  cc-=200
            elif ii =='CD':
                  cc-=200
            elif ii=='XC':
                  cc-=20
            elif ii=='XL':
                  cc-=20
            elif ii=='IX':
                  cc-=2
            elif ii=='IV':
                  cc-=2
      n=(bb-cc)**2
      if n==0:
            print('ZERO')
            continue
      n=n**0.5
      w=''
      n=int(n)
      if n>=1000:
            m=n//1000
            w+='M'*m
            n=n-m*1000
      if n>=500:
            if 999>=n and n>=900:
                  w+='CM'
                  n=n-900
            else:
                  w+='D'
                  n=n-500
      if n>=100:
            if 499>=n and n>=400:
                  w+='CD'
                  n=n-400
            else:
                  c=n//100
                  w+='C'*c
                  n=n-c*100
      if n>=50:
            if 99>=n and n>=90:
                  w+='XC'
                  n-=90
            else:
                  w+='L'
                  n=n-50
      if n>=10:
            if 49>=n and n>=40:
                  w+='XL'
                  n=n-40
            else:
                  x=n//10
                  w+='X'*x
                  n=n-x*10
      if n>=5:
            if 9==n:
                  w+='IX'
                  n-=9
            else:
                  w+='V'
                  n=n-5
      if n>=1:
            if 4==n:
                  w+='IV'
                  n=n-4
            else:
                  i=n//1
                  w+='I'*i
                  n=n-i*1
      print(w)  