# -*- coding:utf-8 -*-
from config import tagger, need_keys
from morphlogical import WordProcessing
from my_debug import exist_key

from flask import Flask, request, jsonify, Blueprint
import json
import traceback

app = Flask(__name__)

@app.route("/split_words", methods=["POST"])
def split_words():
    response = {'resCode': '500','message': ''}
    given_json = request.json
    try:
        exist_key(given_json, need_keys)
        text, word_classes = given_json['text'], given_json['word_classes']
        wp = WordProcessing(tagger)
        wp.set_res_dic(text, word_classes)
        response['split_data'] = wp.res_dic
        response.update(resCode='200')
    except:
        traceback.print_exc()
        response.update(message=traceback.format_exc())
        return response

    print(response)
    return response

if __name__ == "__main__":
    print(" * Flask starting server...")
    app.run(debug=False, host='0.0.0.0', port=5000)