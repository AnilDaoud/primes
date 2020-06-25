# primes
Find prime numbers below n - various algorithms from StackOverflow and the Python Cookbook

```console
% python3 anagram.py dlkjfslkfjslkjf sdlkfjslfjdsjf
dlkjfslkfjslkjf and sdlkfjslfjdsjf are NOT anagram of each other

% python3 anagram.py EÈÉÊË èéeêë
EÈÉÊË and èéeêë are anagram of each other

% python3 primes.py
3.8.3
macOS-10.15.5-x86_64-i386-64bit
==== Primes below 100000 ====
naiveprimes: 0.77 seconds
popprimes: 0.10 seconds
get_primes_erat2: 0.12 seconds
get_primes_erat2a: 0.08 seconds
get_primes_erat3: 0.07 seconds
rwh_primes: 0.01 seconds
rwh_primes1: 0.01 seconds
rwh_primes2: 0.01 seconds
sieve_wheel_30: 0.02 seconds
sieve_of_eratosthenes: 0.01 seconds
sieve_of_atkin: 0.06 seconds
ambi_sieve_plain: 0.03 seconds
==== Primes below 1000000 ====
naiveprimes: 19.15 seconds
popprimes: 1.27 seconds
get_primes_erat2: 1.40 seconds
get_primes_erat2a: 0.97 seconds
get_primes_erat3: 0.88 seconds
rwh_primes: 0.16 seconds
rwh_primes1: 0.17 seconds
rwh_primes2: 0.14 seconds
sieve_wheel_30: 0.18 seconds
sieve_of_eratosthenes: 0.19 seconds
sieve_of_atkin: 0.69 seconds
ambi_sieve_plain: 0.49 seconds
==== Primes below 10000000 ====
Skipping naiveprimes, too slow for large numbers
Skipping popprimes, too slow for large numbers
get_primes_erat2: 15.63 seconds
get_primes_erat2a: 10.56 seconds
get_primes_erat3: 8.96 seconds
rwh_primes: 1.86 seconds
rwh_primes1: 1.76 seconds
rwh_primes2: 1.32 seconds
sieve_wheel_30: 2.27 seconds
sieve_of_eratosthenes: 2.40 seconds
sieve_of_atkin: 6.36 seconds
ambi_sieve_plain: 6.29 seconds
==== Primes below 100000000 ====
Skipping naiveprimes, too slow for large numbers
Skipping popprimes, too slow for large numbers
Skipping get_primes_erat2, too slow for large numbers
Skipping get_primes_erat2a, too slow for large numbers
Skipping get_primes_erat3, too slow for large numbers
rwh_primes: 21.58 seconds
rwh_primes1: 23.08 seconds
rwh_primes2: 16.45 seconds
sieve_wheel_30: 27.21 seconds
sieve_of_eratosthenes: 33.79 seconds
sieve_of_atkin: 80.71 seconds
ambi_sieve_plain: 71.92 seconds
==== Primes below 1000000000 ====
Skipping naiveprimes, too slow for large numbers
Skipping popprimes, too slow for large numbers
Skipping get_primes_erat2, too slow for large numbers
Skipping get_primes_erat2a, too slow for large numbers
Skipping get_primes_erat3, too slow for large numbers
rwh_primes: 239.63 seconds
rwh_primes1: 214.05 seconds
rwh_primes2: 162.01 seconds
sieve_wheel_30: 277.92 seconds
sieve_of_eratosthenes: 5768.43 seconds
sieve_of_atkin: 767.90 seconds
ambi_sieve_plain: 6139.54 seconds

```

