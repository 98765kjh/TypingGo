import wave
import numpy as np
import os
import sys

trPath = "wav/training/cut/"
tePath = "wav/test/cut/"

classes = ["Cat", "Dog", "Pig", "Sad", "Deep", "Part", "Hello", "Happy", "Enter", "Robot"]
classNum = 10
trNum = 50
teNum = 3
size = 40000

# training set
def getTrainingData():
    data = np.empty([classNum, trNum, size])
    classPos = -1
    print "get training data... ",
    for name in classes:
        classPos += 1
        for pos in xrange(trNum):
            path = trPath + name + str(pos+1) + '.wav'
            if not os.path.exists(path):
                print path, "doesn't exists."
                sys.exit(0)

            wav = wave.open(path, 'r')
            f = wav.readframes(40000)
            data[classPos, pos] = np.fromstring(f, 'Int16')

            wav.close()


    print "finish"
    return data

def getTrainingLabel():
    label = np.arange()

# test set
def getTestData():
    pass
def getTestLabel():
    pass

# get all data
def getAllData():
    TrData = getTrainingData()
    TrLabel = getTrainingLabel()

    TeData = getTestData()
    TeLabel = getTestLabel()

    return TrData, TrLabel, TeData, TeLabel
