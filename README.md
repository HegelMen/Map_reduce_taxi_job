Map-reduce приложение, 
использующее скопированные 
в hdfs открытые данные желтого такси за 2020 год 
из Object storage S3 
и вычисляющее отчет о среднемесячной сумме чаевых на каждый месяц 2020 года.


ИСХОДНЫЙ СЕМПЛ ДАННЫХ (IN csv ~ 2,2 Gb):
VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,trip_distance,
RatecodeID,store_and_fwd_flag,PULocationID,DOLocationID,payment_type,fare_amount,extra,mta_tax,
tip_amount,tolls_amount,improvement_surcharge,total_amount,congestion_surcharge)


ИТОГОВЫЙ ОТЧЕТ (OUT csv):
Payment_type, Month, Tips_average_amount
Количество файлов — 1
Формат — csv
Сортировка — Month по возрастанию, Payment type по возрастанию

Время работы jobы - 1 min 05 sec

in Local, command:

python mapper_taxi.py < IN_2020_Yellow_Taxi_Trip_Data_small_2.csv | reducer_taxi.py
