from __future__ import print_function

import sys

from pyspark.sql import SparkSession
#-----------------------------------


if __name__ == "__main__":

    # create an instance of a SparkSession as spark
    spark = SparkSession\
        .builder\
        .appName("wordcount")\
        .getOrCreate()

    inputPath = "/data/foxdata.txt"

    # create SparkContext as sc
    sc = spark.sparkContext

    # create RDD from a text file
    # textfileRDD = sc.textFile(inputPath)
    print(1)
    
    spark.stop()
