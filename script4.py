delta_sum_first_person_in = 0.0
delta_sum_first_person_out = 0.0
delta_sum_first_background_in = 0.0
delta_sum_first_background_out = 0.0
delta_sum_second_person_in = 0.0
delta_sum_second_person_out = 0.0
delta_sum_second_background_in = 0.0
delta_sum_second_background_out = 0.0
delta_sum_third_person_in = 0.0
delta_sum_third_person_out = 0.0

for packet in FIRST_PERSON_IN_PACKETS[1:]:
    delta_sum_first_person_in += float(packet.udp.time_delta)

for packet in FIRST_PERSON_OUT_PACKETS[1:]:
    delta_sum_first_person_out += float(packet.udp.time_delta)

for packet in FIRST_BACKGROUND_IN_PACKETS[1:]:
    delta_sum_first_background_in += float(packet.udp.time_delta)

for packet in FIRST_BACKGROUND_OUT_PACKETS[1:]:
    delta_sum_first_background_out += float(packet.udp.time_delta)

for packet in SECOND_PERSON_IN_PACKETS[1:]:
    delta_sum_second_person_in += float(packet.udp.time_delta)

for packet in SECOND_PERSON_OUT_PACKETS[1:]:
    delta_sum_second_person_out += float(packet.udp.time_delta)

for packet in SECOND_BACKGROUND_IN_PACKETS[1:]:
    delta_sum_second_background_in += float(packet.udp.time_delta)

for packet in SECOND_BACKGROUND_OUT_PACKETS[1:]:
    delta_sum_second_background_out += float(packet.udp.time_delta)

for packet in THIRD_PERSON_IN_PACKETS[1:]:
    delta_sum_third_person_in += float(packet.udp.time_delta)

for packet in THIRD_PERSON_OUT_PACKETS[1:]:
    delta_sum_third_person_out += float(packet.udp.time_delta)

delta_averages = {'in': {'person': {1: (delta_sum_first_person_in / len(FIRST_PERSON_IN_PACKETS)),
                                    2: (delta_sum_second_person_in / len(SECOND_PERSON_IN_PACKETS)),
                                    3: (delta_sum_third_person_in / len(THIRD_PERSON_IN_PACKETS))
                                    },
                         'background': {1: (delta_sum_first_background_in / len(FIRST_BACKGROUND_IN_PACKETS)),
                                        2: (delta_sum_second_background_in / len(SECOND_BACKGROUND_IN_PACKETS))
                                        }
                         },
                  'out': {'person': {1: (delta_sum_first_person_out / len(FIRST_PERSON_OUT_PACKETS)),
                                     2: (delta_sum_second_person_out / len(SECOND_PERSON_OUT_PACKETS)),
                                     3: (delta_sum_third_person_out / len(THIRD_PERSON_OUT_PACKETS))
                                     },
                         'background': {1: (delta_sum_first_background_out / len(FIRST_BACKGROUND_OUT_PACKETS)),
                                        2: (delta_sum_second_background_out / len(SECOND_BACKGROUND_OUT_PACKETS))
                                        }
                          }
                  }