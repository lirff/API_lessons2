import requests

KEY = 'trnsl.1.1.20200517T174409Z.b00469147e596552.aaffd35b6cb8df000fab49eb20426988fbe72860'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_me(mytext):
    params = {
        'key': KEY,
        'text': mytext,
        'lang': 'ru-fr'
    }
    response = requests.get(URL, params=params)
    return response.json()


json = translate_me('Привет, друг!')
print(json['text'])
print(' '.join(json['text']))

