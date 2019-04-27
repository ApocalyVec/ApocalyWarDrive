from wifi import Cell, Scheme
import numpy as np
import time

nt_inerface = 'wlan0'


def record(interval, iterations):
    """
    we are not guranteed to see all the AP at every iteraion

    :param interval: int: unit is second, minimal value is 0.333 sec
    :param iterations: int: unit is mullisecond, minimal value is 1
    :param address: str: only valid when all is set to False, the address of the Ap of interest
    :param all: bool:
    """

    global nt_inerface

    i = 0  # iteration counter
    recording_dict = dict()  # key = time since start, value = list of aps if all is True, value =

    overall_start_time = time.time()

    while i < iterations:
        start_time = time.time()

        i = i + 1

        cell = Cell.all(nt_inerface)
        ap_list = set(cell)

        for ap in ap_list:
            recording_dict[time.time() - start_time] = ap_list

        # end_time = time.time()
        # i_time = end_time - start_time
        # remaining_time = interval - i_time


        # if remaining_time > 0:
        #     time.sleep(remaining_time)

        time.sleep(interval)


    print('Finish time is: ' + str(time.time() - overall_start_time))

    return recording_dict


if __name__ == '__main__':

    # nt_inerface = 'wlan0'
    #
    # start = time.time()
    #
    # ap_cell = Cell.all(nt_inerface)
    #
    # ap_list = set(ap_cell)
    #
    # for ap in ap_list:
    #     print('SSID: ' + str(ap.ssid) + ', signal: ' + str(ap.signal) + ', address: ' + str(ap.address) + ', quality: '
    #           + str(ap.quality) + ', frequency: ' + str(ap.frequency) + ', bitrates: ' + str(ap.bitrates) + \
    #           ',encrypted: ' + str(ap.encrypted) + ', channel: ' + str(ap.channel) + ', mode: ' + str(ap.mode))
    #
    # end = time.time()
    # print('Run time was ' + str(end - start))

    recording_dict = record(1, 10)
    i = 0
    for timestamp, ap_list in recording_dict.items():
        i += 1
        print('Timestamp: ' + str(timestamp))
        for ap in ap_list:
            print('SSID: ' + str(ap.ssid) + ', signal: ' + str(ap.signal) + ', address: ' + str(
                ap.address) + ', quality: '
                  + str(ap.quality) + ', frequency: ' + str(ap.frequency) + ', bitrates: ' + str(ap.bitrates) + \
                  ',encrypted: ' + str(ap.encrypted) + ', channel: ' + str(ap.channel) + ', mode: ' + str(ap.mode))
        print(i)

