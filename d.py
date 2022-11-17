import requests
import re

if __name__ == '__main__':
    s = 'Например, для onclick="CallJSFunction()", где CallJSFunction - это и будет название функц'
    r = requests.get('https://netology.ru/')
    s = set(re.findall(r'\son\w*', str(r.content)))
    print(s)