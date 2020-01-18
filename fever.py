# FEVER DETECTING ARTIFICIAL NEURAL NETWORK(ANN)
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from pandas import read_csv
import numpy

dataset1 = read_csv('fever1.csv', header=None)	
dataset1[[1,2,3,4,5,6,7]] = dataset1[[1,2,3,4,5,6,7]].replace(0, numpy.NaN)
print(dataset1)
dataset1.fillna(dataset1.median(), inplace=True)
print(dataset1)
X = dataset1.iloc[:, :-1] 	#X = dataset1.iloc[:,0:8]
y = dataset1.iloc[:, -1]	#y = dataset1.iloc[:,:8]
# define the Muntu model ===================================================================
muntu = Sequential()
muntu.add(Dense(16, input_dim=8, activation='elu'))
muntu.add(Dense(8, activation='elu'))
muntu.add(Dense(1, activation='sigmoid'))
muntu.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['mse','acc'])
history = muntu.fit(X, y,validation_split=0.33, epochs=300, batch_size=4, verbose=0)
# plot metrics from trained model	//	# summarize history for accuracy	 	   # 1
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Training and Testing accuracy in fever detection')
plt.ylabel('Accuracy values')
plt.xlabel('epoch')
plt.legend(['ACC_Training Data', 'ACC_Validation data','Loss_Training data',
'Loss_Validation data','MSE_Training data','MSE_Validation data'], loc='best')
plt.savefig('Plot_ACC.png')
# plot metrics from trained model	//	# summarize history for loss		    	# 2
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Training and testing loss in fever detection')
plt.ylabel('Loss values')
plt.xlabel('epoch')
plt.legend(['ACC_Training Data', 'ACC_Validation data','Loss_Training data',
'Loss_Validation data','MSE_Training data','MSE_Validation data'], loc='best')
plt.savefig('Plot_Loss.png')
# plot metrics from trained //	# summarize history for mean_squared_error          # 3
plt.plot(history.history['mean_squared_error'])
plt.plot(history.history['val_mean_squared_error'])
plt.title('Training and testing mean_squared_error in fever detection')
plt.ylabel('mean_squared_error values')
plt.xlabel('epoch')
plt.legend(['ACC_Training Data', 'ACC_Validation data','Loss_Training data',
'Loss_Validation data','MSE_Training data','MSE_Validation data'], loc='best')
plt.savefig('Plot_MSE.png')
#=========================================================================================

# evaluate the keras muntuz
accuracy = muntu.evaluate(X, y)
print("Loss, MSE, Accuracy",accuracy)
predictions = muntu.predict_classes(X)
for i in range(1):
	print('%s => %d (Sample Prediction of Fever %d)' % (X[i].tolist(), predictions[i], y[i]))
print("================================== END OF PREDICTION ================================")

