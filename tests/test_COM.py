import serial
import time
from os.path import join, dirname, realpath
import os

port = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=1)

print("Connected to: " + port.port)

portBuffer = bytearray()
recvTime = 0

count = 0
c = 0
while True:
    try:
        dataShow = bytearray()
        while port.inWaiting() > 0:
            recvTime = time.time()
            readByte = port.read()
            portBuffer += readByte
            dataShow += readByte
            #print(portBuffer.hex())
            if len(dataShow) > 20:
                print("> " + " ".join("%02x" % i for i in dataShow) + " .........")
            #    c = c + 1
                dataShow = bytearray()
        time.sleep(1)


        if (time.time() - recvTime > 5) and len(portBuffer) != 0:
            print("Новое изображение было получено!\n")
            #print("Recieved size = " + str(c*20))
            #print("Length of portBuffer = %d" % len(portBuffer))

            count += 1
            imageBuffer = bytearray()
            for i in range(0, len(portBuffer)):
                if i < len(portBuffer) - 5:
                    if portBuffer[i] == 5 and portBuffer[i+1] == 0 and portBuffer[i+2] == 130:
                        c += 1
                        for j in range(0, portBuffer[i+7]-2):
                            imageBuffer.append(portBuffer[i+10+j])
            
            #print("Number of packets = %d" % c)
            c = 0
            #print("Image size = %d" % len(imageBuffer))
            dataPath = join(dirname(realpath(__file__)), '../AppFlask/static/images/image.jpg')
            #os.remove(dataPath)
            f = open(dataPath, "wb")
            f.write(imageBuffer)
            f.close()
            portBuffer = bytearray()

    except KeyboardInterrupt:
        print("An exception")
        print("Good bye")
        break
