# -*- coding:utf-8 -*-
class WordProcessing:
    def __init__(self, tagger):
        self.res_dic = {}
        self.tagger = tagger

    def morphological(self, text, word_class):
        node = self.tagger.parseToNode(text)

        i=0
        while node:
            word_feature = node.feature.split(',')
            if (word_feature[6] != '*') and (word_feature[0] in word_class):
                self.res_dic[str(i)] = [word_feature[6], word_feature[0]]
            i+=1
            node = node.next


    def set_res_dic(self, text, word_classes):
        for word_class in word_classes:
            self.morphological(text, word_class)


if __name__ == "__main__":
    word_classes = ['名詞', '動詞']
    text = '中居正広の金曜日のスマたちへ逃げ恥，新垣結衣へ見た'

    import MeCab
    m = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    wp = WordProcessing(m)
    wp.set_res_dic(text, word_classes)

    print(wp.res_dic)
    print(m.parse (text))