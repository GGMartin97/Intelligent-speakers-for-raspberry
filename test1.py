# -*- coding: utf-8 -*-

import pyaudio
import wave
import sys
import wav2pcm

# setting
CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=16000
RECORD_SECONDS=5

# WORKING

if len(sys.argv)<2:
    print("please input")
    sys.exit(-1)

filename=sys.argv[1]


def rec(filename):
    p=pyaudio.PyAudio()

    stream=p.open(format=FORMAT,
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  frames_per_buffer=CHUNK
    )
    print('recording...')

    frames = []

    for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("ok")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf=wave.open(filename,'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__=='__main__':

    rec(filename)
    wav2pcm.wav_to_pcm(filename)
