#! python3
import sys,os
try:
    from googlesearch import search
except ImportError:
    print("NOT FOUND")
query=' '.join(sys.argv[1:])   
for j in search(query,tld="com",num=1,stop=1):
    resultaddress=j
os.putenv("VARVAR",resultaddress)
os.system("ytdldirect.bat")    
    
