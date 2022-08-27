\#!/usr/bin/env bash

export MR_OUTPUT=/user/root/output-data/2020

hadoop fs -rm -r $MR_OUTPUT


hadoop jar "$HADOOP_MAPRED_HOME"/hadoop-streaming.jar \
-Dmapred.job.name='yelow_taxi_2020_job' \
-Dmapred.reduce.tasks=1 \
-Dmapreduce.map.memory.mb=6144 \
-file /root/taxi/mapper_taxi.py -mapper mapper_taxi.py \
-file /root/taxi/reducer_taxi.py -reducer reducer_taxi.py \
-input /user/root/input-data/2020 \
-output $MR_OUTPUT

hadoop fs -get -f /user/root/output-data/2020/part-00000 ./p-emeljanov_mapred_report_Taxi2020.csv