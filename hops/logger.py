"""
Utility functions to retrieve information about available services and setting up security for the Hops platform.

These utils facilitates development by hiding complexity for programs interacting with Hops services.
"""

from pyspark.sql import SparkSession
try:
    _internal_logger = SparkSession.builder.getOrCreate().sparkContext._jvm.org.apache.log4j.LogManager.getLogger('UserApp')
except:
    pass

def log(s):
    print(s)
    if _internal_logger != None:
        _internal_logger.info(s)