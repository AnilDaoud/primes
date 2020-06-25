import sys
import unicodedata
from math import log, prod
from string import ascii_lowercase
from primes import rwh_primes2 as primelistfunc

if len(sys.argv) < 3:
    sys.exit(2)

# Unicode combining diacritical marks run from 768 to 879, inclusive
combining_chars = ''.join(map(chr, range(768, 880)))

# https://stackoverflow.com/a/57170442
def get_unicode_variations(letter):
    if len(letter) != 1:
        raise ValueError("letter must be a single character to check for variations")
    variations = []
    # We could just loop over map(chr, range(768, 880)) without caching
    # in combining_chars, but that increases runtime ~20%
    for combiner in combining_chars:
        normalized = unicodedata.normalize('NFKC', letter + combiner)
        if len(normalized) == 1:
            variations.append(normalized)
    return ''.join(variations)

charlist = ''
for l in ascii_lowercase:
    charlist += l+get_unicode_variations(l)

n = len(charlist)
# https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
upperbound = int(max(6, n*log(n) + n*log(log(n)))+1)

primeList = primelistfunc(upperbound)

primedict = dict(zip(charlist, primeList[:n]))

def processword(word):
    # ignore non-ascii characters
    return prod([primedict.get(l,1) for l in word.lower()])

def is_anagram(word1, word2):
    return processword(word1) == processword(word2)

x = sys.argv[1]
y = sys.argv[2]

print("%s and %s are %sanagram of each other" % (x, y, "" if is_anagram(x,y) else "NOT "))

