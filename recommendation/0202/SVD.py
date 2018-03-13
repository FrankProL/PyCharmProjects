# encoding:utf-8

# http://blog.csdn.net/buracag_mc/article/details/70143833

def factor2(R, P=None, Q=None, K=2, steps=5000, alpha=0.0002, beta=0.02):
    """
           依靠给定的参数训练矩阵R.

        :param R:  N x M的矩阵，即将要被训练的
        :param P: 一个初始的N x K矩阵
        :param Q: 一个初始的M x K矩阵
        :param K: 潜在的特征
        :param steps: 最大迭代次数
        :param alpha: 梯度下降法的下降率
        :param beta:  惩罚参数

        :returns:  P 和 Q
           """
    if not P or not Q:
        P, Q = initialize(R, K)
    Q = Q.T

    rows, cols = R.shape
    for step in xrange(steps):

        eR = np.dot(P, Q)  # 一次性内积即可

        for i in xrange(rows):
            for j in xrange(cols):
                if R[i, j] > 0:
                    eij = R[i, j] - eR[i, j]
                    for k in xrange(K):
                        P[i, k] = P[i, k] + alpha * (2 * eij * Q[k, j] - beta * P[i, k])
                        Q[k, j] = Q[k, j] + alpha * (2 * eij * P[i, k] - beta * Q[k, j])

        eR = np.dot(P, Q)  # Compute dot product only once
        e = 0

        for i in xrange(rows):
            for j in xrange(cols):
                if R[i, j] > 0:
                    e = e + pow((R[i, j] - eR[i, j]), 2)
                    for k in xrange(K):
                        e = e + (beta / 2) * (pow(P[i, k], 2) + pow(Q[k, j], 2))
        if e < 0.001:
            break

    return P, Q.T


class Recommender(object):
    @classmethod
    def load(klass, pickle_path):
        '''''
        接受磁盘上包含pickle序列化后的文件路径为参数，并用pickle模块载入文件。
        由于pickle模块在序列化是会保存导出时对象的所有属性和方法，因此反序列
        化出来的对象有可能已经和当前最新代码中的类不同。
        '''
        with open(pickle_path, 'rb') as pkl:
            return pickle.load(pkl)

    def __init__(self, udata):
        self.udata = udata
        self.users = None
        self.movies = None
        self.reviews = None

        # 描述性工程
        self.build_start = None
        self.build_finish = None
        self.description = None

        self.model = None
        self.features = 2
        self.steps = 5000
        self.alpha = 0.0002
        self.beta = 0.02

        self.load_dataset()

    def dump(self, pickle_path):
        '''''
        序列化方法、属性和数据到硬盘，以便在未来导入
        '''
        with open(pickle_path, 'wb') as pkl:
            pickle.dump(self, pkl)

    def load_dataset(self):
        '''''
        加载用户和电影的索引作为一个NxM的数组，N是用户的数量，M是电影的数量；标记这个顺序寻找矩阵的价值
        '''

        self.users = set([])
        self.movies = set([])
        for review in load_reviews(self.udata):
            self.users.add(review['userid'])
            self.movies.add(review['movieid'])

        self.users = sorted(self.users)
        self.movies = sorted(self.movies)

        self.reviews = np.zeros(shape=(len(self.users), len(self.movies)))
        for review in load_reviews(self.udata):
            uid = self.users.index(review['userid'])
            mid = self.movies.index(review['movieid'])
            self.reviews[uid, mid] = review['rating']

    def build(self, output=None):
        '''''
        训练模型
        '''
        options = {
            'K': self.features,
            'steps': self.steps,
            'alpha': self.alpha,
            'beta': self.beta
        }

        self.build_start = time.time()
        nnmf = factor2
        self.P, self.Q = nnmf(self.reviews, **options)
        self.model = np.dot(self.P, self.Q.T)
        self.build_finish = time.time()

        if output:
            self.dump(output)

            # 利用模型来访问预测的评分

    def predict_ranking(self, user, movie):
        uidx = self.users.index(user)
        midx = self.movies.index(movie)
        if self.reviews[uidx, midx] > 0:
            return None
        return self.model[uidx, midx]

        # 预测电影的排名

    def top_rated(self, user, n=12):
        movies = [(mid, self.predict_ranking(user, mid)) for mid in self.movies]
        return heapq.nlargest(n, movies, key=itemgetter(1))

