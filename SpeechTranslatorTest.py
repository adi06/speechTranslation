#!/usr/bin/env bash

from SpeechTranslatorUtil import text2Speech
from SpeechTranslatorUtil import speech2Text

if __name__ == '__main__':
    #output.wav file is generated in current working directory
    text2Speech('Is the corridor blocked')

    print speech2Text('output.wav')
