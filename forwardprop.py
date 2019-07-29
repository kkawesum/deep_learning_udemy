import numpy as np
import matplotlib.pyplot as plt

Nclass=500   #500samples per class

X1=np.random.randn(Nclass,2)+np.array([0,-2])         # three Gaussian clouds

X2=np.random.randn(Nclass,2)+np.array([2,2])

X3=np.random.randn(Nclass,2)+np.array([-2,2]) #centered at [-2,2]

X=np.vstack([X1,X2,X3])
Y= np.array([0]*Nclass+[1]*Nclass+[2]*Nclass)         # initial matrix of labels

plt.scatter(X[:,0], X[:,1], c=Y, s=100, alpha=0.5)
plt.show()


D=2    # features
M=3         #hidden layer size  -> nodes in hidden layer
K=3     #no. of classes

W1=np.random.randn(D,M)       #init the weights
b1=np.random.randn(M)           # hidden layer bias
W2=np.random.randn(M,K)             #hidden layer1 weights
b2=np.random.randn(K)               #output layer weight

def forward(X,W1,b1,W2,b2):             #forward action of the NN
    Z = 1 / (1 + np.exp(-X.dot(W1)-b1))         #implementing the softmax for the 1st layer
    A=Z.dot(W2)+b2
    expA=np.exp(A)
    Y=expA / expA.sum(axis=1,keepdims=True)
    return Y                                            # Y is output

def classification_rate(Y,P):
    n_correct=0
    n_total=0
    for i in range(0,len(Y)):
        n_total +=1
        if(Y[i]==P[i]):
            n_correct +=1
    return float(n_correct/n_total)


P_Y_given_x=forward(X,W1,b1,W2,b2)
P=np.argmax(P_Y_given_x,axis=1)

assert(len(P)==len(Y))

print("classification rate is:",classification_rate(Y,P))

