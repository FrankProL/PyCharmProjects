#!/usr/bin/env python
# encoding: utf-8

#rows = int(raw_input('输入列数：'))
rows = 4
i=j=k=1
for i in range(0,rows):
    for j in range(0,rows-i): 
    	print " * ",
    	j=j+1
    i = i+1
    print "\n"

i=j=1
for i in range(0,rows):
	for j in range(0,rows):
		print " * ",
	print '\n'

i=j=1
for i in range(0,rows):
    for j in range(0,rows):
    	if i!=0 and i!=rows-1:
    		if j==0 or j==rows-1:
    			print ' * ',
    		else: print '   ',
    	else: print ' * ',
    print '\n'

print "打印空心等边三角形，这里去掉if-else条件判断就是实心的"
for i in range(0, rows + 1):#变量i控制行数
    for j in range(0, rows - i):#(1,rows-i)
        print " ",
        #j += 1
    for k in range(0, 2 * i - 1):#(1,2*i)
        if k == 0 or k == 2 * i - 2 or i == rows:
            if i == rows:
                if k % 2 == 0:#因为第一个数是从0开始的，所以要是偶数打印*，奇数打印空格
                    print "*",
                else:
                    print " ", #注意这里的","，一定不能省略，可以起到不换行的作用
            else:
               print "*",
        else:
            print " ",
        #k += 1
    print "\n"
    #i += 1