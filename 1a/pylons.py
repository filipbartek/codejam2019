#!/usr/bin/env python3.5

import itertools


def solve(remaining, prev=None):
    if len(remaining) == 0:
        return []
    for cur in remaining:
        if prev is not None:
            if cur[0] == prev[0] or cur[1] == prev[1] or cur[0] - cur[1] == prev[0] - prev[1] or cur[0] + cur[1] == \
                    prev[0] + prev[1]:
                continue
        path = solve(remaining - {cur}, cur)
        if path is not None:
            return path + [cur]
    return None


if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        r, c = map(int, input().split())
        remaining = set(itertools.product(range(r), range(c)))
        path = solve(remaining)
        if path is None:
            print('Case #{}: IMPOSSIBLE'.format(x))
        else:
            print('Case #{}: POSSIBLE'.format(x))
            for pos in path:
                print('{} {}'.format(pos[0] + 1, pos[1] + 1))
