import serial
import time
from random import randint
import datetime
import pytz

start_time = time.time()

while True:
    try:
		
	serialport = serial.Serial("/dev/ttyAMA0",9600)
	while True:
		num = 0
		pos = 0
		while num < 256:
			frame = "f2"
			i = 0
			while i < 64:
				if i == pos:
					add = ""
					if 16 > num >= 0:
						add = "0" + str(hex(num)[2:])
					else:
						add =  hex(num)[2:]
					frame = frame + add
				elif i < pos:
					frame = frame + "ff"
				else:
					frame = frame + "00"

				i = i + 1
#			print(frame)
			serialport.write(frame.decode('hex'))
			time.sleep(.1)
			num = num + 1
			if num == 256:
				pos = pos + 1
				num = 0
				print("%f seconds" % (time.time() - start_time))
				with open('timer.txt', 'w') as f:
    					f.write("%f seconds" % (time.time() - start_time))
			if pos == 64:
				pos = 0
        
        
    except KeyboardInterrupt:
        print("User interrupt encountered. Exiting...")
        time.sleep(3)
        exit()
    except:
        # for all other kinds of error, but not specifying which one
        print("Unknown error...")
        time.sleep(3)
        exit()
