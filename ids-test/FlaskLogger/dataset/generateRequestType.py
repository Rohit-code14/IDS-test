import random

with open("request_types.txt", "w") as f:
    for i in range(10000):
        rand_num = random.uniform(0, 1)
        if rand_num < 0.65:
            request_type = "POST"
        elif rand_num < 0.9:
            request_type = "GET"
        elif rand_num < 0.93:
            request_type = "DELETE"
        elif rand_num < 0.96:
            request_type = "PUT"
        elif rand_num < 0.99:
            request_type = "OPTIONS"
        else:
            request_type = "CONNECT"
        f.write(request_type + "\n")
