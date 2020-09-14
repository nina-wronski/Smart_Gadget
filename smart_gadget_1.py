import struct

import time

from bluepy.btle import Peripheral, DefaultDelegate, UUID

class SmartGadget(Peripheral):

    def __init__(self, device, interface=None):

        super(SmartGadget, self).__init__(deviceAddr=device, addrType='random', iface=interface)

    def temp_reading(self):
        handle = 0x0037
        temp_hnd_char = self.readCharacteristic(handle)
        upkd_bts = struct.unpack('<f',temp_hnd_char)
        return upkd_bts[0]

    def hum_reading(self):
        handle = 0x0032
        hum_hand_char = self.readCharacteristic(handle)
        upkd_bts = struct.unpack('<f',hum_hand_char)
        return upkd_bts[0]

#A2_device = 'F8:70:C7:E1:BB:A2'

#A2_SG = SmartGadget(A2_device)

#while True:
   # A2_SG.temp_reading()
   # A2_SG.hum_reading()

