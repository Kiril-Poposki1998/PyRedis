import redis

with redis.Redis() as r:
    q_len = r.llen("queue")
    for i in range(q_len):
        print("Random number generated from producer is ",r.rpop("queue").decode())