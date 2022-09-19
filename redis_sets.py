import redis

r = redis.Redis(host="localhost", port=6379)

country_capitals = dict()

for i in range(3):
    country = input("Enter a country: ")
    capital = input("Enter a capital city: ")
    country_capitals.update({country: capital})
    print("Country and capital city added to redis")

r.mset(country_capitals)

print("testing if they are stored")
for key in country_capitals.keys():
    print(r.get(key).decode())
