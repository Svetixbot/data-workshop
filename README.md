## Installation instructions

1. [Download Spark - Prebuild for Hadoop 2.6](http://spark.apache.org/downloads.html)

2. Try to run 
``` 
$YOUR_SPARK_PATH/bin/spark-shell
```

3. Once it is loaded you will see scala console:
```
scala>
```
Type ```'sc'``` and press enter, you should see:
```
scala> sc
res0: org.apache.spark.SparkContext = org.apache.spark.SparkContext@1f60824e
```

## Start spark locally

1. Start spark locally.

     1.1. Start the master
         ```$YOUR_SPARK_PATH/sbin/start-master.sh```

     1.2. After couple of minutes the http://localhost:8080 will be available. It is a spark ui.

     1.3. Start workers(as many as you like, 2 or 3):
```
$YOUR_SPARK_PATH/bin/spark-class org.apache.spark.deploy.worker.Worker $SPARK_MASTER_URL &
```

```where $SPARK_MASTER_URL is in the [web ui](http://localhost:8080)```

2. Submit a test job

```
$YOUR_SPARK_PATH/bin/spark-submit --master $SPARK_MASTER_URL job.py $SPARK_MASTER_URL
```

## Exersices

### #1 Learn about RDD
[Let's go through the official tutorial](http://spark.apache.org/docs/latest/quick-start.html)

### #2 More challenges

[Here](https://github.com/maxwedwards/spark-retreat-python)

### #3 Set up a cluster on EC2
[Here](http://spark.apache.org/docs/latest/ec2-scripts.html)

## References
[Designing Data-Intensive Applications](http://amzn.to/1TUya17)

[slides](https://slides.com/svetlanafilimonova/data-intensive-applications)