# encoding:utf-8

# http://blog.csdn.net/buracag_mc/article/details/70143833
# 从http://grouplens.org/datasets/movielens/下载数据集100K(ml-100K.ZIP)
# u.data，第一列为用户ID，第二列为电影ID，第三列为评分，第四列为时间戳
# u.item文中包括电影ID、标题、上映时间和IMDB链接

import os
import csv
import heapq
from operator import itemgetter
from datetime import datetime
from collections import defaultdict
from math import sqrt


def load_reviews(path, **kwargs):
    '''''
    加载电影数据文件
    '''
    options = {
        'fieldnames': ('userid', 'movieid', 'rating', 'timestamp'),
        'delimiter': '\t'
    }

    options.update(kwargs)
    parse_date = lambda r, k: datetime.fromtimestamp(float(r[k]))
    parse_int = lambda r, k: int(r[k])

    with open(path, 'rb') as reviews:
        reader = csv.DictReader(reviews, **options)
        for row in reader:
            row['movieid'] = parse_int(row, 'movieid')
            row['userid'] = parse_int(row, 'userid')
            row['rating'] = parse_int(row, 'rating')
            row['timestamp'] = parse_date(row, 'timestamp')
            yield row


def relative_path(path):
    '''''
    辅助数据导入
    '''
    dirname = os.path.dirname(os.path.realpath('__file__'))
    path = os.path.join(dirname, path)
    return os.path.normpath(path)


def load_movies(path, **kwargs):
    '''''
    读取电影信息
    '''
    options = {
        'fieldnames': ('movieid', 'title', 'release', 'video', 'url'),
        'delimiter': '|',
        'restkey': 'genre'
    }
    options.update(**kwargs)

    parse_int = lambda r, k: int(r[k])
    parse_date = lambda r, k: datetime.strptime(r[k], '%d-%b-%Y') if r[k] else None

    with open(path, 'rb') as movies:
        reader = csv.DictReader(movies, **options)
        for row in reader:
            row['movieid'] = parse_int(row, 'movieid')
            # print row['movieid']
            row['release'] = parse_date(row, 'release')
            # print row['release']
            # print row['video']
            yield row


class MovieLens(object):
    def __init__(self, udata, uitem):
        self.udata = udata
        self.uitem = uitem
        self.movies = {}
        self.reviews = defaultdict(dict)
        self.load_dataset()

    def load_dataset(self):
        # 加载数据到内存中，按ID为索引
        for movie in load_movies(self.uitem):
            self.movies[movie['movieid']] = movie

        for review in load_reviews(self.udata):
            self.reviews[review['userid']][review['movieid']] = review
            # print self.reviews[review['userid']][review['movieid']]
            # 寻找高评分电影

    # 遍历所有评分字典中的值（通过userid进行索引），并检查用户是否对当前的movieid进行过评分，如存在，则将评分结果返回
    def reviews_for_movie(self, movieid):
        for review in self.reviews.values():
            if movieid in review:  # 存在则返回
                yield review[movieid]

    def average_reviews(self):
        # 返回电影ID、平均得分以及评分的个数
        for movieid in self.movies:
            reviews = list(r['rating'] for r in self.reviews_for_movie(movieid))
            average = sum(reviews) / float(len(reviews))
            yield (movieid, average, len(reviews))  # 返回了（movieid，评分平均分，长度(即评价人数)）

    def top_rated(self, n=10):
        # 返回一个前n的top排行 ,利用heapq对结果根据平均分进行排序
        return heapq.nlargest(n, self.bayesian_average(), key=itemgetter(1))

        # C是我们通过

    # C = float(sum(num for mid, avg, num in model.average_reviews())) / len(model.movies)得到的，这里直接给出m为3，C为59
    def bayesian_average(self, c=59, m=3):
        # 返回一个修正后的贝叶斯平均值
        for movieid in self.movies:
            reviews = list(r['rating'] for r in self.reviews_for_movie(movieid))
            average = ((c * m) + sum(reviews)) / float(c + len(reviews))
            yield (movieid, average, len(reviews))

            # 计算用户在偏好空间中的距离

    # 利用欧式距离来构建
    def share_preferences(self, criticA, criticB):
        # 找出两个评论者之间的交集
        if criticA not in self.reviews:
            raise KeyError("Couldn't find critic '%s' in data " % criticA)
        if criticB not in self.reviews:
            raise KeyError("Couldn't find critic '%s' in data " % criticB)
        moviesA = set(self.reviews[criticA].keys())
        moviesB = set(self.reviews[criticB].keys())
        shared = moviesA & moviesB
        # 创建一个评论过的的字典返回
        reviews = {}
        for movieid in shared:
            reviews[movieid] = (
                self.reviews[criticA][movieid]['rating'],
                self.reviews[criticB][movieid]['rating'],
            )
        return reviews

    def euclidean_distance(self, criticA, criticB, prefs='users'):
        # 通过两个人的共同偏好作为向量来计算两个用户之间的欧式距离
        # 创建两个用户的交集
        preferences = self.share_preferences(criticA, criticB)
        # 没有则返回0
        if len(preferences) == 0: return 0
        # 求偏差的平方的和
        sum_of_squares = sum([pow(a - b, 2) for a, b in preferences.values()])
        # 修正的欧式距离，返回值的范围为[0,1]
        return 1 / (1 + sqrt(sum_of_squares))

        # 使用皮尔逊距离

    def pearson_correlation(self, criticA, criticB, prefs='users'):
        # 返回两个评论者之间的皮尔逊相关系数
        if prefs == 'users':
            preferences = self.share_preferences(criticA, criticB)
        elif prefs == 'movies':
            preferences = self.shared_critics(criticA, criticB)
        else:
            raise Exception("No preferences of type '%s'." % prefs)

        length = len(preferences)
        if length == 0: return 0

        # 循环处理每一个评论者之间的皮尔逊相关系数
        sumA = sumB = sumSquareA = sumSquareB = sumProducts = 0
        for a, b in preferences.values():
            sumA += a
            sumB += b
            sumSquareA += pow(a, 2)
            sumSquareB += pow(b, 2)
            sumProducts += a * b

            # 计算皮尔逊系数
        numerator = (sumProducts * length) - (sumA * sumB)
        denominator = sqrt(((sumSquareA * length) - pow(sumA, 2)) * ((sumSquareB * length) - pow(sumB, 2)))
        if denominator == 0: return 0
        return abs(numerator / denominator)

    # 为特定用户寻找最好的影评人
    def similar_critics(self, user, metric='euclidean', n=None):
        # 为特定用户寻找一个合适的影评人
        metrics = {
            'euclidean': self.euclidean_distance,
            'pearson': self.pearson_correlation
        }
        distance = metrics.get(metric, None)
        # 解决可能出现的状况
        if user not in self.reviews:
            raise KeyError("Unknown user, '%s'." % user)
        if not distance or not callable(distance):
            raise KeyError("Unknown or unprogrammed distance metric '%s'." % metric)
            # 计算对用户最合适的影评人
        critics = {}
        for critic in self.reviews:
            # 不能与自己进行比较
            if critic == user:
                continue
            critics[critic] = distance(user, critic)

        if n:
            return heapq.nlargest(n, critics.items(), key=itemgetter(1))
        return critics

    # 预测用户评分
    # 基于其他用户的评分预测当前用户对电影可能的评分
    def predict_ranking(self, user, movie, metric='euclidean', critics=None):
        '''''
        预测一个用户对一部电影的评分，相当于评论过这部电影的用户对当前用户的加权均值
        并且权重取决与其他用户和该用户的相似程度
        '''
        critics = critics or self.similar_critics(user, metric=metric)
        total = 0.0
        simsum = 0.0

        for critic, similarity in critics.items():
            if movie in self.reviews[critic]:
                total += similarity * self.reviews[critic][movie]['rating']
                simsum += similarity

        if simsum == 0.0: return 0.0
        return total / simsum
        # 预测所有电影的评分

    def predict_all_rankings(self, user, metric='euclidean', n=None):
        '''''
        为所有的电影预测评分，返回前n个评分的电影和它们的评分
        '''
        critics = self.similar_critics(user, metric=metric)
        movies = {
            movie: self.predict_ranking(user, movie, metric, critics)
            for movie in self.movies
        }
        if n:
            return heapq.nlargest(n, movies.items(), key=itemgetter(1))
        return movies

    # 基于物品的协同过滤
    def shared_critics(self, movieA, movieB):
        '''''
        返回两部电影的交集,即两部电影在同一个人观看过的情况
        '''
        if movieA not in self.movies:
            raise KeyError("Couldn't find movie '%s' in data" % movieA)
        if movieB not in self.movies:
            raise KeyError("Couldn't find movie '%s' in data" % movieB)

        criticsA = set(critic for critic in self.reviews if movieA in self.reviews[critic])
        criticsB = set(critic for critic in self.reviews if movieB in self.reviews[critic])

        shared = criticsA & criticsB  # 和操作

        # 创建一个评论过的字典以返回
        reviews = {}
        for critic in shared:
            reviews[critic] = (
                self.reviews[critic][movieA]['rating'],
                self.reviews[critic][movieB]['rating']
            )

        return reviews

    def similar_items(self, movie, metric='eculidean', n=None):
        metrics = {
            'euclidean': self.euclidean_distance,
            'pearson': self.pearson_correlation,
        }
        distance = metrics.get(metric, None)
        # 解决可能出现的状况
        if movie not in self.reviews:
            raise KeyError("Unknown movie, '%s'." % movie)
        if not distance or not callable(distance):
            raise KeyError("Unknown or unprogrammed distance metric '%s'." % metric)
        items = {}
        for item in self.movies:
            if item == movie:
                continue
            items[item] = distance(item, movie, prefs='movies')
        if n:
            return heapq.nlargest(n, items.items(), key=itemgetter(1))
        return items

    def predict_items_recommendation(self, user, movie, metric='euclidean'):
        movie = self.similar_items(movie, metric=metric)
        total = 0.0
        simsum = 0.0

        for relmovie, similarity in movie.items():
            if relmovie in self.reviews[user]:
                total += similarity * self.reviews[user][relmovie]['rating']
                simsum += similarity

        if simsum == 0.0: return 0.0
        return total / simsum


if __name__ == '__main__':
    data = relative_path('u.data')
    item = relative_path('u.item')
    model = MovieLens(data, item)

    # 输出排名前十的电影
    for mid, avg, num in model.top_rated(10):
        title = model.movies[mid]['title']
        print "[%0.3f average rating (%i reviews)] %s" % (avg, num, title)

        # 测试欧式距离
    print model.euclidean_distance(631, 532)  # A,B

    # 测试皮尔逊距离
    print model.pearson_correlation(232, 532)

    # 测试一下两种度量指标的结果
    # 利用pearson相关系数的结果
    for item in model.similar_critics(232, 'pearson', n=10):
        print "%4i: %0.3f" % item
    print '=================================='
    # 利用欧式距离的结果为
    for item in model.similar_critics(232, 'euclidean', n=10):
        print "%4i: %0.3f" % item

    # 给用户评分测试
    print model.predict_ranking(422, 50, 'euclidean')
    print model.predict_ranking(422, 50, 'pearson')
    # 返回排名前n的电影
    for mid, rating in model.predict_all_rankings(578, 'pearson', 10):
        print '%0.3f: %s' % (rating, model.movies[mid]['title'])

    # 基于物品相似性
    # for movie, similarity in model.similar_items(631, 'pearson').items():
    #     print '%0.3f : %s' % (similarity, model.movies[movie]['title'])

    print model.predict_items_recommendation(232, 52, 'pearson')

