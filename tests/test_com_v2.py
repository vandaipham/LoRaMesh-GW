import serial
import time
from os.path import join, dirname, realpath
import os

port = serial.Serial(
    port = '/dev/ttyUSB0',\
    baudrate=9600,\
    parity = serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0
)

print("Connected to: " + port.port)
portBuffer = []

recvTime = 0
numPacket = 0
imgNum = 0
while True:
    try:
        dataShow = []
        while port.inWaiting() > 0:
            recvTime = time.time()
            readByte = port.read()
            portBuffer.append(readByte)
            dataShow.append(readByte)
            if len(dataShow) > 20:
                print("> ")
                print(dataShow)
                dataShow = []
        time.sleep(1)

        if (time.time() - recvTime > 4) and len(portBuffer) != 0:
            print("Новое изображение было получено!\n")
            print("Lenght of portBuffer = %d" % len(portBuffer))
            imageBuffer = []
            imgNum += 1
            dataPath = join(dirname(realpath(__file__)), '../AppFlask/static/images/image.jpg')
            f = open(dataPath, 'wb')
            for i in range(0, len(portBuffer)):
                if i < len(portBuffer) - 5:
                    if portBuffer[i] == b'\x05' and portBuffer[i+1] == b'\x00' and portBuffer[i+2] == b'\x82':
                        numPacket += 1
                        #print("Packet No = %d " % numPacket)
                        for j in range(0, int.from_bytes(portBuffer[i+7], 'big') - 2):
                            imageBuffer.append(portBuffer[i+10+j])
                            f.write(portBuffer[i+10+j])

            print("Number of packets = %d" % numPacket)
            numPacket = 0
            print("Image size = %d" % len(imageBuffer))
            f.close()
            portBuffer = []

    except KeyboardInterrupt:
        print("Good bye!!")
        break