from math import log, prod
import string
import sys
from primes import rwh_primes2 as primelistfunc

if len(sys.argv) < 3:
    sys.exit(2)

n = len(string.ascii_uppercase)
# https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
upperbound = int(max(6, n*log(n) + n*log(log(26)))+1)

primeList = primelistfunc(upperbound)

primedict = dict(zip(string.ascii_lowercase, primeList[:n]))

def processword(word):
    # ignore non-ascii characters
    return prod([primedict.get(l,1) for l in list(word)])

def is_anagram(word1, word2):
    return processword(word1) == processword(word2)

x = sys.argv[1]
y = sys.argv[2]

print("%s and %s are %sanagram of each other" % (x, y, "" if is_anagram(x,y) else "NOT "))

