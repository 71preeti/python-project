import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
target_ip="127.0.0.1"      # with in a system used to refer itself system  ke liye local host ip address h 
target_port=2525
target_address=(target_ip,target_port)
condition = True
while condition:
    message=input("Please enter your msg : ")
    message_encrypted=message.encode("ascii")

    s.sendto(message_encrypted,target_address)
    print("Your msg is send......")
    Permission=input("Do you want to quit this chat  press Y/N")
    if Permission=="y" or Permission=="y":
        condition=False
