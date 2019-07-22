# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import tensorflow as tf

classifier=Sequential()

#convolution
classifier.add(Convolution2D(32,3,3,input_shape=(64,64,3),activation='relu'))

#pooling
classifier.add(MaxPooling2D(pool_size=(2,2)))

#flattening()
classifier.add(Flatten())

classifier.add(Dense(output_dim=128,activation='relu'))
classifier.add(Dense(output_dim=1,activation='sigmoid'))

#compiling cnn
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#fitting  images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory(
        'Dataset/Training_Dataset',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'Dataset/Testing_Dataset',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

classifier.fit_generator(
        train_set,
        steps_per_epoch=8000,
        epochs=1,
        validation_data=test_set,
        validation_steps=2000)
import numpy as np
from keras.preprocessing import image
import matplotlib.pyplot as plt

img_pred = image.load_img('/home/ubuntu/ml/Plant-disease-detection-master/Dataset/Testing_Dataset/Corn_(maize)___Common_rust_/85.jpg', target_size = (64, 64))
plt.imshow(img_pred)
img_pred = image.img_to_array(img_pred)

img_pred = np.expand_dims(img_pred, axis = 0)
rslt = classifier.predict(img_pred)

ind = train_set.class_indices

if rslt[0][0] == 1:
    prediction = "No dieseases"
else:
    prediction = "Common Rust found"
print(prediction)

from keras.models import model_from_json
model_json = classifier.to_json()
with open("Final.json", "w") as json_file:
    json_file.write(model_json)
classifier.save_weights("Final_maize.h5")
print("Model Saved to disk")

from keras.models import load_model
from keras.models import model_from_json
import json
# load json and create model
json_file = open('Final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("Final_maize.h5")
print("Loaded model from disk")