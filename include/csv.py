import os

def get_filename():
    i = 1
    while True:
        file_name = f"output/output{i}.csv"
        if not os.path.exists(file_name):
            return file_name
        i += 1

def file(res, file_name):
    with open(file_name, "a") as f:
        f.write(f"{res}\n")