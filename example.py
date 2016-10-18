#
#
import time

fname='primes-1-100000.txt'

## A good exmaple
t0 = time.time()
with open(fname) as fh:
    # Note: in oder to have integers, use [ int(p) for p in fh ]
    # ... but this not what you always want
    primes=[ p for p in fh]

print "Loaded %d primes in %0.3fs" % (len(primes), time.time() -t0 )


# An Even faster one using a set for fast lookup
import primes
limit=100000

t0 = time.time()
sprimes=set([ i for i in primes.load(fname, limit)] )

print "Loaded %d primes in %0.3fs" % (len(sprimes), time.time() -t0 )
