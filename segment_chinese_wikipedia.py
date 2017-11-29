import jieba
import os
import sys
from collections import Counter


def frequency_analysis_multiple_files(directory):
    files_for_analysis = [file_name for file_name in os.listdir(directory) if file_name[-4:] == '.txt']

    frequency_count = Counter()

    for text_file in files_for_analysis:
        print(text_file)
        with open('wiki_data/'+text_file, encoding='utf8') as f:
            for line in f:
                seg_list = jieba.cut(line, cut_all=True)
                frequency_count.update(item for item in seg_list)

    return frequency_count


def write_freq_dist_file(counter_dictionary, title):
    with open(title + '_frequency.txt', 'w', encoding='utf8') as f:
        for word, freq in counter_dictionary.most_common():
            print(word, freq)
            f.write(str(freq) + ' ' + word + '\n')
    print(len(counter_dictionary.most_common()))


if __name__ == '__main__':
    total_counts = frequency_analysis_multiple_files(sys.argv[1])
    write_freq_dist_file(total_counts, sys.argv[1])
