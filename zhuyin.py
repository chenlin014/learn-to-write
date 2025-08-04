import sys, os
sys.path.append(
    os.path.dirname(os.path.abspath(__file__)) + '/bopomofo'
)

from main import trans_sentense

try:
    _, word_list = sys.argv
except Exception:
    print(f'Usage: {sys.argv[0]} <word-list>')
    sys.exit()

try:
    file = open(word_list)
except OSError:
    print(f'Cannot open "{word_list}"')
    sys.exit()

word_table = (row.split('\t') for row in
    file.read().splitlines())
file.close()

print('\n'.join(
    ('\t'.join(
        [word, trans_sentense(word)]+extra_info
    ) for word, *extra_info in word_table)
).replace(' \t', '\t').replace('\t ', '\t'), end='')
