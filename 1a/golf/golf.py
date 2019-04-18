#!/usr/bin/env python3.5

import sys

import numpy as np

# I finally submitted solution with the values [17, 13, 11, 7, 5, 3, 2].
# That solution fails for large m.
# I didn't manage to submit the following values in time.
primes = [18, 17, 16, 15, 14, 13, 11]

if __name__ == '__main__':
    t, n, m = map(int, input().split())
    # t is 20
    # n is 365 or 7
    # m is 100 or 10 ** 6
    for x in range(1, t + 1):
        options = np.ones(m + 1, dtype=np.bool)
        options[0] = False
        for i in range(max(n, len(primes))):
            d = primes[i]
            b = [d] * 18
            print(' '.join(map(str, b)))
            sys.stdout.flush()
            p = np.array(list(map(int, input().split())), dtype=np.int)
            assert len(p) == 18
            # Now we know that g = sum_i(p[i] % b[i])
            s = np.sum(p)
            options[:s] = False
            sm = s % d
            # print(x, i, d, s, file=sys.stderr)
            options[np.arange(m + 1) % d != sm] = False
            if np.count_nonzero(options) <= 1:
                assert np.count_nonzero(options) == 1
                break
        g = np.nonzero(options)[0][0]
        print(g, file=sys.stderr)
        print(g)
        answer = int(input())
        if answer != 1:
            break
