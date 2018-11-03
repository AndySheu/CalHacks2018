from PIL import Image
import pytesseract
import bs4
import urllib.request
import re
import nltk
import heapq
import sys, os
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
from googlesearch import search

sys.stdout = open(os.devnull, 'w')
nltk.download('stopwords')
nltk.download('punkt')
sys.stdout = sys.__stdout__

def get_input():
    if len(sys.argv) > 1:
        text = str(sys.argv[1])
        for e in sys.argv[2:]:
            text += ' ' + str(e)
        return text.lower()
    else:
        return input('').lower()

def summarize(text, ref='', lines=7):
    text = re.sub(r'\[[0-9]*\]',' ',text)            
    text = re.sub(r'\s+',' ',text)    
    clean_text = text.lower()
    clean_text = re.sub(r'\W',' ',clean_text)
    clean_text = re.sub(r'\d',' ',clean_text)
    clean_text = re.sub(r'\s+',' ',clean_text)
    punkt_param = PunktParameters()
    punkt_param.abbrev_types = set(['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e'])
    sentence_splitter = PunktSentenceTokenizer(punkt_param)
    text = text.replace('?"', '? "').replace('!"', '! "').replace('."', '. "')
    sentences = sentence_splitter.tokenize(text)
    #sentences = nltk.sent_tokenize(text)
    stop_words = nltk.corpus.stopwords.words('english')

    word_count = {}
    for word in nltk.word_tokenize(clean_text):
        if word not in stop_words:
            word_count[word] = word_count.get(word, 0) + 1
    
    sentence_score = {}
    i = 0
    for s in sentences:
        for word in nltk.word_tokenize(s.lower()):
            if word in word_count.keys():
                old = sentence_score.get(s, (0, 0, i))
                i+=1
                sentence_score[s] = (old[0] + word_count[word], old[1] + 1, old[2])
    
    def score(pair):
        return (pair[0] - pair[2]) / pair[1]

    scores = {}
    for s in sentence_score.keys():
        if sentence_score[s][1] > 2:
            scores[s] = score(sentence_score[s])
        else:
            scores[s] = score(sentence_score[s]) - 100

    best_sentences = heapq.nlargest(lines, scores, key=scores.get)
    best_sentences.sort(key=lambda x: sentence_score[x][2])
    for s in best_sentences:
        if s[0] == ' ':
            s = s[1:]
        if 'refer' in s and len(scores.keys()) < 2:
            print('Please be more specific\n')
            if len(ref) > 1:
                print('Here are some suggestions:')
            for i in range(len(ref)):
                print("=>",ref[i])
            print('\n')
            return
        print(s)
    print('\n')

def image(img):
    text = pytesseract.image_to_string(Image.open(img))
    summarize(text)

def text_file(path):
    text = open(path, 'r').read()
    summarize(text)

def local(fi):
    end = fi.split('.')[-1]
    if end.lower() in ['bmp', 'pnm', 'png', 'jfif', 'jpeg', 'tiff']:
        image(fi)
    elif end.lower() in ['txt']:
        text_file(fi)
    else:
        print('Images must be: BMP, PNM, PNG, JFIF, JPEG, or TIFF')
        print('Text files must be: TXT')

def website(site):
    page = urllib.request.urlopen(site).read()
    soup = bs4.BeautifulSoup(page, 'lxml')
    text = ''
    for para in soup.find_all('p'):
        text += para.text
    ref = []
    for li in soup.find_all('li'):
        if ',' in li.text.lower() and 'last edited' not in li.text.lower() and 'text is available under the creative commons attribution-sharealike license' not in li.text.lower():
            ref.append(li.text.split('\n')[0])
    summarize(text, ref)

def topic(topic):    
    try:
        website('https://en.wikipedia.org/wiki/' + topic)
    except urllib.error.HTTPError:
        s = search(topic, num=1)
        site = next(s)
        print('Looking at:', site)
        website(site)

def main():
    i = get_input()
    if i == 'exit' or i == 'quit':
        os.system('clear')
        quit()
    elif i == 'clear':
        os.system('clear')
    elif '.' not in i:
        topic(i)
    else: 
        temp = i.split('.')
        parts = []
        for t in temp:
            parts += t.split('/')
        for d in ['com', 'edu', 'org', 'gov', 'net']:
            if d in parts:
                website(i)
                return
        local(i)
    if len(sys.argv) == 1:
        main()

main()
