# spark_streaming

1) How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Modifying maxRatePerPartion from 100 to 500 increased the processedRowsPerSecond by a roughly a magnitude of 8, 753 rows per second to 6100 rows pers second.

2) What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

spark.sql.shuffle.partitions - 12

maxRatePerPartition - 500

Through the progress reporter, I examined values such as processed rows per second. A couple of points I would like to add though,
1) I don't think performance tuning is as simple as grabbing screenshots of the progress reporter and comparing a couple of times as I imagine there are variables in play that would be hard to control on a single execution.

2) It is also not as simple as just cranking about a few of the pararmeters since we are moving to a cloud based, pay for what you use world. It would be unwise to pay for capacity that was not being utilized.

