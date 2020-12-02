# Auth imports
import base64

# Standard imports to get API responses
import requests
import json 

# My credentials import
from secrets import CLIENTID
from secrets import CLIENTSECRET

trackId = '0JJP0IS4w0fJx01EcrfkDe'

"""
The JSON auth response looks like this:
{
    'access_token': 'YOURTOKENHERE', 
    'token_type': 'Bearer', 
    'expires_in': 3600, 
    'scope': ''
}
"""

def auth():
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}
    message = f'{CLIENTID}:{CLIENTSECRET}'
    
    # Base 64 encode
    messageBytes = message.encode('ascii')
    base64bytes = base64.b64encode(messageBytes)
    base64Message = base64bytes.decode('ascii')
    headers['Authorization'] = f'Basic {base64Message}'
    data['grant_type'] = "client_credentials"
    result = requests.post(url, headers=headers, data=data)
    token = result.json()['access_token']
    return token

# Check the testResponse Json for further reference

def getTrack(trackId):
    token = auth()
    spotifyTrackUrl = f'https://api.spotify.com/v1/tracks/{trackId}'
    headers = {
        "Authorization" : "Bearer " + token
    }   
    response = requests.get(url=spotifyTrackUrl, headers=headers).json()
    return response

# Get current playing track
def getCurrentTrack():
    token = auth()
    currentTrackUrl = 'https://api.spotify.com/v1/me/player'
    headers = {
        "Authorization" : "Bearer " + token
    } 
    response = requests.get(url=currentTrackUrl, headers=headers).json()
    return response

# Test album albumId = '0UtenXp3qVbWedKEaNRAp9'
def getAlbum(albumId):
    token = auth()
    albumUrl = f'https://api.spotify.com/v1/albums/{albumId}'
    headers = {
        "Authorization" : "Bearer " + token
    }  
    response = requests.get(url = albumUrl, headers = headers).json()
    return response
