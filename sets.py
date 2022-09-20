import redis

with redis.Redis() as r:
    r.sadd("cloud_providers_a", "AWS", "GCP", "Azure")
    r.sadd("cloud_providers_b", "Digital Ocean", "Linode")
    r.sunionstore("cloud_providers", "cloud_providers_a", "cloud_providers_b")
    members = [i.decode() for i in r.smembers("cloud_providers")]
    for x in members:
        print(x)