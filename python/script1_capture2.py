## THIS SCRIPT CONVERTS ALL THE PACKETS INTO AN ARRAY
## IT IS VERY LONG SO IT'S BETTER TO HAVE IT RUN ON A PYTHON CONSOLE TO SAVE THE ARRAY AND THEN USE THE OTHER SCRIPTS

import pyshark

print("Executing script 1.\n")

path = "capture2_test.pcapng"
packets = pyshark.FileCapture(path, display_filter='ip.addr == 149.137.11.142 && ip.addr == 192.168.1.15 && udp.port == 8801 && udp.port == 51541')

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

print("\n There are " + str(len(PACKETS)) + " packets in capture 2.\n")