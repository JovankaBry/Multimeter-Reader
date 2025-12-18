import os
from .func import timestamp

def get_filename():
    i = 1
    while True:
        file_name = f"output/output{i}.csv"
        if not os.path.exists(file_name):
            return file_name
        i += 1

def file(res, unit, file_name):
    date = timestamp()
    with open(file_name, "a") as f:
        value_str = f"{res:.6f}".replace(".", ",")
        f.write(f"{value_str};{unit};{date}\n")