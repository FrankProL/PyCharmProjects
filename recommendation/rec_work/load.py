# encoding: utf-8
f=open("user_room.txt")
lines =f.readlines()
i=0
data = {}

for line in lines:
    line=line.strip('\n')
    user=line.split("\t")
    # print user[0]
    # print user[1]
    transcations = set()
    transcations.add(user[1])
    if data.has_key(user[0]):
        data[user[0]].add(user[1])
    else:
        data[user[0]]=transcations
        i+=1
data_set=[]
for key in sorted(data.keys()):
    # print key,
    # print '--->',
    # print list(data[key])
    # if len(data[key])>1:
    print key,'--->',list(data[key])
    data_set.append(list(data[key]))
print data_set

print i
f.close()
