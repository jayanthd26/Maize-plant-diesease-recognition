import sys, json, numpy as np
from notify_run import Notify


#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #print (lines)
    #print(type(lines))
    
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])


# -*- coding: utf-8 -*-


def main():

    from keras.models import load_model
    from keras.models import model_from_json
    import json

    from notify_run import Notify
    
   
    
    filename="0.jpg"
   
    #filename="0.jpg"
    # load json and create model
    json_file = open('Final.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model=load_model("Mz-model.h5")
    #loaded_model.load_model("Mz-model.h5")
    print("Loaded model from disk")

    import numpy as np
    from keras.preprocessing import image
    import matplotlib.pyplot as plt

    img_pred = image.load_img('/Users/manthanmkulakarni/Desktop/JU-Nanda/images/'+filename, target_size = (64, 64))
    plt.imshow(img_pred)
    img_pred = image.img_to_array(img_pred)

    img_pred = np.expand_dims(img_pred, axis = 0)
    rslt = loaded_model.predict(img_pred)

    #ind = train_set.class_indices

    if (rslt[0][0] == 1):
        prediction = "No dieseases"
    else:
        prediction = "Common Rust Found"
        notify = Notify()
        notify.send('Common Rust FOUND !!!\n Follow the preventive measures')
    print(prediction)
     

"""
import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_keras_model_file("keras_model.h5")
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)







def main():
    #get our data as an array from read_in()
    lines = read_in()
    print type(lines['path'])
    #create a numpy array
    np_lines = np.array(lines)

    #use numpys sum method to find sum of all elements in the array
    lines_sum = np.sum(np_lines)

    #return the sum to the output stream
    print ("herer")
    print lines_sum
"""

#start process
if __name__ == '__main__':
    main()
    