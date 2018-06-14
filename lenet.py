from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras import backend as K

"""
Yo, here happens the magic. LeNet was found in 1998. http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf
It's quite easy and it was made to recognize characters but for little things and get an idea it's ok .  
"""


class LeNet:
    @staticmethod
    def build(width, height, depth, classes):
        """
        :param width: image width
        :param height: image height
        :param depth: Number of channels in input images
        :param classes: Classes (dog or not)
        """
        # initialize the model
        model = Sequential()
        input_shape = (height, width, depth)

        # if "channels first", update the input shape
        if K.image_data_format() == "channels_first":
            input_shape = (depth, height, width)

        # first set of CONV => RELU => POOL layers
        model.add(Conv2D(20, (5, 5), padding="same", input_shape=input_shape))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # second set of CONV => RELU => POOL layers
        model.add(Conv2D(50, (5, 5), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

        # first (and only) set of FC => RELU layers
        model.add(Flatten())
        model.add(Dense(500))
        model.add(Activation("relu"))

        # softmax classifier
        model.add(Dense(classes))
        model.add(Activation("softmax"))

        # return the constructed network architecture
        return model
