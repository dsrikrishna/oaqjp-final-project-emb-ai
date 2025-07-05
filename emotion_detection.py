'''
Main module for emotion detection
'''
import json
import requests


def emotion_detector(text_to_analyse):
    ''' Emotion Detection using IBM Watson NLP Library
    '''

    url = ("https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url,json=input_json,headers=headers,timeout=500)
    if response.status_code == 500:
        output = {'anger':None,
         'disgust':None,
         'fear':None,
         'joy':None,
         'sadness':None,
         'dominant_emotion':None}
    else:
        emotion_dict = response.json()['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_dict,key=emotion_dict.get)
        output = emotion_dict
        output['dominant_emotion'] = dominant_emotion
    return output 