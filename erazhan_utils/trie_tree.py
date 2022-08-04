# -*- coding = utf-8 -*-
# @time: 2022/2/23 5:42 下午
# @Author: erazhan
# @File: trie_tree.py

# ----------------------------------------------------------------------------------------------------------------------

class TrieTree(object):
    """
    Trie 树的基本方法，用途包括：
    - 前向最大匹配计算
    - 繁简体词汇转换的前向最大匹配计算
    """

    def __init__(self):
        self.dict_trie = dict()
        self.depth = 0

    def add_node(self, word, typing):
        """
        向 Trie 树添加节点
        :param word: 字典中的词汇
        :param typing: 词汇类型
        :return: None
        """
        word = word.strip()
        if word not in ['', '\t', ' ', '\r']:
            tree = self.dict_trie
            depth = len(word)
            word = word.lower()  # 将所有的字母全部转换成小写
            for char in word:
                if char in tree:
                    tree = tree[char]
                else:
                    tree[char] = dict()
                    tree = tree[char]
            if depth > self.depth:
                self.depth = depth
            tree['type'] = typing

    def build_trie_tree(self, dict_list, typing):
        """ 创建 trie 树 """
        for word in dict_list:
            self.add_node(word, typing)

    def search(self, word):
        tree = self.dict_trie
        res = None
        step = 0  # step 计数索引位置
        for char in word:
            if char in tree:
                tree = tree[char]
                step += 1
                if 'type' in tree:
                    res = (step, tree['type'])
            else:
                break
        if res:
            return res
        return 1, None


class TrieFind(object):

    def __init__(self, dict_list):
        self.trie_tree_obj = TrieTree()
        for typing, entity_list in dict_list.items():
            self.trie_tree_obj.build_trie_tree(entity_list, typing)

    def __call__(self, text):

        record_list = list()
        i = 0
        text_length = len(text)

        while i < text_length:
            pointer_orig = text[i: self.trie_tree_obj.depth + i]
            pointer = pointer_orig.lower()
            step, typing = self.trie_tree_obj.search(pointer)
            print("st", step, typing)
            if typing is not None:
                record = {
                    'type': typing,
                    'text': pointer_orig[0: step],
                    'offset': [i, step + i]}
                record_list.append(record)
            i += step

        return record_list

    def search(self, word):

        tree = self.trie_tree_obj.dict_trie
        step = 0
        word = word.lower()
        for char in word:
            # print("char,", step, char, len(word))
            if char in tree:
                step += 1
                tree = tree[char]
                if "type" in tree and step == len(word):
                    return True
            else:
                return False
        return False


if __name__ == '__main__':
    '''利用字典树判断实体是否在提供的字典中'''
    L = ["没得高血压", "没高血压", "没高血"]

    neg_tree = TrieFind({"否定词": L})

    for one_ent in L:
        a = neg_tree.search(one_ent)
        if a is False:
            print(one_ent)

    entity = "没高血压的"
    a = neg_tree.search(entity)
    print(a)