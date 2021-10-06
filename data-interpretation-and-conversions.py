# All data conversions and interpretation functions can be written here

# MODULE IMPORTS
import docx

# Reading document containing bytes
with open('1st_File.txt') as textFile:
    doc = textFile.read()


# Creates list of all bytes
bytesList = doc.split(" ")

# Converting bytes from hexadecimal to decimal
convertedBytes = []  # creates empty list of converted bytes
for i in range(len(bytesList)):
    byte = int(bytesList[i], 16)  # converts the bytes to decimal from hexadecimal (base 16)
    convertedBytes.append(byte)


# Interpreting destination and source MAC addresses
destinationMACAddressLIST = []
for x in range(6):
    destinationMACAddressLIST.append(bytesList[x])
sourceMACAddressLIST = []
for y in range(6, 12):
    sourceMACAddressLIST.append(bytesList[y])


# Interpreting Ethernet Type
typeBytes = []
for z in range(12, 14):
    typeBytes.append(bytesList[z])
if typeBytes[0] == "08":
    if typeBytes[1] == "00":
        ethernetType = "Internet (IPv4)"
    elif typeBytes[1] == "06":
        ethernetType = "Address Resolution (ARP)"
    else:
        ethernetType = "Unknown"
elif typeBytes[0] == "86":
    if typeBytes[1] == "DD":
        ethernetType = "Internet (IPv6)"
    else:
        ethernetType = "Unknown"
else:
    ethernetType = "Unknown"


# Interpreting protocol number
protocolNumber = bytesList[23]
if protocolNumber == "01":
    encapsulatedProtocol = "Internet Control Message (ICMP)"
elif protocolNumber == "02":
    encapsulatedProtocol = "Internet Group Management (IGMP)"
elif protocolNumber == "06":
    encapsulatedProtocol = "Transmission Control Protocol (TCP)"
elif protocolNumber == "11":
    encapsulatedProtocol = "Transport User Datagram (UDP)"
elif protocolNumber == "58":
    encapsulatedProtocol = "Routing Protocol EIGRP"
elif protocolNumber == "58":
    encapsulatedProtocol = "Routing Protocol OSPF"
else:
    encapsulatedProtocol = "Unknown"


# Interpreting IP addresses
sourceIPAddressLIST = []
for i in range(26, 30):
    sourceIPAddressLIST.append(convertedBytes[i])
sIP = sourceIPAddressLIST
sourceIPAddress = (str(sIP[0]) + '.' + str(sIP[1]) + '.' + str(sIP[2]) + '.' + str(sIP[3]))

destinationIPAddressLIST = []
for i in range(30, 34):
    destinationIPAddressLIST.append(convertedBytes[i])
dIP = destinationIPAddressLIST
destinationIPAddress = (str(dIP[0]) + '.' + str(dIP[1]) + '.' + str(dIP[2]) + '.' + str(dIP[3]))


