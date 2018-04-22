import numpy as np
import csv
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import plot_model
'''
Input::		Most Similar User set--- (In our case give the name of file that has relevant scale-space data for that user)
Output::	After creating and training the User_Specific DNNs for each Donor
			'Other' Test user segments can be classified as eat/non-eat/uncertain  

The user specific DNN is implemented based on the output of Generalized DNN
Once the most similar donor set is obtained.
 A user-specific DNN is created for each of the donors in most similar set
	e.g. if most similar set has 3 donors.... 3 specific DNN networks will be created

Training Data:    Donor x Donor    (Eat x Eat)  and (Eat x Non-Eat) DTW Feature Matrix  (COmputed Same as fig 17,16)
					Note:: Only those Donors who appear in most simialar set are used (ignore others)  
					
Testing Data:     Test user   (Eat x 'Other') DTW Feature Matrix 
'''
def compute_user_specific_DNN(similar_donors):
	#to-be-initialized based on DTW-Feature_Matrix rows
	data_train = []
	labels_train = []

	#4 layers each with 256 neurons
	model = Sequential() #linear stack of layers
	model.add(Dense(256, input_dim=486, activation='relu'))#add layers to DNN
	model.add(Dropout(0.5))
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

	model.compile(loss='binary_crossentropy',
				  optimizer='adam',
				  metrics=['accuracy'])

	model.fit(x_train, y_train,
			  epochs=20,
			  batch_size=64)
	#In general: Larger batch sizes result in faster progress in training, but don't always converge as fast. Smaller batch sizes train slower, but can converge faster. It's definitely problem dependent.
	#In general, the models improve with more epochs of training, to a point. They'll start to plateau in accuracy as they converge. Try something like 50 and plot number of epochs (x axis) vs. accuracy (y axis). You'll see where it levels out.
	#batch size defines number of samples that going to be propagated through the network.

	plot_model(model,to_file="user-specific-model.png",show_shapes = True)
	#x: The input data, as a Numpy array (or list of Numpy arrays if the model has multiple outputs).
	#batch_size: Integer. If unspecified, it will default to 32.
	#verbose: Verbosity mode, 0 or 1.
	#steps: Total number of steps (batches of samples) before declaring the prediction round finished. Ignored with the default value of None.
	#evaluate(x_test, y_test, batch_size=128)
	print "Returning from user-specific-dnn"
