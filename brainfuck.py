import sys
_=''.join([l for l in sys.stdin])
if' 'in _:I,S=_.split(' ',1)
else:I,S=_,''
s=i=m=0
M=[0]*30000
O=''
while i<len(I):
 c=I[i];m+=c=='>';m-=c=='<';M[m]+=c=='+';M[m]-=c=='-'
 if'.'==c:O+=chr(M[m])
 if','==c:
  M[m]=ord(S[s])if s<len(S)else-1
  s+=1
 n,d=0,0
 if c=='['and M[m]==0:n,d=1,1
 if c==']':n,d=1,-1
 while n:
  i+=d;f=I[i]
  if'['==f:n+=d
  if']'==f:n-=d
 i+=c!=']'
print O,
