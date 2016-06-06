import time
import serial
from threading import Thread


class SerialData(object):
    def __init__(self, receiving, last_received, init=50):
        try:
            self.receiving = receiving
            self.last_received = last_received
            self.serial_connection = serial.Serial(
                    port='/dev/cu.usbmodem1421', baudrate=9600,
                    bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, timeout=0.1, xonxoff=0,
                    rtscts=0, interCharTimeout=None)

        except serial.serialutil.SerialException:
            # no serial connection
            self.ser = None

        else:
            thread = Thread(target=self.receiving, args=(self.ser,))
            thread.daemon = True
            thread.start()

    def next(self):
        if not self.ser:
            return -1000  # return so we can test when Arduino isn't connected
        # return a float value or try a few times until we get one
        for i in range(40):
            raw_line = self.last_received
            try:
                return float(raw_line.strip())
            except ValueError:
                time.sleep(.005)
        return 0

    def __del__(self):
        if self.serial_connection:
            self.serial_connection.close()
