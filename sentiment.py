import requests,json

def getsentiment(text):
    url = "https://api.meaningcloud.com/sentiment-2.1"

    text = input("Input text:")
    payload={
        'key': '3eac26cb5eb5567b948bab87c8290300',
        'txt': text,
        'lang': 'en',  # 2-letter code, like en es fr ...
    }

    response = requests.post(url, data=payload)

    print('Status code:', response.status_code)
    data = response.json()
    return (data['score_tag']['agreement']['confidence'])




"""
def getSentiment(text):
    url = "https://api.meaningcloud.com/sentiment-2.1"
    payload={
    'key': '3eac26cb5eb5567b948bab87c8290300',
    'txt': text,
    'lang': 'en',  # 2-letter code, like en es fr ...
    }
    

    response= requests.post(url,data=payload)
    dict(json.loads(response.text))
    return 

"""
