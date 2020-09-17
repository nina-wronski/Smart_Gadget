import struct

import time

from bluepy.btle import Peripheral, DefaultDelegate, UUID, BTLEDisconnectError

class SmartGadget(Peripheral):

    def __init__(self, device, interface=None):
        """SmartGadget is a class that establishes a connection between a RPI and a Sensirion Smart Gadget. 
           device : str
             MAC address of Sensor.
           interface : int or None
             bluetooth interface on which to make the connection
        """

        self.device = device
        self.interface = interface

        super(SmartGadget, self).__init__()
        self.establish_connection()
        #super(SmartGadget, self).__init__(deviceAddr=device, addrType='random', iface=interface)

    def establish_connection(self):
        for x in range (3):
            try:
                self.connect(self.device, addrType='random', iface=self.interface)
                return
            except BTLEDisconnectError:
                print("Device not available to connect, please check battery and bluetooth")
                time.sleep(10)
            except BrokenPipeError:
                print("Lost connection, please check connection")


    def temp_reading(self):
        handle = 0x0037
        temp_hnd_char = self.get_reading(handle)
        upkd_bts = struct.unpack('<f',temp_hnd_char)
        return upkd_bts[0]

    def hum_reading(self):
        handle = 0x0032
        hum_hand_char = self.get_reading(handle)
        upkd_bts = struct.unpack('<f',hum_hand_char)
        return upkd_bts[0]

    def battery_percent(self):
        handle = 0x001d
        batt_hand_char = self.get_reading(handle)
        upkd_bts = struct.unpack('<B', batt_hand_char)
        return float(upkd_bts[0])

    def get_reading(self, handle):

        try:
            return self.readCharacteristic(handle)
        except BrokenPipeError:
            print("BrokenPipeError")
        except BTLEDisconnectError:
            print("Device not available to connect, please check battery and bluetooth")
            self.establish_connection()
            return self.readCharacteristic(handle)

if __name__ == "__main__":
    A2_device = 'F8:70:C7:E1:BB:A2'

    A2_SG = SmartGadget(A2_device)

    while True:
        print(A2_SG.battery_percent())
        A2_SG.hum_reading()
        time.sleep(5)
#A2_SG.battery_percent()