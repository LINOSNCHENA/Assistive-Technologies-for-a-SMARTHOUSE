# set the matplotlib backend so figures can be saved in the background
import matplotlib
#matplotlib.use("Agg")
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.preprocessing.image import img_to_array
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from search.generalmodel import GeneralModel
import matplotlib.pyplot as plt
from imutils import paths
import numpy as np
import argparse
import random
import pickle
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,help="path to input dataset (i.e., directory of images)")
ap.add_argument("-m", "--model", required=True,	help="path to output model")
ap.add_argument("-l", "--labelbin", required=True,	help="path to output label binarizer")
args = vars(ap.parse_args())
EPOCHS = 3
INIT_LR = 1e-3
BS = 32
IMAGE_DIMS = (96, 96, 3)

# grab the image paths and randomly shuffle them
print("[INFO #1] loading images...")
imagePaths = sorted(list(paths.list_images(args["dataset"])))
random.seed(42)
random.shuffle(imagePaths)
data = []
labels = []

# loop over the input images
for imagePath in imagePaths:
	# load the image, pre-process it, and store it in the data list
	image = cv2.imread(imagePath)
	image = cv2.resize(image, (IMAGE_DIMS[1], IMAGE_DIMS[0]))
	image = img_to_array(image)
	data.append(image)

	# extract set of class labels from the image path and update the
	l = label = imagePath.split(os.path.sep)[-2].split("_")
	labels.append(l)

# scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)
print("[INFO #2] data matrix: {} images ({:.2f}MB)".format(len(imagePaths), data.nbytes / (1024 * 1000.0)))

# binarize the labels using scikit-learn's special multi-label
# binarizer implementation
print("[INFO #3] class labels:")
mlb = MultiLabelBinarizer()
labels = mlb.fit_transform(labels)

# loop over each of the possible class labels and show them
for (i, label) in enumerate(mlb.classes_):
	print("{}. {}".format(i + 1, label))
(trainX, testX, trainY, testY) = train_test_split(data,labels, test_size=0.2, random_state=42)

# construct the image generator for data augmentation
aug = ImageDataGenerator(rotation_range=25, width_shift_range=0.1,
	height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
	horizontal_flip=True, fill_mode="nearest")

# initialize the model using a sigmoid activation as the final layer
# in the network so we can perform multi-label classification
print("[INFO #4] compiling model...")
model = GeneralModel.build(
	width=IMAGE_DIMS[1], height=IMAGE_DIMS[0],
	depth=IMAGE_DIMS[2], classes=len(mlb.classes_),	finalAct="sigmoid")

# initialize the optimizer (SGD is sufficient)
opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)
model.compile(loss="binary_crossentropy", optimizer=opt,metrics=["accuracy"])

# train the network
print("[INFO #5] training network...")
H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),validation_data=(testX, testY),	
	steps_per_epoch=len(trainX) // BS,epochs=EPOCHS, verbose=1)

# save the model to disk
print("[INFO #6] serializing network...")
model.save(args["model"])

# save the multi-label binarizer to disk
print("[INFO #7] serializing label binarizer...")
f = open(args["labelbin"], "wb")
f.write(pickle.dumps(mlb))
f.close()

# plot the training loss and accuracy history
plt.figure()
plt.plot(H.history["loss"], label="train_loss data")
plt.plot(H.history["acc"], label="train_acc data")
plt.plot(H.history["val_loss"], label="val_loss data")
plt.plot(H.history["val_acc"], label="val_acc data")
plt.title("Pemba Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Pemba Loss/Accuracy")
plt.legend(loc="best")
plt.savefig('Plot_Training.png')