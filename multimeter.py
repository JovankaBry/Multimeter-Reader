import serial
import time

class HP34401A:
    def __init__(self, port="/dev/ttyUSB0"):
        self.ser = serial.Serial(
            port,
            9600,
            timeout=2,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            xonxoff=True,
            rtscts=False,
            dsrdtr=False
        )

        # clear errors and go to remote
        self.ser.write(b"*CLS\r\n")
        time.sleep(0.2)
        self.ser.write(b"SYST:REM\r\n")
        time.sleep(0.2)

    def query(self, cmd, wait=0.3):
        self.ser.write((cmd + "\r\n").encode("ascii"))
        time.sleep(wait)
        return self.ser.readline().decode(errors="ignore").strip()

    def voltage_dc(self):
        self.ser.write(b"CONF:VOLT:DC\r\n")
        time.sleep(0.2)
        return float (self.query("READ?", wait=0.6))

    def current_dc(self):
        self.ser.write(b"CONF:CURR:DC\r\n")
        time.sleep(0.2)
        return float (self.query("READ?", wait=0.6))

    def resistance(self):
        self.ser.write(b"CONF:RES\r\n")
        time.sleep(0.2)
        return float (self.query("READ?", wait=0.6))

    def close(self):
        self.ser.close()

dmm = HP34401A("/dev/ttyUSB0")

print("Voltage (V):", dmm.voltage_dc())
print("Current (A):", dmm.current_dc())
print("Resistance (Ohm):", dmm.resistance())

dmm.close()