#!/usr/bin/env python3.5

if __name__ == '__main__':
    t = int(input())
    for x in range(1, t + 1):
        n, l = map(int, input().split(" "))
        cipher_values = list(map(int, input().split(" ")))
        value_0 = cipher_values[0]
        value_1 = cipher_values[1]
        factor = None
        if value_0 % 2 == 0:
            factor = 2
        elif value_0 % 3 == 0:
            factor = 3
        else:
            sieve_begin_first = 4
            sieve_len = 6
            sieve_indices = [1, 3]
            for sieve_begin in range(sieve_begin_first, value_0, sieve_len):
                for sieve_pos in sieve_indices:
                    candidate = sieve_begin + sieve_pos
                    if value_0 % candidate == 0:
                        factor = candidate
                        break
                if factor is not None:
                    break
        prime_0 = factor
        prime_1 = value_0 // factor
        if value_1 % prime_0 == 0:
            # TODO: What if value_0 == value_1? We need to look at the following values.
            prime_next = prime_1
        else:
            assert value_1 % prime_1 == 0
            prime_next = prime_0
        prime_seq = [prime_next]
        for value in cipher_values:
            assert prime_next > 1
            prime_next = value // prime_next
            prime_seq.append(prime_next)
        primes = set(prime_seq)
        assert len(primes) == 26
        primes_sorted = sorted(primes)
        letter_map = {prime: chr(ord('A') + i) for i, prime in enumerate(primes_sorted)}
        y = ''.join(letter_map[prime] for prime in prime_seq)
        print('Case #{}: {}'.format(x, y))
