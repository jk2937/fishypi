import socket
import RPi.GPIO as GPIO

from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(1, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW) 

HOST = ''  
PORT = 5555  

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.setblocking(False)  
udp_server_socket.bind((HOST, PORT))
print(f"Echo server started on {HOST}:{PORT}")

while True:
    try:
        data, addr = udp_server_socket.recvfrom(4096)
        if len(data) > 0:
            message = data.decode()
            print(message)

            if(message == "A Positive"):
                GPIO.output(0, GPIO.LOW)
                GPIO.output(1, GPIO.HIGH)
            if(message == "A Negative"):
                GPIO.output(0, GPIO.HIGH)
                GPIO.output(1, GPIO.LOW)
            if(message == "A Neutral"):
                GPIO.output(0, GPIO.LOW)
                GPIO.output(1, GPIO.LOW)

            if(message == "B Positive"):
                GPIO.output(2, GPIO.LOW)
                GPIO.output(3, GPIO.HIGH)
            if(message == "B Negative"):
                GPIO.output(2, GPIO.HIGH)
                GPIO.output(3, GPIO.LOW)
            if(message == "B Neutral"):
                GPIO.output(2, GPIO.LOW)
                GPIO.output(3, GPIO.LOW)

            udp_server_socket.sendto(data, addr)

    except BlockingIOError:
        pass  # No data was ready to read, continue to next iteration

