import numpy as np
import pandas as pd
import csv
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import plot_model

'''
data = pd.read_csv("DTW1v2.txt",header=None)
test = pd.read_csv("DTW3v1.txt",header=None)
train = data.iloc[:,:-1]
label = data.iloc[:,-1]
label =label.replace('-',0)
print(data.shape)
print(train.shape)
print(test.shape)
'''



train = np.random.random((1000, 486))
label = np.random.randint(2, size=(1000, 1))#this produces random numbers, either 0 or 1
x_test = np.random.random((100, 486))


model = Sequential() #linear stack of layers
model.add(Dense(512, input_dim=486, activation='relu'))#add layers to DNN
model.add(Dropout(0.5))#keras.layers.Dropout(rate, noise_shape=None, seed=None)
#Dropout consists in randomly setting a fraction rate of input units to 0 at each update
#during training time, which helps prevent overfitting.
model.add(Dense(256, activation='relu'))
#keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
model.add(Dropout(0.5))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1, activation='sigmoid')) #output layer

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(train, label,epochs=20,batch_size=64)
#In general: Larger batch sizes result in faster progress in training, but don't always converge as fast. Smaller batch sizes train slower, but can converge faster. It's definitely problem dependent.
#In general, the models improve with more epochs of training, to a point. They'll start to plateau in accuracy as they converge. Try something like 50 and plot number of epochs (x axis) vs. accuracy (y axis). You'll see where it levels out.
#batch size defines number of samples that going to be propagated through the network.
score = model.predict(test, batch_size=None, verbose=0,steps=None) #predict(self, x, batch_size=None, verbose=0, steps=None)
print(score)
score[score>=0.5]=1
score[score<0.5]=0
print("number of eat segments matched for donor 1",np.count_nonzero(score[0:50:1] == 1))
print("number of eat segments matched for donor 2",np.count_nonzero(score[50:100:1] == 1))
if((np.count_nonzero(score[0:50:1] == 1)) > (np.count_nonzero(score[50:100:1] == 1))):
    print("donor 1 is most similar")
else:
    print("donor 2 is most similar")
if((np.count_nonzero(score == 1))> (np.count_nonzero(score == 0))):
   print("the given test user is eat")
else:
   print("the given test user is non-eat")
'''
dtw_donor1 = np.random.random((1000, 486))
dtw_label1 = np.random.randint(2, size=(1000, 1))
dtw_test = np.random.random((100, 486))
'''
model = Sequential() #linear stack of layers
model.add(Dense(256, input_dim=486, activation='relu'))#add layers to DNN
model.add(Dropout(0.5))#keras.layers.Dropout(rate, noise_shape=None, seed=None)
#Dropout consists in randomly setting a fraction rate of input units to 0 at each update
#during training time, which helps prevent overfitting.
model.add(Dense(256, activation='relu'))
#keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
model.add(Dropout(0.5))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1, activation='sigmoid')) #output layer

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model.fit(dtw_donor1, dtw_label1,epochs=20,batch_size=64)
#In general: Larger batch sizes result in faster progress in training, but don't always converge as fast. Smaller batch sizes train slower, but can converge faster. It's definitely problem dependent.
#In general, the models improve with more epochs of training, to a point. They'll start to plateau in accuracy as they converge. Try something like 50 and plot number of epochs (x axis) vs. accuracy (y axis). You'll see where it levels out.
#batch size defines number of samples that going to be propagated through the network.
score2 = model.predict(dtw_test, batch_size=None, verbose=0,steps=None) #predict(self, x, batch_size=None, verbose=0, steps=None)
print(score2)
'''
dtw_donor2 = np.random.random((1000, 486))
dtw_label2 = np.random.randint(2, size=(1000, 1)) 
'''
model.fit(dtw_donor2, dtw_label2,epochs=20,batch_size=64)
score3 = model.predict(dtw_test, batch_size=None, verbose=0,steps=None) #predict(self, x, batch_size=None, verbose=0, steps=None)
print(score3)
score2[score2>=0.5]=1
score2[score2<0.5]=0
label_t1 = np.count_nonzero(score2[0:50:1] == 1)
score3[score3>=0.5]=1
score3[score3<0.5]=0
label_t2 = np.count_nonzero(score3[0:50:1] == 1)
print(label_t1)
print(label_t2)

if(label_t1 ==0 and label_t2 ==0):
    print("non-eat")
else:
    if(label_t1 >15 and label_t2 > 15):
        print("eat")
    else:
        print("non-eat")
