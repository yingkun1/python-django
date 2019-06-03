import memcache

#在连接之前，一定要切记先启动memcached
mc = memcache.Client(["127.0.0.1:11211","192.168.0.112"],debug=True)

#将数据存储到memcached当中
# mc.set('username','abc',time=120)
# mc.set_multi({'title':'钢铁是怎样炼成的','content':'Hello World'},time=120)

#从memcached中取出数据
# username = mc.get('username')
# print(username)

#从memcached中删除数据
# mc.delete('username')

# username = mc.get('username')
# print(username)

#自增长
# mc.incr('age')
# print(mc.get('age'))

#自减
# mc.decr('age',delta=20)
# print(mc.get('age'))

mc.set_multi({'username':'zhiliao','age':18,'height':180,'weight':180})

