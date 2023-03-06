import socket
class IN:
    IP_MTU = 14
    IP_MTU_DISCOVER = 10
    IP_PMTUDISC_DO = 2


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
hostName = "192.168.0.112"
Port = 9999
s.connect((hostName, Port))
s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)
MTU_Size = 1000    #1488
try:
    s.send(b'#' * 44 * MTU_Size)
except socket.error:
    print('The message did not make it')
    option = getattr(IN, 'IP_MTU', 14)
    print('MTU:', s.getsockopt(socket.IPPROTO_IP, option))
else:
    print('My network supports', MTU_Size, 'big packets!')
