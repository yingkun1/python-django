from redis import Redis

cache = Redis(host='127.0.0.1',port=6379,password='yingkun9257')

for x in range(3):
    cache.publish('email','xxx@qq.com')