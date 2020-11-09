import time
import sys
for x in range (0,20):  
    b = "Loading" + "." * x
    print (b, end="\r")
    time.sleep(0.1)


sys.stdout.write("\033[K")
print('test') 
