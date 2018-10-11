from pyspark import SparkContext
import sys
import time

logFile = sys.argv[1]

sc = SparkContext("local[*]", "first app")

logData = sc.textFile(logFile).cache()
#numAs = logData.filter(lambda s: 'a' in s).count()
#numBs = logData.filter(lambda s: 'b' in s).count()
#print "Lines with a: %i, lines with b: %i" % (numAs, numBs)
before = time.time()

print logData.count()

after = time.time()

print "Time :", after-before 
