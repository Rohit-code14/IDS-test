with open("xsspayload.txt", "w") as f:
    for i in range(10000):
        f.write(str("false") + "\n")
