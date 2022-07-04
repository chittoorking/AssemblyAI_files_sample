import json
import requests
import pprint
from credentials import *
api_key = '50c7e0e64e2f4e77a9ae2717adebb557'
# 50c7e0e64e2f4e77a9ae2717adebb557

TRANSCRIPT_ENDPOINT='https://api.assemblyai.com/v2/transcript'

response=requests.post(
    TRANSCRIPT_ENDPOINT,
    headers={'authorization':api_key,'content-type':'application/json'},
    json ={
        'audio_url':"https://nicetalkingwithyou.com/wp-content/uploads/2018/07/003NTWY_U1_CL.mp3",
        'sentiment_analysis':True,
    }
)
response_json = response.json()
print(pprint.pprint(response_json))
# ojg4m0f8y9-b434-48a7-9bd7-d548391a92b5