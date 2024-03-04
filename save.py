import redis

def save_key_value_pair(dict):
    redis_client = redis.Redis(host='localhost',port=6379)

    for key in dict:
        redis_client.set(key,dict[key])
        