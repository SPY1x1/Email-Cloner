import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        os.system('git pull')
        
        from spymail import Main
 
        Main()
 
 
 
elif bit == "32bit":
 
        os.system('git pull')
        
        print("   yiur device is 32bit ")
        
        print("   32 bit will update soon")
        
        os.system("am start https://www.facebook.com/SPY1x1/")
        
        exit()
 
 
 
