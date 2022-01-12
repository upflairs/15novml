from flask import Flask, render_template, request
import pandas as pd
import nltk
from nltk.corpus import stopwords as sw
from string import punctuation as punc
import re

app = Flask( __name__ )

def text_process(txt):
    sentences = nltk.sent_tokenize(txt.lower())
    words = []
    for sentence in sentences:
        s = ' '.join(i for i in sentence.split() if (i not in sw.words('english')) and (re.fullmatch(r'[a-zA-Z0-9]+',i)))
        words += [i.strip("'") for i in nltk.word_tokenize(s) if i not in sw.words('english') and i not in punc]    
    jw = ' '.join(words)
    jw = ''.join([i for i in jw if (i.isalpha() or i==' ') and i.isascii()]).split()
    return jw

@app.route('/', methods = ['get','post'])
def index_page():
    result = ''
    if request.method == 'POST':
        m = request.form['msg']
        model = pd.read_pickle('spampredictor.pkl')
        result = model.predict([m])[0]
    return render_template('index.html', prediction = result)


if __name__ == '__main__':
    app.run(debug = True)
    
# pythonanywhere.com

























"""
@app.route('/sample')
def abc():
    return "Wow"

@app.route('/new')
def xyz():
    return "it is another page created on flask"

@app.route('/test')
def pqr():
    return '''
    <html>
        <head><title>Flask Page</title></head>
        <body>
            <h1>Test Page</h1>
            <p>It is a test page for Flask and html code</p>
        </body>
    </html>
'''

"""