import os
with open("D:\\AI\\videourls.txt") as f:
    for i in range(0,7):
        os.putenv("VARVAR",f.readline())
        os.system("lecturedownloader.bat") 
