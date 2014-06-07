import sys
O=''
I,S=O.join(sys.stdin.readlines()).split(' ',1)
n=d=i=m=0
M=[0]*30000
while I[i:]:
 c=ord(I[i]);m+=c==62;m-=c==60;M[m]+=c<44;M[m]-=c==45
 n=(c==91)*(M[m]==0)+(c>92);d=c-92
 if 46==c:O+=chr(M[m])
 if(44==c)*S:M[m]=ord(S[0]);S=S[1:]
 while n:i-=d;n-=d*('['==I[i]);n+=d*(']'==I[i])
 i+=c<93
print O,
