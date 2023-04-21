import random
import string

with open("accept_mimetypes.txt", "w") as f:
    for i in range(10000):
        num_types = random.randint(1, 4)  # choose a random number of mime types
        types = random.sample(['text/html', 'text/plain', 'application/json', 'image/jpeg', 'image/png'], num_types)
        accept_header = ', '.join(types) + ', */*'
        f.write(accept_header + "\n")
