import serial
import time

PORT = "/dev/ttyUSB0"

def query(ser, cmd, wait=0.3):
    ser.write((cmd + "\r\n").encode("ascii"))
    time.sleep(wait)
    return ser.readline().decode(errors="ignore").strip()


with serial.Serial(
    PORT, 9600,
    timeout=2,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    xonxoff=True, rtscts=False, dsrdtr=False
) as ser:


    print("IDN :", query(ser, "*IDN?"))

    ser.write(b"*CLS\r\n")
    time.sleep(0.2)

    ser.write(b"SYST:REM\r\n")
    time.sleep(0.2)

    ser.write(b"CONF:CURR:DC\r\n")
    time.sleep(0.2)

    res = float(query(ser, "READ?", wait=0.6))
    print("Current (A): ", res)

   #print("ERR :", query(ser, "SYST:ERR?")) ##Error Check