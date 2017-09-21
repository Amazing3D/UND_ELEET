import serial
import time
from random import randint

while True:
    try:
	
	serialport = serial.Serial("/dev/ttyAMA0",9600)
	while True:
		frame = "f2"
		i = 0
		while i < 64:
			num = randint(0,255)
			add = ""
			if 16 > num >= 0:
				add = "0" + str(hex(num)[2:])
			else:
				add =  hex(num)[2:]
			frame = frame + add
			i = i+1
		print(frame)
		serialport.write(frame.decode('hex'))
		time.sleep(1)
        
        
    except KeyboardInterrupt:
        print("User interrupt encountered. Exiting...")
        time.sleep(3)
        exit()
    except:
        # for all other kinds of error, but not specifying which one
        print("Unknown error...")
        time.sleep(3)
        exit()
