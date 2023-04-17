import socket

target_host = "172.17.0.2"
target_port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"GET / HTTP/1.1\r\nHost: 172.17.02\r\n\r\n",
              (target_host, target_port))

data, addr = client.recvfrom(4096)
print(data.decode())
client.close()
