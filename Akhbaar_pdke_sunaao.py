import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == '__main__':

    speak("Today's news")
    # url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=29e9d8bb14544005a896438f0482834a"
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ebac50e051dd4226a18986d4c957b65d"
    n=requests.get(url).text
    n_dict = json.loads(n)
    a = n_dict['articles']
    for article in a:
        speak(article['title'])
        print(article['title'])

    speak("Thanks for listening")
