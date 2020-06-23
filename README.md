# primes
Find prime numbers below n - various algorithms

All hail StackOverflow
https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n

% python3 primes.py
3.8.3
macOS-10.15.5-x86_64-i386-64bit
==== Primes below 100000 ====
rwh_primes: 0.01 seconds
rwh_primes1: 0.02 seconds
rwh_primes2: 0.01 seconds
sieve_wheel_30: 0.02 seconds
sieve_of_eratosthenes: 0.01 seconds
sieve_of_atkin: 0.07 seconds
ambi_sieve_plain: 0.04 seconds
==== Primes below 1000000 ====
rwh_primes: 0.15 seconds
rwh_primes1: 0.17 seconds
rwh_primes2: 0.13 seconds
sieve_wheel_30: 0.16 seconds
sieve_of_eratosthenes: 0.17 seconds
sieve_of_atkin: 0.64 seconds
ambi_sieve_plain: 0.44 seconds
==== Primes below 10000000 ====
rwh_primes: 2.12 seconds
rwh_primes1: 1.81 seconds
rwh_primes2: 1.36 seconds
sieve_wheel_30: 2.12 seconds
sieve_of_eratosthenes: 2.60 seconds
sieve_of_atkin: 6.93 seconds
ambi_sieve_plain: 6.39 seconds
==== Primes below 100000000 ====
rwh_primes: 21.58 seconds
rwh_primes1: 23.08 seconds
rwh_primes2: 16.45 seconds
sieve_wheel_30: 27.21 seconds
sieve_of_eratosthenes: 33.79 seconds
sieve_of_atkin: 80.71 seconds
ambi_sieve_plain: 71.92 seconds
==== Primes below 1000000000 ====
rwh_primes: 239.63 seconds
rwh_primes1: 214.05 seconds
rwh_primes2: 162.01 seconds
sieve_wheel_30: 277.92 seconds
sieve_of_eratosthenes: 5768.43 seconds
sieve_of_atkin: 767.90 seconds
ambi_sieve_plain: 6139.54 seconds

% python3 anagram.py dlkjfslkfjslkjf sdlkfjslfjdsjf
dlkjfslkfjslkjf and sdlkfjslfjdsjf are NOT anagram of each other

% python3 anagram.py dlkjfslkfjslkjf dlkjlsfkfjslkjf
dlkjfslkfjslkjf and dlkjlsfkfjslkjf are anagram of each other


