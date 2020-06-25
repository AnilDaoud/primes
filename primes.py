from math import sqrt, ceil

# bruteforce function, ultra slow
def naiveprimes(n):
    i = 2
    primes = []
    while i < n:
        for x in range(2, int(sqrt(i) + 1)):
            if i%x==0:
                break
        else:
            primes.append(i)
        i += 1
    return primes

# https://stackoverflow.com/a/2068412
# https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/3796442#3796442
import itertools
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat2(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))

def erat2a( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            # old code here:
            # x = p + q
            # while x in D or not (x&1):
            #     x += p
            # changed into:
            x = q + 2*p
            while x in D:
                x += 2*p
            D[x] = p

def get_primes_erat2a(n):
  return list(itertools.takewhile(lambda p: p<n, erat2a()))

def erat3( ):
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in itertools.compress(
            itertools.islice(itertools.count(7), 0, None, 2),
            itertools.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p

def get_primes_erat3(n):
  return list(itertools.takewhile(lambda p: p<n, erat3()))

# https://stackoverflow.com/a/19391111
def psieve():
    yield from (2, 3, 5, 7)
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p*p
    for i in itertools.count(9, 2):
        if i in D:      # composite
            step = D.pop(i)
        elif i < psq:   # prime
            yield i
            continue
        else:           # composite, = p*p
            assert i == psq
            step = 2*p
            p = next(ps)
            psq = p*p
        i += step
        while i in D:
            i += step
        D[i] = step

def get_primes_psieve(n):
  return list(itertools.takewhile(lambda p: p<n, psieve()))

def rwh_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def rwh_primes1(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """Input n>=6, Returns a list of primes, 2 <= p < n"""
    assert n >= 6
    correction = n % 6 > 1
    n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
    sieve = [True] * (n // 3)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = [False] * (
                (n // 6 - (k * k) // 6 - 1) // k + 1
            )
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = [False] * (
                (n // 6 - (k * k + 4 * k - 2 * k * (i & 1)) // 6 - 1) // k + 1
            )
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


def sieve_wheel_30(N):
    # http://zerovolt.com/?p=88
    """ Returns a list of primes <= N using wheel criterion 2*3*5 = 30

Copyright 2009 by zerovolt.com
This code is free for non-commercial purposes, in which case you can just leave this comment as a credit for my work.
If you need this code for commercial purposes, please contact me by sending an email to: info [at] zerovolt [dot] com."""
    __smallp = (
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
        307,
        311,
        313,
        317,
        331,
        337,
        347,
        349,
        353,
        359,
        367,
        373,
        379,
        383,
        389,
        397,
        401,
        409,
        419,
        421,
        431,
        433,
        439,
        443,
        449,
        457,
        461,
        463,
        467,
        479,
        487,
        491,
        499,
        503,
        509,
        521,
        523,
        541,
        547,
        557,
        563,
        569,
        571,
        577,
        587,
        593,
        599,
        601,
        607,
        613,
        617,
        619,
        631,
        641,
        643,
        647,
        653,
        659,
        661,
        673,
        677,
        683,
        691,
        701,
        709,
        719,
        727,
        733,
        739,
        743,
        751,
        757,
        761,
        769,
        773,
        787,
        797,
        809,
        811,
        821,
        823,
        827,
        829,
        839,
        853,
        857,
        859,
        863,
        877,
        881,
        883,
        887,
        907,
        911,
        919,
        929,
        937,
        941,
        947,
        953,
        967,
        971,
        977,
        983,
        991,
        997,
    )
    # wheel = (2, 3, 5)
    const = 30
    if N < 2:
        return []
    if N <= const:
        pos = 0
        while __smallp[pos] <= N:
            pos += 1
        return list(__smallp[:pos])
    # make the offsets list
    offsets = (7, 11, 13, 17, 19, 23, 29, 1)
    # prepare the list
    p = [2, 3, 5]
    dim = 2 + N // const
    tk1 = [True] * dim
    tk7 = [True] * dim
    tk11 = [True] * dim
    tk13 = [True] * dim
    tk17 = [True] * dim
    tk19 = [True] * dim
    tk23 = [True] * dim
    tk29 = [True] * dim
    tk1[0] = False
    # help dictionary d
    # d[a , b] = c  ==> if I want to find the smallest useful multiple of (30*pos)+a
    # on tkc, then I need the index given by the product of [(30*pos)+a][(30*pos)+b]
    # in general. If b < a, I need [(30*pos)+a][(30*(pos+1))+b]
    d = {}
    for x in offsets:
        for y in offsets:
            res = (x * y) % const
            if res in offsets:
                d[(x, res)] = y
    # another help dictionary: gives tkx calling tmptk[x]
    tmptk = {1: tk1, 7: tk7, 11: tk11, 13: tk13, 17: tk17, 19: tk19, 23: tk23, 29: tk29}
    pos, prime, lastadded, stop = 0, 0, 0, int(ceil(sqrt(N)))

    # inner functions definition
    def del_mult(tk, start, step):
        for k in range(start, len(tk), step):
            tk[k] = False

    # end of inner functions definition
    cpos = const * pos
    while prime < stop:
        # 30k + 7
        if tk7[pos]:
            prime = cpos + 7
            p.append(prime)
            lastadded = 7
            for off in offsets:
                tmp = d[(7, off)]
                start = (
                    (pos + prime)
                    if off == 7
                    else (prime * (const * (pos + 1 if tmp < 7 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 11
        if tk11[pos]:
            prime = cpos + 11
            p.append(prime)
            lastadded = 11
            for off in offsets:
                tmp = d[(11, off)]
                start = (
                    (pos + prime)
                    if off == 11
                    else (prime * (const * (pos + 1 if tmp < 11 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 13
        if tk13[pos]:
            prime = cpos + 13
            p.append(prime)
            lastadded = 13
            for off in offsets:
                tmp = d[(13, off)]
                start = (
                    (pos + prime)
                    if off == 13
                    else (prime * (const * (pos + 1 if tmp < 13 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 17
        if tk17[pos]:
            prime = cpos + 17
            p.append(prime)
            lastadded = 17
            for off in offsets:
                tmp = d[(17, off)]
                start = (
                    (pos + prime)
                    if off == 17
                    else (prime * (const * (pos + 1 if tmp < 17 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 19
        if tk19[pos]:
            prime = cpos + 19
            p.append(prime)
            lastadded = 19
            for off in offsets:
                tmp = d[(19, off)]
                start = (
                    (pos + prime)
                    if off == 19
                    else (prime * (const * (pos + 1 if tmp < 19 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 23
        if tk23[pos]:
            prime = cpos + 23
            p.append(prime)
            lastadded = 23
            for off in offsets:
                tmp = d[(23, off)]
                start = (
                    (pos + prime)
                    if off == 23
                    else (prime * (const * (pos + 1 if tmp < 23 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # 30k + 29
        if tk29[pos]:
            prime = cpos + 29
            p.append(prime)
            lastadded = 29
            for off in offsets:
                tmp = d[(29, off)]
                start = (
                    (pos + prime)
                    if off == 29
                    else (prime * (const * (pos + 1 if tmp < 29 else 0) + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
        # now we go back to top tk1, so we need to increase pos by 1
        pos += 1
        cpos = const * pos
        # 30k + 1
        if tk1[pos]:
            prime = cpos + 1
            p.append(prime)
            lastadded = 1
            for off in offsets:
                tmp = d[(1, off)]
                start = (
                    (pos + prime)
                    if off == 1
                    else (prime * (const * pos + tmp)) // const
                )
                del_mult(tmptk[off], start, prime)
    # time to add remaining primes
    # if lastadded == 1, remove last element and start adding them from tk1
    # this way we don't need an "if" within the last while
    if lastadded == 1:
        p.pop()
    # now complete for every other possible prime
    while pos < len(tk1):
        cpos = const * pos
        if tk1[pos]:
            p.append(cpos + 1)
        if tk7[pos]:
            p.append(cpos + 7)
        if tk11[pos]:
            p.append(cpos + 11)
        if tk13[pos]:
            p.append(cpos + 13)
        if tk17[pos]:
            p.append(cpos + 17)
        if tk19[pos]:
            p.append(cpos + 19)
        if tk23[pos]:
            p.append(cpos + 23)
        if tk29[pos]:
            p.append(cpos + 29)
        pos += 1
    # remove exceeding if present
    pos = len(p) - 1
    while p[pos] > N:
        pos -= 1
    if pos < len(p) - 1:
        del p[pos + 1 :]
    # return p list
    return p


def sieve_of_eratosthenes(n):
    """sieveOfEratosthenes(n): return the list of the primes < n."""
    # Code from: <dickinsm@gmail.com>, Nov 30 2006
    # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si * si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]


def sieve_of_atkin(end):
    """return a list of all the prime numbers <end using the Sieve of Atkin."""
    # Code by Steve Krenzel, <Sgk284@gmail.com>, improved
    # Code: https://web.archive.org/web/20080324064651/http://krenzel.info/?p=83
    # Info: http://en.wikipedia.org/wiki/Sieve_of_Atkin
    assert end > 0
    lng = (end - 1) // 2
    sieve = [False] * (lng + 1)

    x_max, x2, xd = int(sqrt((end - 1) / 4.0)), 0, 4
    for xd in range(4, 8 * x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end - x2))
        n, n_diff = x2 + y_max * y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n % 12
            if m == 1 or m == 5:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, x2, xd = int(sqrt((end - 1) / 3.0)), 0, 3
    for xd in range(3, 6 * x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end - x2))
        n, n_diff = x2 + y_max * y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if n % 12 == 7:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, y_min, x2, xd = int((2 + sqrt(4 - 8 * (1 - end))) / 4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end:
            y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x * x + x) << 1) - 1, (((x - 1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if n % 12 == 11:
                m = n >> 1
                sieve[m] = not sieve[m]
            n += d

    primes = [2, 3]
    if end <= 3:
        return primes[: max(0, end - 2)]

    for n in range(5 >> 1, (int(sqrt(end)) + 1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            aux = (n << 1) + 1
            aux *= aux
            for k in range(aux, end, 2 * aux):
                sieve[k >> 1] = False

    s = int(sqrt(end)) + 1
    if s % 2 == 0:
        s += 1
    primes.extend([i for i in range(s, end, 2) if sieve[i >> 1]])

    return primes


def ambi_sieve_plain(n):
    s = list(range(3, n, 2))
    for m in range(3, int(n ** 0.5) + 1, 2):
        if s[(m - 3) // 2]:
            for t in range((m * m - 3) // 2, (n >> 1) - 1, m):
                s[t] = 0
    return [2] + [t for t in s if t > 0]


import platform, timeit

if __name__ == '__main__':
    print(platform.python_version())
    print(platform.platform())
    functionList = [naiveprimes, get_primes_erat2, get_primes_erat2a, get_primes_erat3, get_primes_psieve, rwh_primes, rwh_primes1, rwh_primes2, sieve_wheel_30, sieve_of_eratosthenes, sieve_of_atkin, ambi_sieve_plain]
    primes = []
    it = 4
    n = 10**6
    print("==== Primes below " + str(n) + " ====")
    for f in functionList:
        if len(primes) == 0:
            func = f.__name__
            primes = f(n)
        else:
            prevPrimes = primes
            prevFunc = func
            func = f.__name__
            primes = f(n)
            if prevPrimes != primes:
                print("Error: %s and %s return different prime list" % (func, prevFunc))
                break
        print("%s: %.2f seconds" % (f.__name__, timeit.timeit(f.__name__ + '('+str(n)+')', number=it, globals=globals())))


