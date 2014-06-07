import sys
inp = ''.join([l for l in sys.stdin])
if ' ' in inp:
    i,s=inp.split(' ',1)
else:
    i=inp
    s=''
sp=0
pc=0
dp=0
m=[0]*30000
out = ''

while pc<len(i):
    c=i[pc]
    if c=='>':
        dp += 1
    if c=='<':
        dp -= 1
    if c=='+':
        m[dp]+=1
    if c=='-':
        m[dp]-=1
    if c=='.':
        out+=chr(m[dp])
    if c==',':
        m[dp]=ord(s[sp]) if sp<len(s) else -1
        sp+=1
    if c=='[':
        if m[dp] == 0:
            scopes = 1
            while scopes:
                pc += 1
                if i[pc] == '[':
                    scopes += 1
                if i[pc] == ']':
                    scopes -= 1
    elif c==']':
        scopes = 1
        pc-=1
        while scopes:
            if i[pc] == ']':
                scopes += 1
            if i[pc] == '[':
                scopes -= 1
            pc -= 1
    pc += 1
print out,
