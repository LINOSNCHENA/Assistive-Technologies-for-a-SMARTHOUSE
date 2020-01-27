# TWO PREDICTORS AND AN EXECUTION TOOL-BOX FOR EACH PREDICTOR
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
import pickle
import os
from pandas import read_csv
import matplotlib.pyplot as plt
#==============================================================================================#0
numpy.random.seed(3)
dataset = numpy.loadtxt("feverTraining1.csv", delimiter=",")
X = dataset[:,0:8]
Y = dataset[:,8]
bantu = Sequential()
bantu.add(Dense(12, input_dim=8, activation='relu'))
bantu.add(Dense(8, activation='relu'))
bantu.add(Dense(1, activation='sigmoid'))
bantu.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc','mse'])
bantu.fit(X, Y, epochs=300, batch_size=4, verbose=0)
history = bantu.fit(X, Y,validation_split=0.33, epochs=300, batch_size=4, verbose=0)
#=============================================================================================
muntu = Sequential()
muntu.add(Dense(16, input_dim=8, activation='elu'))
muntu.add(Dense(8, activation='elu'))
muntu.add(Dense(1, activation='sigmoid'))
muntu.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['mse','acc'])
history = muntu.fit(X, Y,validation_split=0.33, epochs=300, batch_size=4, verbose=0)
#=============================================================================================#1
# Save the trained model as a JSON file. 
print("\n"+"MANUFUCTURING OF THE BANTU AND MUNTU PREDICTION MODELS"+"\n"+
"========================================================================================"+"\n")


# Save the trained model2 as a pickle string. 
pickle.dump(muntu, open('xmuntu1.pkl','wb'))
print("Saved xmodel1 to disk Monze")
xmodel2 = pickle.load(open('xmuntu1.pkl','rb'))
print("Retrived xmodel1 from Monze")

# Save the trained model3 as a pickle string. 
pickle.dump(bantu, open('xmuntu2.pkl','wb'))
print("Saved xmodel2 to disk Chilanga")
xmodel3 = pickle.load(open('xmuntu2.pkl','rb'))
print("Retrived xmodel2 from Chilanga")

model_json = bantu.to_json()
with open("zbantu3.json", "w") as json_file:    json_file.write(model_json)
bantu.save_weights("zbantu3.h5")
print("Saved xmodel1 to disk Choma")
json_file = open('zbantu3.json', 'r')
xmodel_json = json_file.read()
json_file.close()
xmodel1 = model_from_json(xmodel_json)
xmodel1.load_weights("zbantu3.h5")
print("Retrived xmodel1 from Choma")
#*******************************************************************************************#2
xmodel1.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
klassx = xmodel1.evaluate(X, Y, verbose=0)  # one
print("%s:MONZEX8X OPTION #1 %.2f%%" % (xmodel1.metrics_names[1], klassx[1]*100))
xmodel2.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['mse','acc'])
klassy = xmodel2.evaluate(X, Y, verbose=0) #three
print("%s:TEEN CHILANGA OPTION #2 %.2f%%" % (xmodel2.metrics_names[2], klassy[2]*100))
xmodel3.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['mse','acc'])
klassz = xmodel3.evaluate(X, Y, verbose=0) #three
print("%s:TEEN CHOMAX8X OPTION #3 %.2f%%" % (xmodel3.metrics_names[2], klassz[2]*100))

#*******************************************************************************************#3
accuracy1 = xmodel1.evaluate(X, Y)
print('\n'+"Model-Loss1, Model-MSE1, Model-Accuracy1",accuracy1)
accuracy2 = xmodel2.evaluate(X, Y)
print('\n'+"Model-Loss2, Model-MSE2, Model-Accuracy2",accuracy2)
accuracy3 = xmodel3.evaluate(X, Y)
print('\n'+"Model-Loss3, Model-MSE3, Model-Accuracy3",accuracy3)
#*******************************************************************************************#4
datasets1 = read_csv('citizen1.csv', header=None)        # ORDINARY
datasets2 = read_csv('citizen2.csv', header=None)
q1 = datasets1.iloc[0:-1]	           
q2 = datasets2.iloc[0:-1]	              

dataset1 = numpy.loadtxt("citizen1.csv", delimiter=",")  # EXPONENTIAL SENIOR CITIZEN #1
X1 = dataset1[:,0:8]
dataset2 = numpy.loadtxt("citizen2.csv", delimiter=",")  # EXPONENTIAL SENIOR CITIZEN #2
X2 = dataset2[:,0:8]
# create model predictors===================================================================#5
box1=xmodel1.predict_classes(X1)   # PREDICTOR MODEL No.1
box1Size=(len(box1))
box2=xmodel2.predict_classes(X2)   # PREDICTOR MODEL No.2
box2Size=(len(box2))

print('\n'+"======================= PREDICTION RESULTS FOR CITIZEN (A) ================= #2"+'\n')
if box1.sum() > box1Size*30/100:
  print(box1)
  print('UNITS_Total : %d Errors_FOUND : %d GREATER than 30-Threshold @: %.2f%%' % 
  (box1Size, box1.sum(), 100*box1.sum()/box1Size))
elif box1.sum() == box1Size*30/100:
  print(box1)
  print('UNITS_Total : %d Errors_FOUND : %d is EQUAL to t30-Threshold @: %.2f%%' % 
  (box1Size, box1.sum(), 100*box1.sum()/box1Size))
else:
  print(box1)
  print('UNITS_Total : %d Errors_FOUND :  %d LESSER than 30-Threshold @: %.2f%%' % 
  (box1Size, box1.sum(), 100*box1.sum()/box1Size))

print('\n'+"======================= PREDICTION RESULTS FOR CITIZEN (B) ================== #2"+'\n')
if box2.sum() > box2Size*30/100:
  print(box2)
  print('UNITS_Total : %d Errors_FOUND : %d GREATER than 30-Threshold @: %.2f%%' % 
  (box2Size, box2.sum(), 100*box2.sum()/box2Size))
elif box2.sum() == box2Size*30/100:
  print(box2)
  print('UNITS_Total : %d Errors_FOUND : %d is EQUAL to t30-Threshold @: %.2f%%' % 
  (box2Size, box2.sum(), 100*box2.sum()/box2Size))
else:
  print(box2)
  print('UNITS_Total : %d Errors_FOUND :  %d LESSER than 30-Threshold @: %.2f%%' % 
  (box2Size, box2.sum(), 100*box2.sum()/box2Size))

print('\n'+"======================================= END =================================== #2"+'\n')
# plot metrics from trained model	//	# summarize history for accuracy	 	        # 1
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Training and Testing accuracy in fever detection')
plt.ylabel('Accuracy values')
plt.xlabel('epoch')
plt.legend(['ACC_Training Data', 'ACC_Validation data','Loss_Training data',
'Loss_Validation data','MSE_Training data','MSE_Validation data'], loc='best')
plt.savefig('Plot_ACC.png')
# plot metrics from trained model	//	# summarize history for loss		           	# 2
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Training and testing loss in fever detection')
plt.ylabel('Loss values')
plt.xlabel('epoch')
plt.legend(['ACC_Training Data', 'ACC_Validation data','Loss_Training data',
'Loss_Validation data','MSE_Training data','MSE_Validation data'], loc='best')
plt.savefig('Plot_Loss.png')
# plot metrics from trained //	# summarize history for mean_squared_error          # 3
plt.plot(history.history['mse'])
plt.plot(history.history['val_mse'])
plt.title('Training and testing mean_squared_error in fever detection')
plt.ylabel('mean_squared_error values')
plt.xlabel('epoch')
plt.legend(['ACC_Training Data', 'ACC_Validation data','Loss_Training data',
'Loss_Validation data','MSE_Training data','MSE_Validation data'], loc='best')
plt.savefig('Plot_MSE.png')
#===========================================================================================#8