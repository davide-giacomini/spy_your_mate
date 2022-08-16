## With this script I will extract the features of the 860 frames and I will organize them with pandas

import pandas as pd
import numpy as np

def avg_packet_interval(packets):
    tot = 0.0
    for packet in packets:
        tot += float(packet.udp.time_delta)
    return tot / len(frame)

def avg_packet_size(packets):
    tot = 0.0
    for packet in packets:
        tot += float(packet.length)
    return tot / len(frame)

def in_out_pkts_number(packets):
    tot_in = 0
    tot_out = 0
    for packet in packets:
        if str(packet.ip.src) == '192.168.1.15':
            tot_out += 1
        elif str(packet.ip.dst) == '192.168.1.15':
            tot_in += 1
    return {'in': tot_in, 'out': tot_out}


data = []

time_interval = [] # Time interval
packets_number = [] # Number of packets for each frame
avg_pack_intervals = [] # Average packet intervals for each frame
avg_pack_sizes = []   # Average packet sizes for each frame
inbound_pkts_number = []    # Inbound packets number for each frame
outbound_pkts_number = []   # Outbound packets number for each frame

count = 0.0
for frame in FRAMES:
    time_interval.append(str(count * 0.5) + "s - " + str(0.5 + count * 0.5) + "s")
    packets_number.append(len(frame))
    avg_pack_intervals.append(avg_packet_interval(frame))
    avg_pack_sizes.append(avg_packet_size(frame))
    inbound_pkts_number.append(in_out_pkts_number(frame)['in'])
    outbound_pkts_number.append(in_out_pkts_number(frame)['in'])

    count += 1

data.extend([time_interval, packets_number, avg_pack_intervals, avg_pack_sizes, inbound_pkts_number, outbound_pkts_number])

df = pd.DataFrame(np.transpose(data), columns=['Time Interval', 'Pkts number', 'Avg pkts interval', 'Avg pkts size', 'Inbound pkts', 'Outbound pkts'])
df.to_csv('test.csv')