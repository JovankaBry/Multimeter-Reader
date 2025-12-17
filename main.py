from include.imports import *

ser = open_serial()   # Opening serial from serials.py

print("Identification :", query(ser, "*IDN?"))

mode = "r"

print("Press 'v' for Voltage, 'r' for Resistance")
print("\nSTRG + C to stop measuring!")

ser.write(b"*CLS\r\n")
time.sleep(0.2)

ser.write(b"SYST:REM\r\n")
time.sleep(0.2)

file_name = get_filename()
print("Logging to: ", file_name)

try:
    while True:
        key = get_key()
        if key:
            key = key.lower()
            if key == "v":
                mode = "v"
                print("\nSwitched to VOLTAGE")
            elif key == "r":
                mode = "r"
                print("\nSwitched to RESISTANCE")

        if mode == "v":
            value = voltage(ser)
            print("Voltage (V):", value)
        else:
            value = resistance(ser)
            print("Resistance (Ohm):", value)

        file(value, file_name)
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nTest stopped by user")
#print("ERR :", query(ser, "SYST:ERR?")) ##Error Check