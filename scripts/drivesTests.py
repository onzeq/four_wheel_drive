import drives
import time
import keyboard


def main():
    motors = drives.get_motors()
    
    while 1:

        counter = 1
        speed = (counter%10)/10
        drives.forward(motors, counter%10)
        time.sleep(0.1)

        try:
            if(keyboard.is_pressed('esc')):
                drives.stop(motors)

        except:
            break


if __name__ == '__main__':
    main()