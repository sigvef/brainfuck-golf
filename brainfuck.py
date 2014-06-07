import sys
O=''
I,S=O.join(sys.stdin.readlines()).split(' ',1)
n=d=i=m=0
M=[0]*30000
while I[i:]:
 c=ord(I[i]);m+=c==62;m-=c==60;M[m]+=c<44;M[m]-=c==45
 if 46==c:O+=chr(M[m])
 if(44==c)*S:M[m]=ord(S[0]);S=S[1:]
 n=d=(c==91)*(M[m]==0)
 if c>92:n,d=1,-1
 while n:
  i+=d
  if'['==I[i]:n+=d
  if']'==I[i]:n-=d
 i+=c<93
print O,
