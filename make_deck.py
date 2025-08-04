import csv, yaml
from tqdm import tqdm

HINT_QUOTA = 3
HINT_DELIM = '、'

with open('char-set/std_common_chars.yaml') as f:
    std_common_chars = yaml.safe_load(f)

with open('word-list/essay_zhuyin.txt') as f:
    reader = csv.reader(f, delimiter='\t')
    ft_table = [(word, pinyin.split(" "), int(freq)) for word, pinyin, freq in
        reader if len(word) >= 2]

ft_table.sort(reverse=True, key=lambda row: (1 / len(row[0]), row[2]))

with open('word-list/现代汉语常用词表.txt') as f:
    reader = csv.reader(f, delimiter='\t')
    jt_table = [(word, pinyin.split("'"), int(freq)) for word, pinyin, freq in
        reader if len(word) >= 2]

jt_table.sort(reverse=False, key=lambda row: (len(row[0]), row[2]))

with open('zh_deck.csv', 'w') as f:
    std_chars_tqdm = tqdm(std_common_chars['ft']+std_common_chars['jt_patch'])
    for ft_char, jt_char, jp_char in std_chars_tqdm:

        row = [ft_char, jt_char, jp_char]

        hints = list()
        for word, pinyin, _ in ft_table:
            if not ft_char in word:
                continue
            hints.append(''.join(
                (yin if char == ft_char else char) for char, yin in
                    zip(word, pinyin)
            ))
            if len(hints) >= HINT_QUOTA:
                break
        row.append(HINT_DELIM.join(hints))

        hints = list()
        for word, pinyin, _ in jt_table:
            if not jt_char in word:
                continue
            hints.append(''.join(
                (yin if char == jt_char else char) for char, yin in
                    zip(word, pinyin)
            ))
            if len(hints) >= HINT_QUOTA:
                break
        row.append(HINT_DELIM.join(hints))

        f.write(','.join(row)+'\n')
