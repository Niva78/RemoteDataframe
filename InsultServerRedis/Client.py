import redis
import pandas as dataframe
import json

redis_cli = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True, encoding="utf-8")
redis_cli.set("version", "v1.0")
print("The version is: " + str(redis_cli.get("version")))

product_stock = {"pid" : 123, "in_stock" : False}
redis_cli.set("product_stock", json.dumps(product_stock))
print("The info we got was: " + str(redis_cli.get("product_stock")))

print("Operation result: " + str(redis_cli.delete("version")))


redis_cli.set("student:john", '{"score": 90, "bonus": 10}')

redis_cli.set("student:tom", '{"score": 80, "bonus": 5}')

for key in redis_cli.scan_iter("student:*"):
    print("The student: ", key , " got:", str(redis_cli.get(key)))