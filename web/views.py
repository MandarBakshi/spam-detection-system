from flask import Blueprint, request, url_for, render_template, redirect
import pickle

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def DetectSpam():
    if request.method == 'POST':
        text = request.form.get('text')
        vectorizer = pickle.load(open('./web/models/TfidfVectorizerModel.model', 'rb'))
        classifier = pickle.load(open('./web/models/SpamClassifierSimple.model', 'rb'))
        text1 = [text]
        text_converted = vectorizer.transform(text1)
        y = classifier.predict(text_converted)
        result = y[0]
        return render_template('home.html', result = result)
    else:
        return render_template('home.html', result = None)