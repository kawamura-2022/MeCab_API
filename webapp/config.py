import MeCab
# path_mecab_dic = "-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd"
path_mecab_dic = "-d ./mecab-ipadic-neologd_ec2"  ##we cannnot install from official site, because there is no memory(2GB) in 't2.micro'
tagger = MeCab.Tagger(path_mecab_dic)

need_keys  = ['text', 'word_classes']