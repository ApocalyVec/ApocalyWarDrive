import rssi
import numpy as np

rssi_scanner = rssi.RSSI_Scan('en6')
ap_info = rssi_scanner.getAPinfo(sudo=True)