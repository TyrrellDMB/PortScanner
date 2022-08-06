from socket import *
import time
startTime = time.time()

def portScan():
   target = input('Enter the host to be scanned: ')
   tarIP = gethostbyname(target)
   print ('Starting scan on host: ', tarIP)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((target, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()  
   print('Time taken:', time.time() - startTime)

if __name__ == '__main__':
    portScan()