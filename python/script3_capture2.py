## With this script I will extract the features of the frames and I will organize them with pandas

import script3_util


def person_or_background(packets):
    first_time = float(packets[0].udp.time_relative)
    last_time = float(packets[-1].udp.time_relative)
    FIRST_THRESHOLD = 75.0
    SECOND_THRESHOLD = 137.0
    THIRD_THRESHOLD = 209.0
    FOURTH_THRESHOLD = 273.0

    if last_time < FIRST_THRESHOLD or first_time >= FOURTH_THRESHOLD or (first_time >= SECOND_THRESHOLD and last_time < THIRD_THRESHOLD):
        return 1
    else:
        return 0

df = script3_util.cycle(person_or_background, FRAMES)

df.to_csv('capture2_test.csv')