# encoding:utf-8
print ('你好，hello')

def fun1():
    print ('fun1')

def fun2():
    print ('fun2')

def fun99():
    for i in range(1,9+1):
        for j in range(1,i+1):
            print j,'*',i,'=',i*j,'  ',
        print('\n')
import sys
if __name__== '__main__':
    print("脚本参数："),
    print(sys.argv[0:])
    input=raw_input("请输入：")
    print("输入内容："+input)
    fun1()
    print ('hello test')
    a,b=1,3
    print (a,b)
    print(a,'+',b)  #python2中输出元组，python3中print()是个函数 输出a+b
    fun99()