import redis

def save_key_value_pair(dict):
    redis_client = redis.Redis(host='172.214.74.29', port=6379, db=0)

    for key in dict:
        redis_client.set(key,dict[key])
        