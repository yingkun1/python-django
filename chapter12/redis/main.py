from redis import Redis

cache = Redis(host="127.0.0.1",port=6379,password="yingkun9257")

#1.操作字符串
# cache.set('username','abcx')
# print(cache.get('username'))
# cache.delete('username')
# print(cache.get('username'))

#2.列表的操作
# cache.lpush('languages','java'),
# cache.lpush('languages','python'),
# cache.lpush('languages','php'),
# print(cache.lrange('languages',0,-1))

#3.集合的操作
# cache.sadd('team','li')
# cache.sadd('team','zhang')
# cache.sadd('team','huang')
# print(cache.smembers('team'))

#4.hash的操作
# cache.hset('websites','baidu','www.baidu.com')
# cache.hset('websites','google','www.google.com')
# print(cache.hgetall('websites'))

#5.事务的操作
# pip = cache.pipeline()
# pip.set('username','zhiliao')
# pip.set('password','111111')
# pip.execute()

#6.发布与订阅，异步发送邮件的功能
ps = cache.pubsub()
ps.subscribe('email')
while True:
    for item in ps.listen():                 #注意：ps.listen()返回的是一个生成器
        if item['type'] == 'message':
            data = item['data']
            print(data)
