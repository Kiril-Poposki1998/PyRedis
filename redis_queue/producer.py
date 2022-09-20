import random
import redis

with redis.Redis() as r:
    for i in range(10):
        integer = random.randint(0, 100)
        print(integer)
        r.lpush("queue", integer)