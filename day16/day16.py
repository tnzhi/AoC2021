from collections import defaultdict
import fileinput
inp = fileinput.input()
lines = [a.strip() for a in inp ]
print(lines)
code = lines[0]

scale = 16 ## equals to hexadecimal

num_of_bits = 8

h_size = len(code) * 4


bitsstring = bin(int(code, scale))[2:].zfill(h_size)
bitsint = int(code, scale)
print(bin(bitsint))




total = [0]

def readPacket(packet):

    while True:
        if packet == "" or int(packet,2) == 0:
            break

        packetvision = packet[:3]
        print(f"Packet Version: {packetvision} {int(packetvision,2)}")
        total[0] += int(packetvision,2)
        typeId = int(packet[3:6],2)

        if typeId == 4:
            index = 6
            while True:
                if packet[index] == '0':
                    index += 5
                    break
                else:
                    index += 5
            packet = packet[index:]
        else:
            opId = packet[6]
            if opId == '0':
                print("Operator 0")
                index = 6+1+15
                subpacklength = int(packet[6:6+14],2)
                # print(subpacklength)
                # print(int(subpacklength,2))
                readPacket(packet[6+16:])
                index +=  subpacklength
                packet = packet[index:]
                # print(index)
                print("bitstring:",end="")
                print(packet)
                break

            if opId == '1':
                print("Operator 1")
                numsubpackets = int(packet[7:7+11],2)
                print(packet[7:7+11])
                print(numsubpackets)
                readPacket(packet[7+11:])
                print(packet[7+11:])
                break
                # index += numsubpackets
                # print("bitstring:",end="")
                # packet = packet[index:]
                # print(packet)

                # print(index)
                # break
readPacket(bitsstring)


print(total)