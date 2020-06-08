# テキスト分割　API
自然言語処理を利用し，テキストから指定された品詞を抜き出します．

（低メモリのサーバでの動作を想定しているので，MeCabの辞書は別途ダウンロードする必要があります．）

## ファイル構成
``` bash
webapp/        ---- source code
|
|- app.py ---- API 実行ファイル
|- config.py ---- 設定ファイル
|- morphlogical.py ----- 形態素解析クラス
|- my_debug.py ----- エラー処理用の関数
|- requirements.txt
|
my_conf/
|
|-server.crt  ---- 証明書(公開鍵)
|-server.key ---- 秘密鍵
|
Dockerfile
docker-compose.yml
README.md
test_api.py  ---- API の動作テスト
```
## 使用方法
1. YAMLがあるフォルダまで移動
``` bash
$ cd /var/www/MeCab_API
```
2. mecab-ipadic-neolog の辞書を https://github.com/neologd/mecab-ipadic-neologd を参考にダウンロード

3. mecab-ipadic-neolog の辞書をwebappのフォルダに移動
```
$ mv 'mecab-ipadic-neologの辞書' ./webapp/
```
4. MeCab の辞書をconfig.py のpath_mecab_dicの変数で指定
```
$ vi webapp/config.py

import MeCab
path_mecab_dic = "-d ./mecab-ipadic-neologd"
tagger = MeCab.Tagger(path_mecab_dic)

need_keys  = ['text', 'word_classes']
```
5. 自己署名証明書を作成(このステップを飛ばす場合は，YAMLの中身を書き換える)
```
$ openssl genrsa 2048 > server.key
$ openssl req -new -key server.key > server.csr
$ openssl x509 -days 3650 -req -signkey server.key < server.csr > server.crt
```
6. API 起動
```
$ docker-compose up -d
```
## API URL
https://localhost:5000/split_words


## 入力
| key | 説明 |
| --- | --- |
| text |　対象のテキスト |
| word_classes |　抽出したい品詞のリスト |

```json
{
    'text' : '中村さんと中居正広の金曜日のスマたちへ逃げ恥，新垣結衣を見た．美しい今日は綺麗なラーメンを食べたい．'
    ,'word_classes': ['名詞', '動詞', '形容詞']
}
```

## 出力
| 返り値 | 説明 |
| --- | --- |
| resCode | レスポンス コード |
| message | レスポンス メッセージ |
| split_data | 分割された単語と品詞 |

### resCode
| resCode | ステータス | 説明 |
| --- | --- | --- |
| 200 | 成功 | 対象テキストの分割成功 |
| 500 | エラー |  内部エラー |
```json
{
    'resCode': '200'
    ,'message': ''
    ,'split_data': {'1': ['中村', '名詞'], '12': ['美しい', '形容詞'], '13': ['今日', '名詞'], '15': ['綺麗', '名詞'], '17': ['ラーメン', '名詞'], '19': ['食べる', '動詞'], '2': ['さん', '名詞'], '4': ['中居正広の金曜日のスマたちへ', '名詞'], '5': ['逃げ恥', '名詞'], '7': ['新垣結衣', '名詞'], '9': ['見る', '動詞']}
}
```
