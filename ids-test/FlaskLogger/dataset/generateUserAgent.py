import fake_useragent

with open("user_agents.txt", "w") as f:
    for i in range(10000):
        ua = fake_useragent.UserAgent()
        user_agent = ua.random
        f.write(user_agent + "\n")