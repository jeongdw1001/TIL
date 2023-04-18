import os
import cv2
import numpy as np
from numpy import save

# array of all the classes
class_names = ['banana', 'apple', 'pear', 'grapes', 'orange', 'kiwi', 'watermelon',
               'pomegranate', 'pineapple', 'mango.', 'cucumber', 'carrot', 'capsicum', 
               'onion', 'potato', 'lemon', 'tomato', 'raddish', 'beetroot', 'cabbage', 
               'lettuce', 'spinach', 'soy bean', 'cauliflower', 'bell pepper', 'chilli pepper', 
               'turnip', 'corn', 'sweetcorn', 'sweet potato', 'paprika', 'jalepeho', 'ginger, 
               'garlic', 'peas', 'eggplant']

train_data_array = []
train_data_labels_array = []

print("Loading the train data")

rootdir = "D:/dataset/test04/train"

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        # let's open each image in the directory
        frame = cv2.imread(os.path.join(subdir, file))
        
        # check the validity of the image
        if frame is None:
            print("not an image")
        else:
            print(subdir, file)
            
            # let's check the sizes of the imagees to see if all are the same
            # each image has it's own size and dimetions
            # so, we have to resized all the images to the same size
            # we will reduce the size of the images the 28*28
            resized = cv2.resize(frame, (28,28), interpolation=cv2.INTER_AREA)
            checkSize = resized.shape[0] #checking that the resize was done successfuly
            if checkSize == 28:
                train_data_array.append(resized)
                index = class_names.index(os.path.basename(subdir))
                train_data_labels_array.append(index)

# converts the lists to numpy arrays
train_data = np.array(train_data_array)
train_data_labels = np.array(train_data_labels_array)

print("Finished loading the train data")
print("Number of train records : ", train_data.shape[0])

print(train_data.shape)
print(train_data_labels.shape)

