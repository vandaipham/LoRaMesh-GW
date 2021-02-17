import serial
import time

port = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0)

print("Connected to: " + port.port)

portBuffer = bytearray()

while True:
	try:
		while port.inWaiting() > 0:
            recvTime = time.time()
            portBuffer += port.read()
            time.sleep(1)
            
        if time.time() - recvTime > 30:
            postBuffer = bytearray()
            for i in range(0,len(portBuffer)):
                if i < len(portBuffer) - 5:
                    if portBuffer[i] == 5 and portBuffer[i+1] == 0 and portBuffer[i+2] == 130:
                        for j in range(0,portBuffer[i+7]-2):
                            postBuffer.append(portBuffer[i+10+j])
            f = open("received.jpg" , "wb")
		    f.write(postBuffer)
		    f.close()
            portBuffer = bytearray()
    except:
        print("An exception occurred")