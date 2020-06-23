from math import log, prod
import string
import sys

if len(sys.argv) < 3:
    sys.exit(2)

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

n = len(string.ascii_uppercase)
# https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
upperbound = int(max(6, n*log(n) + n*log(log(26)))+1)
primeList = rwh_primes2(upperbound)

primedict = dict(zip(string.ascii_lowercase, primeList[:26]))

def processword(word):
    return prod([primedict.get(l,1) for l in list(word)])

def is_anagram(word1, word2):
    return processword(word1) == processword(word2)

if is_anagram(sys.argv[1],sys.argv[2]):
    print("%s and %s are anagram of each other" % (sys.argv[1], sys.argv[2]))
else:
    print("%s and %s are NOT anagram of each other" % (sys.argv[1], sys.argv[2]))

