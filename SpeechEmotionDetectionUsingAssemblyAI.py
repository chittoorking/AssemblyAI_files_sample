import json
import requests
import pprint
from credentials import *
api_key ='Replace with your api key'

#Replace id with id that you copy fom credentials.py output
TRANSCRIPT_ENDPOINT='https://api.assemblyai.com/v2/transcript/id'

response=requests.get(
    TRANSCRIPT_ENDPOINT,
    headers={'authorization':api_key}
)
response_json = response.json()
print(pprint.pprint(response_json))
