import redis
from time import sleep

r = redis.Redis(host="localhost")

r.psetex("Germany",10000,"Berlin")

print(r.get("Germany").decode())

sleep(10)

if r.get("Germany") is None:
    print("The capital of germany is not in redis anymore")