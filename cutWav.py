"""

find all position of original wav file to cut (in this case, least volume is 800)
cut length is 40000

check variable was made to check mistake (miss position),
but useless... it wasn't work well... because I don't have idea for audio file thing.
maybe need to improve algorithm to another way.

"""

import numpy as np
import wave
import random
import os

def getNpRand(size, max):
    ret = []
    for _ in xrange(size):
        ret.append(random.randrange(1, max))
    return np.array(ret)

nch = 1
sw = 2
fr = 44100
nfr = 40000
def writeWav(name, file, _pos):

    now = 1
    tmpName = name[:-3]
    for pos in _pos:
        path = "wav/training/cut/" + tmpName + str(now) + ".wav"
        if os.path.exists(path):
            print "exist"
            return
        now += 1
        w = wave.open(path, 'w')

        w.setnchannels(nch)
        w.setsampwidth(sw)
        w.setframerate(fr)
        w.setnframes(nfr)

        file.setpos(pos)
        data = file.readframes(40000)

        w.writeframes(data)
        w.close()

allName = ["Cat 51", "Dog 50", "Pig 53", "Sad 50", "Deep 50", "Part 50", "Hello 50", "Happy 50", "Enter 50", "Robot 52"]
pos = 1

for now in allName:
    name = now
    path = "wav/training/"+name+".wav"
    wav = wave.open(path, 'r')

    print "#", pos, " - ", name

    f = wav.readframes(-1)
    f = np.fromstring(f, 'Int16')

    startPos = []
    found = 0
    i = 0
    while i < len(f):
        if f[i] > 800:
            check = getNpRand(1000, 5000)

            cnt = 0
            for k in check:
                if f[i+k]>1000:
                    cnt += 1

            if cnt>-1:
                #print i
                # get start pos to cut
                i -= 5000
                startPos.append(i)
                # end pos to cut
                i += 40000
                found += 1

        i += 250
    print "-------- found num: ", found, " --------"

    writeWav(name, wav, startPos)

    pos += 1

print " Finished"
