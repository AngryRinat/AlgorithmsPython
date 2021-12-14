from collections import Counter, namedtuple
import hashlib
import heapq




#Задача№1.
def search(str1: str, str2: str) -> int:
    len_sub = len(str2)
    h_sub = hashlib.sha1(str2.encode('utf-8')).hexdigest()
    counter = 0
    for i in range(len(str1) - len(str2) + 1):
        if h_sub == hashlib.sha1(str1[i:i + len_sub].encode('utf-8')).hexdigest():
            counter += 1
    return counter

#Задача№2
def haffm(a_string: str):
    h = []
    haf_dict = Counter(a_string)
    for ch,freq in haf_dict.items():
        h.append((freq,ch))

    heapq.heapify(h)

    return h


if __name__ == '__main__':
    sample = 'abracadabra'
    ref = 'bra'

    print(search(sample,ref))

    a = 'what a wonderfull word'
    print(haffm(a))


