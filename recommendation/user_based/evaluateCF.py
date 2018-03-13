# coding=utf-8
import pprint, pickle


# 获取推荐列表
def getRecom():
    pkl_file = open('./Recom/recommendationList5.pkl', 'rb')
    recomList = pickle.load(pkl_file)
    # pprint.pprint(recomList)
    pkl_file.close()
    return recomList


def load_data():
    filename_user_movie = './ml-100k/u5.test'

    user_movie = {}
    for line in open(filename_user_movie):
        # 原文件格式 user id | item id | rating | timestamp，
        # The time stamps are unix seconds since 1/1/1970 UTC
        (userId, itemId, rating, timestamp) = line.strip().split('\t')
        user_movie.setdefault(userId, [])
        user_movie[userId].append(itemId)

    return user_movie


# 计算准确率precision,对于某一用户u，其推荐准确率为系统推荐的L个商品中用户喜欢的商品所占的比例,
# 这里每个用户推荐列表的长度为10
def calPrecision(recom, user_movie):
    precisionForUser = {}  # 存储每个用户的准确率
    for key in recom:
        hit_Num = 0
        if user_movie.has_key(key):
            for i in range(10):  # 这里的10是因为simpleCF.py文件里面设置的是top-10推荐
                item = recom[key][i][0]
                if item in user_movie[key]:
                    # 如果用户u的推荐列表中每有一个movie 在 u1.test中用户u的记录中出现，
                    # 那么用户u的hit_Num+1，
                    hit_Num += 1
            precisionForUser[key] = hit_Num * 1.0 / 10
    Precision = sum(precisionForUser.values()) * 1.0 / len(precisionForUser)
    # 将系统中所有用户的准确率求平均得到系统整体的推荐准确率
    return Precision


# 计算召回率recall,用户u推荐命中的电影数量与测试集中用户看过的电影数量的比，
# 命中是指同时在用户u的推荐列表和测试集中u看过的电影列表中出现，
def calRecall(recom, user_movie):
    recallForUser = {}  # 存储每个用户的准确率
    for key in recom:
        hit_Num = 0
        # 首先判断推荐列表中的每一个用户是否在测试集得到的字典user_movie中，
        # 在里面的才能计算准确率和召回率，没在的跳过
        if user_movie.has_key(key):
            for i in range(10):  # 这里的10是因为simpleCF.py文件里面设置的是top-10推荐
                item = recom[key][i][0]
                if item in user_movie[key]:
                    # 如果用户u的推荐列表中每有一个movie 在 u1.test中用户u的记录中出现，
                    # 那么用户u的hit_Num+1，
                    hit_Num += 1
            recallForUser[key] = hit_Num * 1.0 / len(user_movie[key])
    Recall = sum(recallForUser.values()) * 1.0 / len(recallForUser)
    # 将系统中所有用户的召回率求平均得到系统整体的推荐召回率
    return Recall


if __name__ == "__main__":
    recom = getRecom()
    user_movie = load_data()
    precision = calPrecision(recom, user_movie)
    recall = calRecall(recom, user_movie)
    print ' 该推荐算法准确率为: %s,  召回率为: %s' % (precision, recall)
