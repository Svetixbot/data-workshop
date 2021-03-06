import sys
from pyspark import SparkContext


logFile = "lorem.txt"  # Should be some file on your system
sc = SparkContext(sys.argv[1], "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print "Lines with a: %i, lines with b: %i" % (numAs, numBs)
