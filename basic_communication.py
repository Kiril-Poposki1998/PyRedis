import redis

r = redis.Redis(host="localhost", port=6379)

capitals = {"Germany": "Berlin", "France": "Paris", "U.K.": "London"}

for (key, value) in capitals.items():
    r.set(key, value)

for country in capitals.keys():
    print("The capital of {} is {}".format(country, r.get(country).decode()))
