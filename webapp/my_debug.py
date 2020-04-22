# -*- coding:utf-8 -*-
import traceback

def exist_key(target_dict, need_keys):
    for need_key in need_keys:
        if need_key in target_dict.keys():
            print(need_key, ' is exist')
        else:
            raise ValueError("必要なkey値が存在しません．存在しないkey値 -> ", need_key)


if __name__ == "__main__":
    need_keys  = ['text', 'word_classes']
    try:
        given_json = {'text' : 'temp', 'word_classe': ''}
        exist_key(given_json, need_keys)
    except:
        traceback.print_exc()