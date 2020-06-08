# -*- coding:utf-8 -*-
import requests
import json

api_url = "https://localhost:5000/split_words"
# api_url = "http://localhost:5000/split_words"

request_para_correct = {
    'text' : '中村さんと中居正広の金曜日のスマたちへ逃げ恥，新垣結衣を見た．美しい今日は綺麗なラーメンを食べたい．'
    ,'word_classes': ['名詞', '動詞', '形容詞']  ## correct key name
}
request_para_invalid = {
    'text' : '中居正広の金曜日のスマたちへ逃げ恥，新垣結衣を見た．今日はラーメンを食べたい．'
    ,'word_class': ['名詞', '動詞']  ## invaid key name
}

def callAPI(request_para):
    ##自己署名証明書を許容
    res = requests.post(api_url, json=request_para, verify=False)
    print(res)
    print(res.json())

if __name__ == "__main__":
    print('call API with correct parameters')
    callAPI(request_para_correct)

    print('\ncall API with invalid parameters')
    callAPI(request_para_invalid)