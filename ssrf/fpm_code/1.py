import urllib.parse

a=''
with open('hex.txt','r') as f:
    for i in f.readlines():
        i=i.strip('\n')
        a+=i
b=''
length=len(a)
for i in range(0,length,2):
    b+='%'
    b+=a[i]
    b+=a[i+1]
b=urllib.parse.quote(b)
print(b)
