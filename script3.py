## THIS SCRIPT DIVIDES THE INBOUNDS PACKETS INTO FRAMES WITH BACKGROUND AND WITHOUT BACKGROUND

FIRST_PERSON_OUT_PACKETS = []
FIRST_BACKGROUND_OUT_PACKETS = []
SECOND_PERSON_OUT_PACKETS = []
SECOND_BACKGROUND_OUT_PACKETS = []
THIRD_PERSON_OUT_PACKETS = []

for packet in OUT_PACKETS:
    if float(packet.udp.time_relative) <= 139.0:
        FIRST_PERSON_OUT_PACKETS.append(packet)
    elif float(packet.udp.time_relative) <= 210.0:
        FIRST_BACKGROUND_OUT_PACKETS.append(packet)
    elif float(packet.udp.time_relative) <= 279.0:
        SECOND_PERSON_OUT_PACKETS.append(packet)
    elif float(packet.udp.time_relative) <= 353.0:
        SECOND_BACKGROUND_OUT_PACKETS.append(packet)
    else:
        THIRD_PERSON_OUT_PACKETS.append(packet)