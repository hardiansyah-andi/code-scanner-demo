import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 31137))
s.bind(('192.168.0.1', 8080))
