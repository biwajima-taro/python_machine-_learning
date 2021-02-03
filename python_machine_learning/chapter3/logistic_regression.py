import numpy as np


class LogisticRegression:
    def __init__(self, eta=0.05, n_iter=100, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X: np.ndarray, y: np.ndarray):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1+X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y-output)
            self.w_[1:] += self.eta*X.T.dot(errors)
            self.w_[0] += self.eta*errors.sum()
            cost = -y.dot(np.log(output))-((1-y).dot(np.log(1-output)))
            self.cost_.append(cost)

        return self
    def activation(self,z):
        return 1./(1.+np.exp(-np.clip(z,-250,250)))

    def net_input(self, X):
        return np.dot(X, self.w_[1:])+self.w_[0]

        return 1./(1.+np.exp(-np.clip(z, -250, 250)))

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, 0)
#############################
#####################################################################################
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np



iris = datasets.load_iris()
X = iris.data[: ,[2, 3]]
y = iris.target
print("class labels:", np.unique(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                           random_state=1, stratify=y)
print(type(X_train))
##############################
sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)






X_train_01_subset=X_train[(y_train==0)|(y_train==1)]
y_train_01_subset=y_train[(y_train==0)|(y_train==1)]

lrgd=LogisticRegression(eta=0.05,n_iter=1000,random_state=1)
lrgd.fit(X_train_01_subset,y_train_01_subset)


from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(C=100.0,random_state=1)
lr.fit(X_train_std,y_train)
print(X_test_std[0,:])
print(X_test_std[0,:].reshape(1,-1))

###############
weights,params=[],[]
for c in np.arange(-5,5):
    lr=LogisticRegression(C=10.**c ,random_state=1)
    lr.fit(X_train_std,y_train)
    weigths.append(lr.coef_[1])
    params.append(10.**c)

weights=np.array(weights)
plt.plot(params,weights[:,0],label="petal length")
plt.plot(params,weigths[:,1],linestyle="--",label="petal width")
plt.ylabel("weight coefficient")
plt.xlabel("C")
plt.legend(loc="upper left")
plt.xscale("log")
plt.show()