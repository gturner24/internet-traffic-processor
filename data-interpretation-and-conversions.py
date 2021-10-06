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
destinationMACAddress = []
for x in range(6):
    destinationMACAddress.append(bytesList[x])
sourceMACAddress = []
for y in range(6, 12):
    sourceMACAddress.append(bytesList[y])


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
