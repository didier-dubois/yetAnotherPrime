#
#
import time
t0 = time.time()

fname='primes-1-100000.txt'

with open(fname) as fh:
    primes=[ p for p in fh]

print "Loaded %d primes in %0.3fs" % (len(primes), time.time() -t0 )
