import random

with open("content_lengths.txt", "w") as f:
    for i in range(10000):
        content_length = random.randint(1, 100000)
        f.write(str(content_length) + "\n")
