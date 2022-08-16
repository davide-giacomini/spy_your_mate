## THIS SCRIPT CONVERTS ALL THE PACKETS INTO AN ARRAY DIVIDED IN INBOUND AND OUTBOUND
## IT IS VERY LONG SO IT'S ADVICED TO HAVE IT RUN ON A PYTHON CONSOLE TO SAVE THE ARRAYS AND THEN USE THE OTHER SCRIPTS


# Needed to run tshark on colab
import os
import nest_asyncio

import pyshark

# Useful for treating table-like data
import pandas as pd
# Numerical operations library
import numpy as np

nest_asyncio.apply()

path = "capture.pcapng"

inbound_packets = pyshark.FileCapture(path, display_filter='ip.src == 149.137.11.203 && ip.dst == 192.168.1.15 && udp.srcport == 8801 && udp.dstport == 60235')
outbound_packets = pyshark.FileCapture(path, display_filter='ip.dst == 149.137.11.203 && ip.src == 192.168.1.15 && udp.dstport == 8801 && udp.srcport == 60235')

IN_PACKETS = []
OUT_PACKETS = []

count = 0
for packet in inbound_packets:
  try:
    IN_PACKETS.append(packet)
    count+=1
    if count%1000 == 0:
        print(count)
  except:
    print("some error")

count = 0
for packet in outbound_packets:
  try:
    OUT_PACKETS.append(packet)
    count+=1
    if count%1000 == 0:
        print(count)
  except:
    print("some error")

print(len(IN_PACKETS))
print(len(OUT_PACKETS))