#!/usr/bin/env python3.5

def process(words):
    categories = dict()
    for w in words:
        if len(w) == 0:
            continue
        suf = w[-1:]
        if suf not in categories:
            categories[suf] = set()
        assert w[:-1] not in categories[suf]
        categories[suf].add(w[:-1])
    y = 0
    for category in categories.values():
        if len(category) < 2:
            continue
        if len(category) <= 3:
            y += 2
        else:
            bonus = process(category)
            y += bonus
            remaining = len(category) - bonus
            if remaining >= 2:
                y += 2
    return y


if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        n = int(input())
        words = set()
        max_len = 0
        for i in range(n):
            w = input()
            assert w not in words
            words.add(w)
            max_len = max(max_len, len(w))
        y = process(words)
        print('Case #{}: {}'.format(x, y))
