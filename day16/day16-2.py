from collections import defaultdict
import math
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

def isValid(packet):
    if packet == "" or int(packet,2) == 0:
        return False
    return True

def readPacket(packet):

    while True:
        if packet == "" or int(packet,2) == 0:
            print("ERROR5")
            return 0, ""
            # break

        packetvision = packet[:3]
        print(f"Packet Version: {packetvision} {int(packetvision,2)}")
        total[0] += int(packetvision,2)
        typeId = int(packet[3:6],2)

        if typeId == 4:
            index = 6
            number = ""
            while True:
                if packet[index] == '0':
                    number += packet[index+1:index+5]
                    index += 5
                    break
                else:
                    number += packet[index+1:index+5]
                    index += 5
            packet = packet[index:]
            print("Number: ",end="")
            print(int(number),2)
            return((int(number,2), packet))
            # break
            # readPacket(packet)
        else:
            opId = packet[6]
            if opId == '0':
                print("Operator 0")
                # index = 6+1+15
                subpacklength = int(packet[7:7+15],2)
                # print(subpacklength)
                # print(int(subpacklength,2))
                numbers = []
                packet2 = packet[6+16:6+16+subpacklength]
                while True:
                    print(packet2)
                    if not isValid(packet2):
                        break
                    num, packet2 = readPacket(packet2)
                    numbers.append(num)

                print(numbers)
                print("TypeId: ",end="")
                print(typeId)
                packet = packet[6+16+subpacklength:]
                if typeId == 0:
                    return sum(numbers), packet
                if typeId == 1:
                    return math.prod(numbers), packet
                if typeId == 2:
                    return min(numbers), packet
                if typeId == 3:
                    return max(numbers), packet
                if typeId == 5:
                    if numbers[0] > numbers[1]:
                        return 1, packet
                    else:
                        return 0, packet
                if typeId == 6:
                    if numbers[0] < numbers[1]:
                        return 1, packet
                    else:
                        return 0, packet
                if typeId == 7:
                    if numbers[0] == numbers[1]:
                        return 1, packet
                    else:
                        return 0, packet
                print(typeId)
                print("ERROR")

            if opId == '1':
        
                print("Operator 1")
                numsubpackets = int(packet[7:7+11],2)
                # print(packet[7:7+11])
                # print(numsubpackets)
                # return readPacket(packet[7+12:])

                numbers = []
                packet = packet[7+11:]
                for i in range(numsubpackets):
                    if not isValid(packet):
                        break
                    num, packet = readPacket(packet)
                    numbers.append(num)

                print(numbers)
                print("TypeId: ",end="")
                print(typeId)
                
                if typeId == 0:
                    return sum(numbers), packet
                if typeId == 1:
                    return math.prod(numbers), packet
                if typeId == 2:
                    return min(numbers), packet
                if typeId == 3:
                    return max(numbers), packet
                if typeId == 5:
                    if numbers[0] > numbers[1]:
                        return 1, packet
                    else:
                        return 0, packet
                if typeId == 6:
                    if numbers[0] < numbers[1]:
                        return 1, packet
                    else:
                        return 0, packet
                if typeId == 7:
                    if numbers[0] == numbers[1]:
                        return 1, packet
                    else:
                        return 0, packet
                print(typeId)
                
                print("ERROR2")
                # print(packet[7+11:])
                # break
                # index += numsubpackets
                # print("bitstring:",end="")
                # packet = packet[index:]
                # print(packet)

                # print(index)
                # break

            print(typeId)
            print("ERROR3")
        print(typeId)
        print("ERROR4")


print(readPacket(bitsstring))


# print(total)