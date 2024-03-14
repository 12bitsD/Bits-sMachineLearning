from onedal.linear_model import linear_model
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

filename= "iris.data.csv"
names = ["separ-length","separ-width","petal-length","petal-width","class"]
dataset = read_csv(filename,names=names)

#dimension of data
print("Dimension of data: row %s,column %s " % dataset.shape)
#check the header 10 lines of dataset
print(dataset.head(10))
#check the info for data
print(dataset.describe())
#distribution of dataset
print(dataset.groupby("class").size())

#show the data in graph

#box diagram
dataset.plot(kind="box",subplots=True,layout=(2,2),sharex=False,sharey=False)

#normal
dataset.hist()

#scatter_matrix
scatter_matrix(dataset)
plt.show()


#评估算法
#分离评估数据集，80%训练数据集，20%评估数据集
arr =dataset.values
X,Y=arr[:,0:4],arr[:,4]
print(X)
print("___|___")
print(Y)

validation_size=0.2
seed =7
X_train,X_validation,Y_train,Y_validation=train_test_split(X,Y,test_size=validation_size,random_state=seed)

'''
模型算法：
1.LR（Linear Regression线性回归）
2.LDR（Logistic Discriminant Analysis线性判断分析)
3.KNN
4.CART(Classification and Regression Tree分类与回归树)
5.NB(Navier-Bayesian)
6.SVM(Support Vector Machine)
'''
#模型
models={}
models["LR"]=LogisticRegression()
models["LDA"]=LinearDiscriminantAnalysis()
models["KNN"]=KNeighborsClassifier()
models["SVM"]=SVC()
models["CART"]=DecisionTreeClassifier()
models["NB"]=GaussianNB()

#评估
result =[]
for key in models:
    kfold=KFold(n_splits=10, random_state=seed,shuffle=True)
    cv_result=cross_val_score(models[key],X_train,Y_train,cv=kfold,scoring='accuracy')
    result.append(cv_result)
    print("%s:%f (%f)"%(key,cv_result.mean(),cv_result.std()))
