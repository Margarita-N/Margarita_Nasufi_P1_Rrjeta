import socket

serverName='localhost'
serverPort=1200

serverName=input('Shkruani emrin e serverit me te cilin deshironi te lidheni:')
serverPort=input('Shkruani portin e serverit me te cilin deshironi te lidheni:')

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((serverName,int(serverPort)))
var=input("Jeni lidhur me serverin\nShkruani njeren nga komandat(IPADDRESS, PORT, COUNT, REVERSE, PALINDROME, TIME, GAME, GCF, CONVERT)?:")

s.sendall(str.encode(var))

mesazhi=''
while True:
    data=s.recv(10)
    if len(data)<=0:
        break
    mesazhi+=data.decode("utf-8")
print('Te dhenat e pranuara nga serveri',mesazhi)
s.close()



