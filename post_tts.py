import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/pMsXgVXv3BLzUgSXRplE"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "some api key"
}

data = {
    "text": "Born and raised in the charming south",
     "I can add a touch of sweet southern hospitality"
    "to your audiobooks  podcasts"
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
    }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
