#
#
#

from math import sqrt
import time
t0 = time.time()

def isPrime(n):
    lim = int(sqrt(n))+1
    for i in xrange(2, lim ) :
        if n % i == 0: return False
    return True


def dumpPrimes(start, end):
    fh = open("primes-%d-%d.txt" % (start, end), 'w+')
    if start < 3:
        fh.write("2\n")
        start = 3
    for i in xrange(start, end + 1, 2):
        if isPrime(i):
            fh.write(str(i))
            fh.write("\n")
    fh.close()


#v=int(1e8)
v=1000
dumpPrimes(1,v)
print "Dumped primes up to %d in %0.3f s" % (v, time.time() -t0 )