#!/usr/bin/env python3.5

# Fails both test set 1 and test set 2.

import fractions
import itertools
import math


if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        n = int(input())
        molecules = []
        wj_min = fractions.Fraction()
        wj_max = None
        failed = False
        for y in range(n):
            c1, j1 = map(int, input().split(" "))
            for c0, j0 in molecules:
                assert c0 < c1 or j0 < j1
                cd = c0 - c1
                jd = j1 - j0
                if jd == 0 or cd == 0:
                    continue
                f = fractions.Fraction(cd, jd)
                if jd > 0:
                    wj_min = max(wj_min, f)
                if jd < 0:
                    if wj_max is None:
                        wj_max = f
                    else:
                        wj_max = min(wj_max, f)
                if wj_max is not None and wj_min >= wj_max:
                    failed = True
                    break
                assert wj_max is None or wj_min < wj_max
            if failed:
                break
            molecules.append((c1, j1))
        if failed:
            print('Case #{}: IMPOSSIBLE'.format(x))
        else:
            for yc in itertools.count(1):
                yj = math.ceil(wj_min * yc)
                if yj == wj_min * yc:
                    yj += 1
                if wj_max is None or yj < wj_max * yc:
                    break
            print('Case #{}: {} {}'.format(x, yc, yj))
