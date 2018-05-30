# encoding:utf-8
print '你好，hello'

def fun1():
    print 'fun1'

def fun2():
    print 'fun2'

def fun99():
    for i in range(1,9):
        for j in range(1,i):
            print (i*j)
        print('\n')

if __name__== '__main__':
    fun1()
    print 'hello test'
    a,b=1,3
    print a
    print b
    print a,'+',b
    fun99()