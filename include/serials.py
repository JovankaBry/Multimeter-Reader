import serial

PORT = "/dev/ttyUSB0"

def open_serial():
    ser = serial.Serial(
        PORT,
        9600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        xonxoff=True,
        rtscts=False,
        dsrdtr=False
)
    return ser