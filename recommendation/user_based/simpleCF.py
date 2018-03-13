# coding=utf-8
"""
http://blog.csdn.net/u010454636/article/details/51842160
基于用户的协同过滤（user-based CF）推荐系统
top-10推荐，也就是为每个用户推荐了10部电影
"""
from operator import itemgetter, attrgetter
from math import sqrt
import pickle


def load_data():
    filename_user_movie = './ml-100k/u5.base'
    filename_movieInfo = './ml-100k/u.item'

    user_movie = {}
    for line in open(filename_user_movie):
        # 原文件格式 user id | item id | rating | timestamp，
        # The time stamps are unix seconds since 1/1/1970 UTC
        (userId, itemId, rating, timestamp) = line.strip().split('\t')
        user_movie.setdefault(userId, {})
        user_movie[userId][itemId] = float(rating)

    movies = {}
    for line in open(filename_movieInfo):
        # u.item 文件格式：movie id | movie title | release date | video release date |IMDb URL |
        # unknown | Action | Adventure | Animation |Children's | Comedy | Crime | Documentary | Drama | Fantasy |
        #  Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western |
        # 最后19个是该电影的体裁，一部电影一次可以有几种体裁，取值为1和0.
        # 1表示是，0表示否
        (movieId, movieTitle) = line.split('|')[0:2]
        movies[movieId] = movieTitle

    return user_movie, movies


# 求一个用户所有评分的平均分
def average_rating(user):
    average = 0
    for u in user_movie[user].keys():
        average += user_movie[user][u]
    average = average * 1.0 / len(user_movie[user].keys())
    return average


def calUserSim(user_movie):
    # build inverse table for movie_user
    movie_user = {}  # 建立倒排表
    for ukey in user_movie.keys():
        for mkey in user_movie[ukey].keys():
            if mkey not in movie_user:
                movie_user[mkey] = []
            movie_user[mkey].append(ukey)

    # calculated co-rated movies between users
    # 最终C形如{u:{n1:[movie1,movie2],n2:[movie2,movie4]},...}  存储的是用户间共同看过的电影的集合
    C = {}
    for movie, users in movie_user.items():  # dict.items()返回返回字典的(键，值)元组对的列表
        for u in users:
            C.setdefault(u, {})
            for n in users:
                if u == n:
                    continue
                C[u].setdefault(n, [])
                C[u][n].append(movie)

    # calculate user similarity (perason correlation)
    userSim = {}
    for u in C.keys():  # 所有的用户
        for n in C[u].keys():  # 共同看过同一部电影的用户
            userSim.setdefault(u, {})
            userSim[u].setdefault(n, 0)

            average_u_rate = average_rating(u)
            average_n_rate = average_rating(n)

            part1 = 0
            part2 = 0
            part3 = 0
            for m in C[u][n]:  # C[u][n]中是用户u和n共同看过的电影, 采用皮尔逊相关系数计算相似性


                part1 += (user_movie[u][m] - average_u_rate) * (user_movie[n][m] - average_n_rate) * 1.0
                part2 += pow(user_movie[u][m] - average_u_rate, 2) * 1.0
                part3 += pow(user_movie[n][m] - average_n_rate, 2) * 1.0

            part2 = sqrt(part2)
            part3 = sqrt(part3)
            if part2 == 0:
                part2 = 0.001
            if part3 == 0:
                part3 = 0.001
            userSim[u][n] = part1 / (part2 * part3)
    return userSim
    # userSim looks like {u:{n:sim,...},...},这里只是根据有共同记录的计算出来的那部分，
    # 如果没有共同记录的，那部分用户相似度怎么处理没说


def getRecommendations(user, user_movie, userSim, N):  # N个最相似的用户
    pred = {}
    interacted_items = user_movie[user].keys()  # user看过的movie集合
    average_u_rate = average_rating(user)  # user的平均分
    sumUserSim = 0
    for n, nuw in sorted(userSim[user].items(), key=itemgetter(1), reverse=True)[0:N]:
        # 取前N个和用户user最相似的（用户：相似度）集合
        average_n_rate = average_rating(n)  # 用户n的平均分
        for i, nrating in user_movie[n].items():  # 用户n看过电影集合及评分
            # filter movies user interacted before
            if i in interacted_items:
                continue
            pred.setdefault(i, 0)
            pred[i] += nuw * (nrating - average_n_rate)
        sumUserSim += nuw

    for i, rating in pred.items():
        pred[i] = average_u_rate + (pred[i] * 1.0) / sumUserSim

    # top-10 pred recommendation
    pred = sorted(pred.items(), key=itemgetter(1), reverse=True)[0:10]
    # 最终pored的形式形如[('movie', rating), ...]
    return pred


if __name__ == "__main__":
    j = 0
    # load data
    user_movie, movies = load_data()

    # Calculate user similarity
    userSim = calUserSim(user_movie)

    recomList = {}
    # Recommend
    for user in user_movie.keys():
        pred = getRecommendations(user, user_movie, userSim, 20)
        recomList[user] = pred

        # display recommend result (top-10 results)
        for i, rating in pred:
            print (' user: %s,  film: %s,  rating: %s' % (user, movies[i], rating))
            j += 1
    print ("总共生成", j, "次推荐。")
    print (len(recomList))
    print (recomList['1'])
    output = open('./Recom/recommendationList5.pkl', 'wb')

    # Pickle dictionary using protocol 0.
    pickle.dump(recomList, output)
    output.close()
