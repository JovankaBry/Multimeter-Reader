from include.imports import *

ser = open_serial()   # Opening serial from serials.py

print("Identification :", query(ser, "*IDN?"))
print("\nSTRG + C to stop measuring!")

ser.write(b"*CLS\r\n")
time.sleep(0.2)

ser.write(b"SYST:REM\r\n")
time.sleep(0.2)

file_name = get_filename()
print("Logging to: ", file_name)

try:     
    while True:
        res = resistance(ser)
        file(res, file_name)
        time.sleep(1)
        #voltage()
    
except KeyboardInterrupt:
    print("\nTest stopped by user")
#print("ERR :", query(ser, "SYST:ERR?")) ##Error Check