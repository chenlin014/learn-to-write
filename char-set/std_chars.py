import opencc, json

with open('ft-a.txt') as f:
    tchars = set(f.read().strip().split('\n'))

with open('jt-l1.txt') as f:
    schars = set(f.read().strip().split('\n'))

with open('jp.txt') as f:
    jchars = set(f.read().strip().split('\n'))

with open('old_to_new_kanjis.json') as f:
    o2nk = json.load(f)

t2s_converter = opencc.OpenCC('t2s.json')
t2j_converter = opencc.OpenCC('t2jp.json')

std_chars = list()

for char in tchars:
    std_chars.append((
        char,
        t2s_converter.convert(char),
        o2nk.get(char, t2j_converter.convert(char))
    ))

msc = schars.difference(set(s for _, s, _ in std_chars))
mjc = jchars.difference(set(j for _, _, j in std_chars))

with open('std_chars.csv', 'w') as f:
    f.write('\n'.join(
        ','.join(chars) for chars in std_chars
    ))

    f.write('\n\n')
    f.write('\n'.join(msc))

    f.write('\n\n')
    f.write('\n'.join(mjc))
