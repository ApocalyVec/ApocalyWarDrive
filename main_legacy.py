import argparse
import rssi
import numpy as np

"""



example usage

"""


def main(args):
    """

    :param args: arguements given by the user

    arguments for main:

        Required:
        -nwi: the name of your WIFI interface.
            For MAC users, use this terminal command: system_profiler SPNetworkDataType | grep Wi-Fi -A10
            The name is denoted by "BSD Device Name", in my case, it's en0
        -itv: time interval between samples, unit = millisecond
        -drt: the duration during which to capture samples, unit = millisecond

        Optional:
        -ave: take the average of give number of samples
    """
    # start parsing arguments
    nt_interface = args.nwInterface
    sampling_interval = args.interval
    sampling_duration = args.duration

    num_samples = int(sampling_duration / sampling_interval)

    config_msg = 'The WI-FI interface for scanning is ' + nt_interface
    sampling_msg = 'This will take ' + str(num_samples) + ' samples in ' + str(
        sampling_duration) + ' ms.\nPress enter to continue...'
    input(config_msg + '\n' + sampling_msg)
    # end of parsing arguments

    # initialize scanner
    rssi_scanner = rssi.RSSI_Scan(nt_interface)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-nwi', '--nwInterface', type=str, required=True,
                        help='the duration during which to capture samples, unit = millisecond')
    parser.add_argument('-i', '--interval', type=int, required=True,
                        help='time interval between samples, unit = millisecond')
    parser.add_argument('-d', '--duration', type=int, required=True,
                        help='the duration during which to capture samples, unit = millisecond')

    # parser.add_argument("--nice", type=str2bool, nargs='?',
    #                     const=True, default=NICE,
    #                     help="Activate nice mode.")
    # parser.add_argument('-fl', '--full_length', type=str2bool, nargs='?',
    #                     help='group in full length', const=True, default=False)

    args = parser.parse_args()
    main(args)
