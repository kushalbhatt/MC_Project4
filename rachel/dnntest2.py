import numpy as np
import csv
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
'''
#trainfilename will look like 487 column matrix, where last row is y
#tranfilename will be all donors combined, eat vs eat and eat vs non-eat
#have 3 donors, D1 is eat, D2 is eat, D3 is non-eat; DTW feature matrix inputs(3 iterations):D1 vs D2, D3; D2 vs D1, D3; D3 vs D2, D1;
trainfilename = "pima-indians-diabetes.csv"
#DTW feature matrix of Test User vs D1, D2 (eat)
testfilename = ""
# Generate dummy data
from numpy import genfromtxt
x_train = genfromtxt(trainfilename, delimiter=',')
#delete last column from x_train
y_train = x_train[:,[8]]#485
x_test = genfromtxt(testfilename, delimiter=',')
#delete last column from x_test
y_test = x_test[:,[8]]#485
'''
x_train = np.random.random((1000, 486)) #first number is rows, second number is columns
y_train = np.random.randint(2, size=(1000, 1))#this produces random numbers, either 0 or 1
x_test = np.random.random((100, 486))
y_test = np.random.randint(2, size=(100, 1))

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

model.compile(loss='binary_crossentropy',
			  optimizer='adam',
			  metrics=['accuracy'])

model.fit(x_train, y_train,
		  epochs=20,
		  batch_size=64git )
#In general: Larger batch sizes result in faster progress in training, but don't always converge as fast. Smaller batch sizes train slower, but can converge faster. It's definitely problem dependent.
#In general, the models improve with more epochs of training, to a point. They'll start to plateau in accuracy as they converge. Try something like 50 and plot number of epochs (x axis) vs. accuracy (y axis). You'll see where it levels out.
#batch size defines number of samples that going to be propagated through the network.
score = model.predict(x_test, batch_size=None, verbose=1,steps=None) #predict(self, x, batch_size=None, verbose=0, steps=None)
#x: The input data, as a Numpy array (or list of Numpy arrays if the model has multiple outputs).
#batch_size: Integer. If unspecified, it will default to 32.
#verbose: Verbosity mode, 0 or 1.
#steps: Total number of steps (batches of samples) before declaring the prediction round finished. Ignored with the default value of None.
#evaluate(x_test, y_test, batch_size=128)
