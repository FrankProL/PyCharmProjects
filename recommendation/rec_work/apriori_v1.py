# encoding: utf-8
def load_data_set():
    """
    加载数据
    uid,roomid
    原数据集648
    20180110用户数509
    处理后数据集509 {uid,set(roomid)}
    """
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
        if len(data[key])>1:
            # print key,'--->',list(data[key])
            data_set.append(list(data[key]))
    # print data_set
    print (i)
    print (len)
    f.close()
    return data_set

def load_data_set2():
    """
    加载数据
    月数据，day--uid--roomid    28780
    返回所有用户每天对应的roomid集合的集合
    12月用户数 10665
    处理后数据集21985 {day_uid,set(roomid)}
    """
    # f=open("user_room_month.txt")
    f=open("user_room_3days.txt")   # 原数据集2356，处理后1922, 3天用户数1626
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
    print (i)
    print len(data)         #每个用户每日的set(roomid)的集合
    f.close()
    return data_set

def create_C1(data_set):
    """
    扫描数据集，创建候选频繁一项集C1
    Args:
        data_set: 数据集list，每条数据包含若roomid
    Returns:
        C1: set 包含所有的roomid
    """
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1


def is_apriori(Ck_item, Lksub1):
    """
    Judge whether a frequent candidate k-itemset satisfy Apriori property.
    Args:
        Ck_item: a frequent candidate k-itemset in Ck which contains all frequent
                 candidate k-itemsets.
        Lksub1: Lk-1, a set which contains all frequent candidate (k-1)-itemsets.
    Returns:
        True: satisfying Apriori property.
        False: Not satisfying Apriori property.
    """
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lksub1:
            return False
    return True


def create_Ck(Lksub1, k):
    """
    Create Ck, a set which contains all all frequent candidate k-itemsets
    by Lk-1's own connection operation.
    Args:
        Lksub1: Lk-1, a set which contains all frequent candidate (k-1)-itemsets.
        k: the item number of a frequent itemset.
    Return:
        Ck: a set which contains all all frequent candidate k-itemsets.
    """
    Ck = set()
    len_Lksub1 = len(Lksub1)
    list_Lksub1 = list(Lksub1)
    for i in range(len_Lksub1):
        for j in range(1, len_Lksub1):
            l1 = list(list_Lksub1[i])
            l2 = list(list_Lksub1[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:
                Ck_item = list_Lksub1[i] | list_Lksub1[j]
                # pruning
                if is_apriori(Ck_item, Lksub1):
                    Ck.add(Ck_item)
    return Ck


def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):
    """
    Generate Lk by executing a delete policy from Ck.
    Args:
        data_set: A list of transactions. Each transaction contains several items.
        Ck: A set which contains all all frequent candidate k-itemsets.
        min_support: The minimum support.
        support_data: A dictionary. The key is frequent itemset and the value is support.
    Returns:
        Lk: A set which contains all all frequent k-itemsets.
    """
    Lk = set()
    item_count = {}
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk


def generate_L(data_set, k, min_support):
    """
    Generate all frequent itemsets.
    Args:
        data_set: A list of transactions. Each transaction contains several items.
        k: Maximum number of items for all frequent itemsets.
        min_support: The minimum support.
    Returns:
        L: The list of Lk.
        support_data: A dictionary. The key is frequent itemset and the value is support.
    """
    support_data = {}
    C1 = create_C1(data_set)
    L1 = generate_Lk_by_Ck(data_set, C1, min_support, support_data)
    Lksub1 = L1.copy()
    L = []
    L.append(Lksub1)
    for i in range(2, k+1):
        Ci = create_Ck(Lksub1, i)
        Li = generate_Lk_by_Ck(data_set, Ci, min_support, support_data)
        Lksub1 = Li.copy()
        L.append(Lksub1)
    return L, support_data


def generate_big_rules(L, support_data, min_conf):
    """
    Generate big rules from frequent itemsets.
    Args:
        L: The list of Lk.
        support_data: A dictionary. The key is frequent itemset and the value is support.
        min_conf: Minimal confidence.
    Returns:
        big_rule_list: A list which contains all big rules. Each big rule is represented
                       as a 3-tuple.
    """
    big_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    conf = support_data[freq_set] / support_data[freq_set - sub_set]
                    big_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and big_rule not in big_rule_list:
                        # print freq_set-sub_set, " => ", sub_set, "conf: ", conf
                        big_rule_list.append(big_rule)
            sub_set_list.append(freq_set)
    return big_rule_list


if __name__ == "__main__":
    """
    Test
    """
    data_set = load_data_set()
    L, support_data = generate_L(data_set, k=3, min_support=0.02)
    big_rules_list = generate_big_rules(L, support_data, min_conf=0.5)
    for Lk in L:
        print "="*50
        # print list(Lk)
        print "frequent " + str(len(list(Lk)[0])) + "-itemsets\t\tsupport"
        print "="*50
        for freq_set in Lk:
            print freq_set, support_data[freq_set]
    print
    print "Big Rules"
    for item in big_rules_list:
        print item[0], "=>", item[1], "conf: ", item[2]
