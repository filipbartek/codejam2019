#!/usr/bin/env python3.5

# Passes test set 1 and fails test set 2.

import fractions


# We assume the weight of C is 1. We maintain a range estimate of weight of J.
def solve(unsorted, sortedmols=[], wj_min=fractions.Fraction(), wj_max=None):
    assert wj_max is None or wj_min < wj_max
    if len(unsorted) == 0:
        return 1
    answer = 0
    for i in range(len(unsorted)):
        unsorted_new = unsorted.copy()
        c1, j1 = unsorted_new.pop(i)
        wj_min_new = wj_min
        wj_max_new = wj_max
        failed = False
        for c0, j0 in sortedmols:
            if c0 >= c1 and j0 >= j1:
                failed = True
                break
            cd = c0 - c1
            jd = j1 - j0
            if jd == 0:
                continue
            f = fractions.Fraction(cd, jd)
            if jd > 0:
                wj_min_new = max(wj_min_new, f)
            if jd < 0:
                if wj_max_new is None:
                    wj_max_new = f
                else:
                    wj_max_new = min(wj_max_new, f)
            if wj_max_new is not None and wj_min_new >= wj_max_new:
                failed = True
                break
        if failed:
            continue
        sorted_new = sortedmols + [(c1, j1)]
        answer += solve(unsorted_new, sorted_new, wj_min_new, wj_max_new)
    return answer


if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        n = int(input())
        molecules = []
        for y in range(n):
            c, j = map(int, input().split(" "))
            molecules.append((c, j))
        y = solve(molecules)
        print('Case #{}: {}'.format(x, y))
