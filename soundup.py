import math
import pyaudio
import sys
print(sys.version)
#sudo apt-get install python-pyaudio

PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 32000 #number of frames per second/frameset.      

FREQUENCY = 500 #Hz, waves per second, 261.63=C4-note.
LENGTH = 1 #seconds to play sound

if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

#for x in xrange(NUMBEROFFRAMES):
for x in range(NUMBEROFFRAMES):
 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

#for x in xrange(RESTFRAMES): 
for x in range(RESTFRAMES): 
 WAVEDATA = WAVEDATA+chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)

stream.write(WAVEDATA)
stream.stop_stream()