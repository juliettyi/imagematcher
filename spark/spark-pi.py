import findspark
findspark.init()
import pyspark
import random

sc = pyspark.SparkContext(appName="Pi")
num_samples = 1000 * 1000

def inside(p):
  x, y = random.random(), random.random()
  return x*x + y*y < 1

count = sc.parallelize(range(0, num_samples)).filter(inside).count()
pi = 4.0 * count / num_samples
print(pi)
sc.stop()
