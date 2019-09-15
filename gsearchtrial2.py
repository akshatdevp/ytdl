#! python3
import pyperclip,sys,os
try:
    from googlesearch import search
except ImportError:
    print("NOT FOUND")
query=' '.join(sys.argv[1:])   
for j in search(query,tld="com",num=1,stop=1):
    pyperclip.copy(j)
os.putenv("VARVAR",pyperclip.paste())
os.system("ytdldirect.bat")    
    
