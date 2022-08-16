## This script divides all packets in frames of half a second.
## I use a list of a list to create a dynamic and different-size rows matrix

AGGREGATES = []

list = []
if len(PACKETS) > 0:
    list.append(PACKETS[0])
    AGGREGATES.append(list)
else:
    print("there are no packets in the array \'PACKETS\'\n")

for packet in PACKETS[1:]:
    if int(float(AGGREGATES[-1][-1].udp.time_relative) / 0.5) < int(float(packet.udp.time_relative) / 0.5):
        AGGREGATES.append([])
    AGGREGATES[-1].append(packet)

