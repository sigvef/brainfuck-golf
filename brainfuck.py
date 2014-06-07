import sys
I,S=''.join(sys.stdin.readlines()).split(' ',1)
i=m=0
M=[0]*30000
O=''
while i<len(I):
 n,d=0,0;c=ord(I[i]);m+=c==62;m-=c==60;M[m]+=c<44;M[m]-=c==45
 if 46==c:O+=chr(M[m])
 if(44==c)*S:
  M[m]=ord(S[0])
  S=S[1:]
 if(c==91)*(M[m]==0):n,d=1,1
 if c>92:n,d=1,-1
 while n:
  i+=d
  if'['==I[i]:n+=d
  if']'==I[i]:n-=d
 i+=c<93
print O,
