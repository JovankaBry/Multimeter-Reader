import time

def query (ser, cmd, wait=1):
    ser.write((cmd + "\r\n").encode("ascii"))
    time.sleep(wait)
    return ser.readline().decode(errors="ignore").strip()

def resistance(ser):
    ser.write(b"CONF:RES\r\n")
    time.sleep(0.2)
    res = float(query(ser,"READ?"))
    print("Resistance (Ohm): ", res)
    return res

def voltage(ser):
    ser.write(b"CONF:VOLT:DC\r\n")
    time.sleep(0.2)
    volt = float(query(ser,"READ?"))
    print("Voltage(V): ", volt)
    return volt