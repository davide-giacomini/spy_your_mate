import numpy as np
import pandas as pd


def avg_packet_interval(packets):
    tot = 0.0
    for packet in packets:
        tot += float(packet.udp.time_delta)
    return tot / len(packets)

def avg_packet_size(packets):
    tot = 0.0
    for packet in packets:
        tot += float(packet.length)
    return tot / len(packets)

def in_out_pkts_number(packets):
    tot_in = 0
    tot_out = 0
    for packet in packets:
        if str(packet.ip.src) == '192.168.1.15':
            tot_out += 1
        elif str(packet.ip.dst) == '192.168.1.15':
            tot_in += 1
    return {'in': tot_in, 'out': tot_out}

def in_out_pkts_interval(packets):
    tot_interval_in = 0
    tot_interval_out = 0
    tot_number_in = 0
    tot_number_out = 0
    prev_in_time_relative = 0.0
    prev_out_time_relative = 0.0

    for packet in packets:
        if str(packet.ip.src) == '192.168.1.15':
            if prev_out_time_relative>0:
                interval = float(packet.udp.time_relative) - prev_out_time_relative
                tot_interval_out += interval
                tot_number_out += 1
                prev_out_time_relative = float(packet.udp.time_relative)
            else:
                prev_out_time_relative = float(packet.udp.time_relative)
        elif str(packet.ip.dst) == '192.168.1.15':
            if prev_in_time_relative>0:
                interval = float(packet.udp.time_relative) - prev_in_time_relative
                tot_interval_in += interval
                tot_number_in += 1
                prev_in_time_relative = float(packet.udp.time_relative)
            else:
                prev_in_time_relative = float(packet.udp.time_relative)

    if tot_number_in>0 and tot_number_out>0:
        return {'in': (tot_interval_in / tot_number_in), 'out': (tot_interval_out / tot_number_out)}
    elif tot_number_in==0 and tot_number_out==0:
        return {'in': 0, 'out': 0}
    elif tot_number_in>0:
        return {'in': (tot_interval_in / tot_number_in), 'out': 0}
    else:
        return {'in': 0, 'out': (tot_interval_out / tot_number_out)}

def in_out_pkts_size(packets):
    tot_size_in = 0
    tot_size_out = 0
    tot_number_in = 0
    tot_number_out = 0
    for packet in packets:
        if str(packet.ip.src) == '192.168.1.15':
            tot_size_out += float(packet.length)
            tot_number_out += 1
        elif str(packet.ip.dst) == '192.168.1.15':
            tot_size_in += float(packet.length)
            tot_number_in += 1

    if tot_number_in>0 and tot_number_out>0:
        return {'in': (tot_size_in / tot_number_in), 'out': (tot_size_out / tot_number_out)}
    elif tot_number_in==0 and tot_number_out==0:
        return {'in': 0, 'out': 0}
    elif tot_number_in>0:
        return {'in': (tot_size_in / tot_number_in), 'out': 0}
    else:
        return {'in': 0, 'out': (tot_size_out / tot_number_out)}


def cycle(callback, frames):

    print("Executing script 3.\n")

    data = []

    time_interval = []  # Time interval
    packets_number = []  # Number of packets for each frame
    avg_pack_intervals = []  # Average packet intervals for each frame
    avg_pack_sizes = []  # Average packet sizes for each frame
    inbound_pkts_number = []  # Inbound packets number for each frame
    outbound_pkts_number = []  # Outbound packets number for each frame
    avg_in_pkts_interv = [] # Inbound packet interval
    avg_out_pkts_interv = [] # Outbound packet interval
    avg_in_pkts_size = []   # Inbound packet size
    avg_out_pkts_size = []  # Outbound packet size
    person = []  # If the person is present (1) or not (0)

    count = 0.0
    for frame in frames:
        time_interval.append(str(count * 0.5) + "s - " + str(0.5 + count * 0.5) + "s")
        packets_number.append(len(frame))
        avg_pack_intervals.append(avg_packet_interval(frame))
        avg_pack_sizes.append(avg_packet_size(frame))
        inbound_pkts_number.append(in_out_pkts_number(frame)['in'])
        outbound_pkts_number.append(in_out_pkts_number(frame)['out'])
        avg_in_pkts_interv.append(in_out_pkts_interval(frame)['in'])
        avg_out_pkts_interv.append(in_out_pkts_interval(frame)['out'])
        avg_in_pkts_size.append(in_out_pkts_size(frame)['in'])
        avg_out_pkts_size.append(in_out_pkts_size(frame)['out'])
        person.append(callback(frame))

        count += 1

    data.extend([time_interval, packets_number, avg_pack_intervals, avg_pack_sizes, inbound_pkts_number,
                 outbound_pkts_number, avg_in_pkts_interv, avg_out_pkts_interv, avg_in_pkts_size, avg_out_pkts_size, person])

    return pd.DataFrame(np.transpose(data), columns=['Time Interval', 'Pkts number', 'Avg pkts interval',
                                                   'Avg pkts size', 'Inbound pkts','Outbound pkts', 'In pkts interval',
                                                     'Out pkts interval', 'In pkts size', 'Out pkts size', 'Person'])