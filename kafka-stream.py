from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

sc = SparkContext("local[*]","PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc, 60)

kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'test', {'twitter':1})
parsed = kafkaStream.map(lambda v: json.loads(v[1]))
parsed.count().map(lambda x:'Tweets in this batch: %s' % x).pprint()
ssc.start()
ssc.awaitTermination()
