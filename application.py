from flask import Flask, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application=app = Flask(__name__)
app.config['SECRET_KEY'] = 'fakenews'

@app.route('/')
def index():
    return '<h1> Hello World!</h1>'

@app.route('/<text>', methods=['GET'])
def detemineValidity(text):
    # Model loading
    loaded_model = None
    with open('basic_classifier.pkl','rb') as fid:
        loaded_model = pickle.load(fid)
    vectorier = None
    with open('count_vectorizer.pkl','rb') as vd:
        vectorier = pickle.load(vd)
    #Using model to predict
    prediction = loaded_model.predict(vectorier.transform([text]))[0]
    response = jsonify(prediction)
    return response

if __name__ == "__main__":
    app.run()