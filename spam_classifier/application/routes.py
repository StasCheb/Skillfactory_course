from flask import Flask, request
from application import app
from flask import request, jsonify
from spam_classifier import Filter
import pickle

@app.route('/classify_text', methods=['POST'])
def classify_text():    
    with open('data.pickle', 'rb') as f:
        model = pickle.load(f)
    data = request.json
    text = data.get('text') 
    if text is None:
        params = ', '.join(data.keys()) 
        return jsonify({'message': f'Parametr "{params}" is invalid'}), 400 
    else:
        result = model.classify(text)
        return jsonify({'result': result})