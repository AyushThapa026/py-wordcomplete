import requests
import time

_wait = 0.5

def get_freq(term):
    response = None
    while True:
        try:
            response = requests.get('https://api.datamuse.com/words?sp='+term+'&md=f&max=1').json()
        except:
            print('Could not get response. Sleep and retry...')
            time.sleep(_wait)
            continue
        break;

    freq = 0.0 if len(response)==0 else float(response[0]['tags'][0][2:])
    return freq


file = open('popular.txt', 'r')
freq = open('freq.txt', 'w')


for x in range(50):
    word = file.readline()
    freq.write(str(get_freq(word)) + "\n")