from itertools import *
import sys

word = 'сон'
with open('rusnouns.txt', 'rb') as rusnouns:
    target = rusnouns.read().decode("UTF-8")
    target = target.splitlines()
target = [item for item in target if len(item) == len(word)]
target = set(target)

superdata = permutations(list(word))

def join_next_word(next_word):
    return ''.join(next_word)

def find_words(data, target):
    data = [join_next_word(item) for item in data]
    data = set(data)
    if 'спаниель' in data:
        print('app')
    res = data & target
    return res


result = set()
start = 0
step = 2
data = set('t')

while len(data):
    stop = start + step
    print(start, stop)
    data = set(islice(superdata, start, stop+1))
    upd = find_words(data, target)
    if upd:
        print(upd)
        result.update(upd)
    start = stop

print(result)
