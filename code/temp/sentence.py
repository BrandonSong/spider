# 迭代对象时, 会自动调用iter()
# 可迭代的对象和迭代器的关系：Python 从可迭代的对象中获取迭代器


import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('"The time has come," the Walrus said,')
print(s)

for word in s:
    print(word)