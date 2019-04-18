#!/usr/bin/env python3.5

if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        n = int(input())
        p = input()
        assert len(p) == 2 * n - 2
        y = []
        for step in p:
            if step == 'E':
                y.append('S')
            else:
                y.append('E')
        y = ''.join(y)
        print('Case #{}: {}'.format(x, y))
