import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # socket class ka object s h 
# through the internet= socket.AF_INET
# protocol (UDP/TCP)= socket.SOCK_DGRAM
ip_address = "127.0.0.1"
port_no=2525
complete_address = (ip_address,port_no)
s.bind(complete_address)        # register complete address 
print("Hii I am listening :")
while True:         # infinite loop
    data=s.recvfrom(100)   # 100 means at a time 100 char.ka msg receive kr skta h nhi to error aayega
    message=data[0]
    message=message.decode("ascii")
    sender_address=data[1]
    sender_ip_address=data[1][0]
    print(data)
   
        
   


