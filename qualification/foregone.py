#!/usr/bin/env python3.5

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        a = list(n)
        b = []
        start = 0
        while start < len(n):
            pos = n.find('4', start)
            if pos == -1:
                b.extend(['0'] * (len(n) - start))
                break
            a[pos] = '3'
            if len(b) > 0:
                b.extend(['0'] * (pos - start))
            b.append('1')
            start = pos + 1
        a = ''.join(a)
        b = ''.join(b)
        print('Case #{}: {} {}'.format(i + 1, a, b))
