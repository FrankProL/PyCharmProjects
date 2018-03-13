# encoding: utf-8
def load_data_set2():
    """
    加载数据
    """
    f=open("user_room_month.txt")
    lines =f.readlines()
    i=0
    data = {}

    for line in lines:
        line=line.strip('\n')
        user=line.split("\t")
        transcations = set()
        transcations.add(user[2])
        dayitem='%s%s%s' % (user[0], '_', user[1])
        if data.has_key(dayitem):
            data[dayitem].add(user[2])
        else:
            data[dayitem]=transcations
            i+=1
    data_set=[]
    for key in sorted(data.keys()):
        # print key,
        # print '--->',
        # print list(data[key])
        if len(data[key])>1:
            # print key,'--->',list(data[key])
            data_set.append(list(data[key]))
    # print data_set
    print i
    f.close()
    return data_set

if __name__ == '__main__':
	print load_data_set2()
    # print t