import struct

ADDR = ("127.0.0.1", 8888)
st = struct.Struct("i16sif")
sockfd = socket(AF_INET, SOCK_DGRAM)

