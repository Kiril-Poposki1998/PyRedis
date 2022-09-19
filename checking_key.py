import redis

r = redis.Redis(host="localhost")

if r.exists("Spain"):
    print("Spain's capital is "+r.get("Spain").decode())
elif r.exists("Germany"):
    print("Germany's capital is "+r.get("Germany").decode())
else:
    print("Spain's and Germany's capital is not in redis")

