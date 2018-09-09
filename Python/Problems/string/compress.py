import collections

def compress(chars):
    compressed = collections.Counter(chars)
    cnt = 0
    for letter in compressed:
        if (compressed[letter]) > 1:
            cnt += 2
        else:
            cnt += 1
    return cnt


print(compress(["a","a","b","b","c","c","c"]))