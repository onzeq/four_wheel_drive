import time
from drives import Drives

SIM_DUR:float = 15.0
SLEEP_DUR:float = 0.5
def main():
    drives = Drives()
     
    
    print("driving method testing")

    start_time = time.time()
    diff = 0
    counter = 1
    
    while diff < SIM_DUR:
        
        diff = time.time() - start_time
        
        
        speed = 0.2 + (counter%8)/10
        counter = counter + 1
        drives.forward(speed)
        time.sleep(SLEEP_DUR)
        
        print(speed)
    
    drives.stop()

        
        

        


if __name__ == '__main__':
    main()