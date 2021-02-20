import serial
import time

port = serial.Serial(
    port='/dev/ttyS0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0)

print("Connected to: " + port.port)

f = open("Full_log" , "wb")
while True:
	try:
		portBuffer = bytearray()
		while port.inWaiting() > 0:
			portBuffer += port.read()	

		if len(portBuffer) > 0:
			f.write(portBuffer)
			print("\n" + portBuffer.hex())
		time.sleep(1)
		
	except KeyboardInterrupt:
		f.close()
		port.close()
		f = open("Full_log" , "rb")
		postBuffer = bytearray(f.read())
		f.close()
		postBuffer2 = bytearray()
		
		for i in range(0,len(postBuffer)):
			if i < len(postBuffer) - 5:
				if postBuffer[i] == 5 and postBuffer[i+1] == 0 and postBuffer[i+2] == 130:
					for j in range(0, postBuffer[i+7] - 2):
						postBuffer2.append(postBuffer[i+10+j])
		
		f = open("received.jpg" , "wb")
		f.write(postBuffer2)
		f.close()
		print("\nGoodbye!!!")
		break

