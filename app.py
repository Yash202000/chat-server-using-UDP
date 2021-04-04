import socket
import threading
import os

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )  #using UDP protocol
s.bind(("192.168.43.132",567)) #reciever's IP address and port on which we are collecting mesaages
os.system("tput setaf 3")
print("\t\t\t====>  UDP CHAT APP  <=====")
os.system("tput setaf 2") #changing color of terminal
print("==============================================")
nm = input("ENTER YOUR NAME : ") #user name
os.system("tput setaf 6")
print("\nType 'quit' to exit.")
os.system("tput setaf 2")

def send():
    while True:
        os.system("tput setaf 2")
        ms = input()
        if ms == "quit":
            os.system("tput setaf 7")
            os._exit(1)
        sm = "{}  : {}".format(nm,ms)
        s.sendto(sm.encode() , ("192.168.43.122",1234) )  #sender's IP address and port on which they are collecting messages

def rec():
    while True:
        msg = s.recvfrom(1024)
        os.system("tput setaf 5")
        print("\t\t\t\t" +  msg[0].decode()  )
        os.system("tput setaf 2")

x1 = threading.Thread( target = send ) #creating thread1
x2 = threading.Thread( target = rec ) #creating thread2

x1.start() #initializing thread1
x2.start() #initializing thread2
