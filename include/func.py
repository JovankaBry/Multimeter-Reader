import time

def query (ser, cmd, wait=1):
    ser.write((cmd + "\r\n").encode("ascii"))
    time.sleep(wait)
    return ser.readline().decode(errors="ignore").strip()

def resistance(ser):
    ser.write(b"CONF:RES\r\n")
    time.sleep(0.2)
    res = float(query(ser,"READ?"))
    print("Resistance: ", res ,'\u03A9')
    return res

def voltage(ser):
    ser.write(b"CONF:VOLT:DC\r\n")
    time.sleep(0.2)
    volt = float(query(ser,"READ?"))
    print("Voltage: ", volt , 'V')
    return volt

def current(ser):
    ser.write(b"CONF:CURR:DC\r\n")
    time.sleep(0.2)
    cur = float(query(ser, "READ?"))
    print("Current: ", cur, 'A')
    return cur