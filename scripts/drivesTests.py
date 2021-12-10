import drives
import time
import keyboard

SIM_DUR:float = 4.0
def main():
    motors = drives.get_motors()
    start_time = time.time()

    diff = 0 
    
    while diff < SIM_DUR:
        
        diff = time.time() - start_time
        
        counter = 1
        speed = (counter%10)/10
        drives.forward(motors, -0.9)
        time.sleep(0.1)

    drives.stop(motors)

        
        

        


if __name__ == '__main__':
    main()