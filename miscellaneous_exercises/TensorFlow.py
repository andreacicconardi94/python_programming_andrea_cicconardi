import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images/255.0
test_images = test_images/255.0

#plt.imshow(train_images[7], cmap=plt.cm.binary)
#plt.show()

model = keras.Sequential([
	keras.layers.Flatten(input_shape=(28,28)),	#flat our data
	keras.layers.Dense(128, activation="relu"),	#Dense=all connected
	keras.layers.Dense(10, activation="softmax")	#Softmax put the probability of each neuron egual to 1
	])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(train_images, train_labels, epochs=5)		#epochs = how many times the same image is showen, to improve performance
							#If you increase epochs too much the model becomes less reliable

#test_loss, test_acc = model.evaluate(test_images, test_labels)
#print ("Tested Acc:", test_acc)

prediction = model.predict(test_images)			#The argument must be a list
print (prediction)
