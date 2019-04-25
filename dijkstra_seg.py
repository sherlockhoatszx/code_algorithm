words ={'我','去','天','安','门','天安门'}
def get_DAG(sentence):

    DAG = {}
    N = len(sentence)
    for k in range(N):
        print('k is ',k)
        tmplist = []
        i = k
        frag = sentence[k]
        while i < N and frag in words:
            print('i is',i)

            tmplist.append(i)
            print(tmplist)
            i += 1
            frag = sentence[k:i + 1]
            print('frag',frag)
        if not tmplist:
            tmplist.append(k)
        DAG[k] = tmplist
    return DAG
print(get_DAG('我去天安门'))

import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise "Must be using Python 3"
else:
    unicode = str

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-11:22:32:26"


default_dictionary = dict({
    "苦": [40, 'nz'],
    "苦尽": [10, 'nz'],
    "苦尽甘": [10, 'nz'],
    "苦尽甘来":[10, 'nz']
})

def get_DAG(sentence, dictionary=default_dictionary):
    import pdb
    pdb.set_trace()
    DAG, N = {}, len(sentence)
    for k in range(N):
        suffix, i = [], k
        word = sentence[k]
        while i < N and word in dictionary:
            if dictionary[word][0] > 0:
                suffix.append(i)
            i += 1
            word = sentence[k:i + 1]
        if len(suffix) == 0:
            suffix.append(k)
        DAG[k] = suffix
    return DAG

def main():
    sentence = "是苦尽甘来"
    import pdb
    pdb.set_trace()
    lis = [x for x in sentence]

    print(str(lis) + '\n' + str(get_DAG(sentence)))

if __name__ == '__main__':
    main()
