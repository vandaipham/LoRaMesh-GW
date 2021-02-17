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
recvTime = 0

while True:
    try:
        while port.inWaiting() > 0:
            recvTime = time.time()
            portBuffer += port.read()
        time.sleep(1)


        if (time.time() - recvTime > 10) and len(portBuffer) != 0:
            print(portBuffer.hex())

            imageBuffer = bytearray()
            for i in range(0, len(portBuffer)):
                if i < len(portBuffer) - 5:
                    if portBuffer[i] == 5 and portBuffer[i+1] == 0 and portBuffer[i+2] == 130:
                        for j in range(0, portBuffer[i+7]-2):
                            imageBuffer.append(portBuffer[i+10+j])
            
            f = open("D:\Dev_Workspace\LoRaMesh-GW\AppFlask\static\images\image.jpg", "wb")
            f.write(imageBuffer)
            f.close()
            portBuffer = bytearray()

    except KeyboardInterrupt:
        print("An exception")
        print("Good bye")
        break