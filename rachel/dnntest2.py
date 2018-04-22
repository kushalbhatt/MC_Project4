import numpy as np
import csv
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
'''
trainfilename = "pima-indians-diabetes.csv"
testfilename = ""
# Generate dummy data
from numpy import genfromtxt
x_train = genfromtxt(trainfilename, delimiter=',')
y_train = x_train[:,[8]]#485
x_test = genfromtxt(testfilename, delimiter=',')
y_test = x_test[:,[8]]#485
'''
x_train = np.random.random((1000, 486)) #first number is rows, second number is columns
y_train = np.random.randint(2, size=(1000, 1))#this produces random numbers, either 0 or 1
x_test = np.random.random((100, 486))
y_test = np.random.randint(2, size=(100, 1))

model = Sequential() #linear stack of layers
model.add(Dense(64, input_dim=20, activation='relu'))#add layers to DNN
model.add(Dropout(0.5))#keras.layers.Dropout(rate, noise_shape=None, seed=None)
#Dropout consists in randomly setting a fraction rate of input units to 0 at each update
#during training time, which helps prevent overfitting.
model.add(Dense(64, activation='relu'))
#keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, bias_constraint=None)
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
			  optimizer='rmsprop',
			  metrics=['accuracy'])

model.fit(x_train, y_train,
		  epochs=20,
		  batch_size=128)
#In general: Larger batch sizes result in faster progress in training, but don't always converge as fast. Smaller batch sizes train slower, but can converge faster. It's definitely problem dependent.
#In general, the models improve with more epochs of training, to a point. They'll start to plateau in accuracy as they converge. Try something like 50 and plot number of epochs (x axis) vs. accuracy (y axis). You'll see where it levels out.
#batch size defines number of samples that going to be propagated through the network.
score = model.evaluate(x_test, y_test, batch_size=128)x
