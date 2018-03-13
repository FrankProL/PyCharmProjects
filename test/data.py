# encoding: utf-8
# f=open("0129.txt")
f = open("../suggest/user_room_month.txt")
lines =f.readlines()
i=0
data = {}

for line in lines:
    line=line.strip('\n')
    user=line.split("\t")
    # print user[0]
    # print user[1]
    transcations = []
    transcations.append(user[2])
    if data.has_key(user[0]):
        data[user[0]].append(user[2])
    else:
        data[user[0]]=transcations
        i+=1
#data_set=[]
for key in sorted(data.keys()):
    # print key,
    # print '--->',
    # print list(data[key])
    # if len(data[key])>1:
    print data[key]


    #data_set.append(list(data[key]))
#print data_set


f.close()
