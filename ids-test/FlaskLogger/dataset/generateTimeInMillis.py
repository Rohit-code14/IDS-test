import random

with open("time_in_millis.txt", "w") as f:
    for i in range(10000):
        time_in_millis = random.randint(0, 2**63-1)
        f.write(str(time_in_millis) + "\n")
