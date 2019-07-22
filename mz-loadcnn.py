# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import tensorflow as tf



from keras.models import load_model
from keras.models import model_from_json
import json
# load json and create model
json_file = open('Final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model=load_model("Mz-model.h5")
print("Loaded model from disk")

import numpy as np
from keras.preprocessing import image
import matplotlib.pyplot as plt

#path='/home/ubuntu/ml/Plant-disease-detection-master/Dataset/Testing_Dataset/Corn_(maize)___healthy/7.jpg'


path='/Users/manthanmkulakarni/Desktop/Dataset/Testing_Dataset/Corn_(maize)___healthy/60.jpg'

img_pred = image.load_img(path, target_size = (64, 64))
plt.imshow(image.load_img(path, ))
img_pred = image.img_to_array(img_pred)

img_pred = np.expand_dims(img_pred, axis = 0)
rslt = loaded_model.predict(img_pred)

#ind = train_set.class_indices

if rslt[0][0] == 1:
    prediction = "No dieseases"
else:
    prediction = "Common Rust found"
print("\n\n",prediction,"\n\n")

'''
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file("/home/ubuntu/ml/Plant-disease-detection-master/Final_maize.h5")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)'''