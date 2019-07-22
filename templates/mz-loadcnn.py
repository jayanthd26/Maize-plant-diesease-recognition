# -*- coding: utf-8 -*-




from keras.models import load_model
from keras.models import model_from_json
import json


filename="0.jpg"
# load json and create model
json_file = open('Final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("Final_maize.h5")
print("Loaded model from disk")

import numpy as np
from keras.preprocessing import image
import matplotlib.pyplot as plt

img_pred = image.load_img('/Users/manthanmkulakarni/Desktop/Dataset/Testing_Dataset/Corn_(maize)___Common_rust_/'+filename, target_size = (64, 64))
plt.imshow(img_pred)
img_pred = image.img_to_array(img_pred)

img_pred = np.expand_dims(img_pred, axis = 0)
rslt = loaded_model.predict(img_pred)

#ind = train_set.class_indices

if rslt[0][0] == 1:
    prediction = "No dieseases"
else:
    prediction = "Common Rust found"
print(prediction)

"""
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file("keras_model.h5")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)

"""