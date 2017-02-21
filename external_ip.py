#!/bin/bash
"""
Simple script stub that texts your ip address
"""
import json
import requests
from twilio.rest import TwilioRestClient

# Change ID, Token, and Numbers
accountSID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
authToken = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+18005550103'
myCellPhone = '+18005550100'

external_ip = requests.get('http://whatismyip.akamai.com/')
external_ip.raise_for_status()

# external_ip.json used for persistence 
# Make sure path is correct
with open('external_ip.json', 'r') as f:
    stored_ip = json.load(f)

if stored_ip != external_ip.text:
    message = twilioCli.messages.create(body=external_ip.text, from_=myTwilioNumber, to=myCellPhone)

    # Fix path here too
    with open('external_ip.json', 'w') as f:
        json.dump(external_ip.text, f)
