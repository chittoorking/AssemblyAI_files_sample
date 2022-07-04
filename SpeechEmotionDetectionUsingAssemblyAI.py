import json
import requests
import pprint
from credentials import *
api_key ='50c7e0e64e2f4e77a9ae2717adebb557'
# 50c7e0e64e2f4e77a9ae2717adebb557

TRANSCRIPT_ENDPOINT='https://api.assemblyai.com/v2/transcript/ojg1fpq6k9-6bf8-4bda-8c88-b7ab303c13f8'

response=requests.get(
    TRANSCRIPT_ENDPOINT,
    headers={'authorization':api_key}
)
response_json = response.json()
print(pprint.pprint(response_json))
# ojg102hu79-5a09-43c3-a9cd-242f5d8bcb64