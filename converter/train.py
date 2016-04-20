from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers import Convolution2D, Flatten, AveragePooling2D
import numpy as np
import training_set
from keras.optimizers import SGD, Adamax, Adadelta, Adagrad, RMSprop, Adam
import pickle


ds = Sequential()

ds.add(Convolution2D(32, 3, 3, border_mode='valid', input_shape=(1, 100, 32)))
ds.add(Activation("tanh"))
ds.add(AveragePooling2D(pool_size=(10, 2)))
ds.add(Convolution2D(64, 3, 3, border_mode='valid', input_shape=(1, 100, 32)))
ds.add(Activation("tanh"))
ds.add(Flatten())
ds.add(Dense(100, activation='tanh'))
ds.add(Dropout(0.5))
ds.add(Dense(100, activation='tanh'))
ds.add(Dropout(0.5))
ds.add(Dense(100, activation='tanh'))
ds.add(Dropout(0.5))
ds.add(Dense(100, activation='tanh'))
ds.add(Dropout(0.5))
ds.add(Dense(1, activation='tanh'))

xs = pickle.load(open("xs", "rb"), encoding="bytes")

ys = pickle.load(open("ys", "rb"), encoding="bytes")

print(len(ys[0]))
print(len(xs[0]))
print(xs[0])

ds.compile(loss='binary_crossentropy',
              optimizer='rmsprop')

samples = []

for x in xs:
    samples.append([x])
images = pickle.load(open("urls", "rb"))

def test():
    wrong = 0.
    print(len(xs[300:]))
    for i in range(300, len(xs)):
        if ys[i][0] > 0 != ds.predict(np.array([samples[i],]))[0] > 0:
            print(i, ds.predict(np.array([samples[i], ])), images[int(i/2)])
            wrong += 1

    print(wrong/len(xs[300:]))
for i in range(0, 10):
    ds.fit(np.array(samples[:300]), np.array(ys[:300]), nb_epoch=10)
    test()
    ds.save_weights("trained", overwite=True)



test()
