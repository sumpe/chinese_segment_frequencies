import jieba
import os
from collections import Counter

wiki_files = [f for f in os.listdir('wiki_data') if f[-4:] == '.txt']

count = Counter()

print(wiki_files)
c = 0

for wiki_file in wiki_files:
    print(wiki_file)
    c += 1
    print(c)
    with open('wiki_data/'+wiki_file, encoding='utf8') as f:
        for line in f:
            seg_list = jieba.cut(line, cut_all=True)
            count.update(item for item in seg_list)

with open('output.txt', 'w', encoding='utf8') as f:
    for word, freq in count.most_common():
        print(word, freq)
        f.write(str(freq) + ' ' + word + '\n')

print(len(count.most_common()))
