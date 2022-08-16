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

def person_or_background(packets):
    first_time = float(packets[0].udp.time_relative)
    last_time = float(packets[-1].udp.time_relative)
    FIRST_THRESHOLD = 139.0
    SECOND_THRESHOLD = 210.0
    THIRD_THRESHOLD = 279.0
    FOURTH_THRESHOLD = 353.0

    if last_time < FIRST_THRESHOLD or first_time >= FOURTH_THRESHOLD or (first_time >= SECOND_THRESHOLD and last_time < THIRD_THRESHOLD):
        return 1
    else:
        return 0


data = []

time_interval = [] # Time interval
packets_number = [] # Number of packets for each frame
avg_pack_intervals = [] # Average packet intervals for each frame
avg_pack_sizes = []   # Average packet sizes for each frame
inbound_pkts_number = []    # Inbound packets number for each frame
outbound_pkts_number = []   # Outbound packets number for each frame
person = [] # If the person is present (1) or not (0)

count = 0.0
for frame in FRAMES:
    time_interval.append(str(count * 0.5) + "s - " + str(0.5 + count * 0.5) + "s")
    packets_number.append(len(frame))
    avg_pack_intervals.append(avg_packet_interval(frame))
    avg_pack_sizes.append(avg_packet_size(frame))
    inbound_pkts_number.append(in_out_pkts_number(frame)['in'])
    outbound_pkts_number.append(in_out_pkts_number(frame)['in'])
    person.append(person_or_background(frame))

    count += 1

data.extend([time_interval, packets_number, avg_pack_intervals, avg_pack_sizes, inbound_pkts_number, outbound_pkts_number, person])

df = pd.DataFrame(np.transpose(data), columns=['Time Interval', 'Pkts number', 'Avg pkts interval', 'Avg pkts size', 'Inbound pkts', 'Outbound pkts', 'Person'])
df.to_csv('capture1_train.csv')