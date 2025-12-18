import os

for i in range (2, 10):
    filename = f"output/output{i}.csv"
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename}")