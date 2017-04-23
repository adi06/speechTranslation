#!/usr/bin/env python

import json
from os.path import join
from os.path import dirname
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud import SpeechToTextV1


def text2Speech(inputText, outputAudioFile=None):
    # load credential file
    with open(join(dirname(__file__), 'text2speech.json')) as jsonFile:
        jsonString = jsonFile.read()

    try:
        credentials = json.loads(jsonString)
    except ValueError, ve:
        raise ve

    # prepare request
    text_to_speech = TextToSpeechV1(username=credentials['username'],
                                    password=credentials['password'],
                                    x_watson_learning_opt_out=True)

    if outputAudioFile is None:
        outputAudioFile = 'output.wav'

    with open(join(dirname(__file__), outputAudioFile), 'wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(inputText,
                                                   accept='audio/wav',
                                                   voice="en-US_AllisonVoice"))

def speech2Text(audioFile):
    # load credential file
    with open(join(dirname(__file__), 'speech2text.json')) as jsonFile:
        jsonString = jsonFile.read()

    try:
        credentials = json.loads(jsonString)
    except ValueError, ve:
        raise ve

    speech_to_text = SpeechToTextV1(username=credentials['username'],
                                    password=credentials['password'],
                                    x_watson_learning_opt_out=False)

    with open(join(dirname(__file__), audioFile), 'rb') as audio_file:
        response = speech_to_text.recognize(audio_file,
                                            content_type='audio/wav',
                                            timestamps=True,
                                            word_confidence=True)

        text = response['results'][0]['alternatives'][0]['transcript']
        return text


