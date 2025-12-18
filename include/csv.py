import os
from datetime import datetime

def get_filename():
    i = 1
    while True:
        file_name = f"output/output{i}.csv"
        if not os.path.exists(file_name):
            return file_name
        i += 1

def file(res, unit, file_name):
    timestamp = datetime.now().strftime("%d.%m.%y %H:%M:%S")
    with open(file_name, "a") as f:
        value_str = f"{res:.6f}".replace(".", ",")
        f.write(f"{value_str};{unit};{timestamp}\n")