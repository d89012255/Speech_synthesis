"""
Example code for yating tts api call.
"""

from yating_tts_sdk import YatingClient as ttsClient

URL = "https://tts.api.yating.tw/v2/speeches/short"
KEY = "f6f3f72c9f9a316e03abe2bd17c8172ab4ab8fcc"


TEXT = "紀錄"
TEXT_TYPE = ttsClient.TYPE_TEXT
MODEL = ttsClient.MODEL_ZHEN_FEMALE_1
SPEED = 1.0
PITCH = 1.0
ENERGY = 1.0
ENCODING = ttsClient.ENCODING_LINEAR16
SAMPLE_RATE = ttsClient.SAMPLE_RATE_16K
single_sound = 0

for i in range(5):
    FILE_NAME = "example"+ str(i+1+single_sound*5)

    try:
        client = ttsClient(URL, KEY)
        client.synthesize(TEXT, TEXT_TYPE, MODEL, SPEED, PITCH, ENERGY, ENCODING, SAMPLE_RATE, FILE_NAME)
    except Exception as err :
        print("An exception occurred:", err)
