class Test(object):
    def __init__(self):
        self.name = 'testname_yingkun'

    def foo(self,name):
        self.name = name

if __name__ == '__main__':
    eval_test = eval('Test()')
    # print(type(eval_test))
    # print(eval_test)
    # print('old name is:%s'%eval_test.name)
    func = getattr(eval_test,'foo')
    # print(func)
    func('new_name')
    print('new name is:%s'%eval_test.name)