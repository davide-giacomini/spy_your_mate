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

path = "capture_train.pcapng"

packets = pyshark.FileCapture(path, display_filter='ip.addr == 149.137.11.203 && ip.addr == 192.168.1.15 && udp.port == 8801 && udp.port == 60235')

IN_PACKETS = []
OUT_PACKETS = []

PACKETS = []

count = 0
for packet in packets:
  try:
    PACKETS.append(packet)
    count+=1
    if count%1000 == 0:
        print(count)
  except:
    print("some error")

print(len(PACKETS))