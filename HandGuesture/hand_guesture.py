# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:23:12 2017

@author: ellen
"""

from keras.models import Sequential 
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

import matplotlib.pyplot as plt

model = Sequential()
model.add(Convolution2D(32,(3,3), input_shape=(64,64,3), activation='relu' ))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(activation="relu", units=128))
model.add(Dense(units = 4, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('datasets/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('datasets/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'categorical')

training_set.class_indices

model.fit_generator(training_set,
                    steps_per_epoch = 93,
                    epochs = 2,
                    validation_data = test_set,
                    validation_steps = 21)


import numpy as np
from keras.preprocessing import image

test_image = image.load_img('datasets/predict/IMG_5025.JPG', target_size=(64,64))
test_image = image.img_to_array(test_image)

test_image = np.expand_dims(test_image,axis = 0)

result = model.predict(test_image)

test_image = image.load_img('datasets/predict/IMG_5024.JPG', target_size=(64,64))
test_image = image.img_to_array(test_image)

test_image = np.expand_dims(test_image,axis = 0)

result = model.predict(test_image)

test_image = image.load_img('datasets/predict/IMG_5027.JPG', target_size=(64,64))
test_image = image.img_to_array(test_image)

test_image = np.expand_dims(test_image,axis = 0)

test_image[0,:,:,2] = test_image[0,:,:,2]/255
result = model.predict(test_image)
