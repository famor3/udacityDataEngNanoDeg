# import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
from pyspark.sql import types as T
from pyspark.sql.types import TimestampType
# from pyspark.sql import functions as F
from datetime import datetime


# Following four lines commented out to run the py file from AWS CLI
# config = configparser.ConfigParser()
# config.read('dl.cfg')

# os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
# os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    # create spark session for processing data files
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    # get filepath to song data file
    # song_data = os.path.join("s3a://udacity-dend/song_data/A/A/A/*.json")
    song_data = "s3a://udacity-dend/song_data/*/*/*/*.json"

    # read song data file
    df_songs = spark.read.json(song_data)
    print(df_songs.columns)

    # extract columns to create songs table
    df_songs.createOrReplaceTempView("songs_table_DF")
    songs_table = spark.sql("""
                            SELECT
                            song_id, title, artist_id, year, duration, artist_name
                            FROM
                            songs_table_DF
                            ORDER BY song_id
                            """)

    # write songs table to parquet files partitioned by year and artist
    songs_table.write.mode('overwrite').partitionBy(
        'year', 'artist_name').parquet(output_data+'songs_table/')

    # extract columns to create artists table
    df_songs.createOrReplaceTempView("artists_table_DF")
    artists_table = spark.sql("""
                            SELECT
                            artist_id, artist_name, artist_location, artist_latitude, artist_longitude
                            FROM
                            artists_table_DF
                            WHERE
                            artist_id IS NOT NULL
                            """)

    # write artists table to parquet files
    artists_table.write.mode('overwrite').parquet(output_data+'artists_table/')


def process_log_data(spark, input_data, output_data):
    # get filepath to log data file
    log_data = "s3a://udacity-dend/log_data/*/*/*.json"

    # read log data file
    df_logs = spark.read.json(log_data)

    # filter by actions for song plays
    df_logs = df_logs.filter(df_logs.page == 'NextSong')

    # extract columns for users table
    df_logs.createOrReplaceTempView('users_table_DF')
    users_table = spark.sql("""
                            SELECT
                            userId, firstName, lastName, gender, level
                            FROM
                            users_table_DF
                            WHERE
                            userId IS NOT NULL
                            """)

    # write users table to parquet files
    users_table.write.mode('overwrite').parquet(output_data+'users_table/')

    # create timestamp column from original timestamp column
    get_timestamp = F.udf(lambda x: datetime.fromtimestamp(
        (x/1000.0)), T.TimestampType())
    df_logs = df_logs.withColumn("timestamp", get_timestamp(df_logs.ts))

    # create datetime column from original timestamp column
    get_datetime = F.udf(
        lambda x: datetime.fromtimestamp((int(x))), T.DateType())
    df_logs = df_logs.withColumn("start_time", get_datetime(df_logs.ts))

    # extract columns to create time table
    time_table = df_logs.withColumn('hour', hour('start_time'))\
        .withColumn('day', dayofmonth('start_time'))\
        .withColumn('week', weekofyear('start_time'))\
        .withColumn('month', month('start_time'))\
        .withColumn('year', year('start_time'))\
        .withColumn('weekday', date_format('start_time', 'u'))\
        .select('ts', 'start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday')\
        .dropDuplicates()

    # write time table to parquet files partitioned by year and month
    time_table.write.mode('overwrite').partitionBy(
        'year', 'month').parquet(output_data+'time_table/')

    # read in song data to use for songplays table
    song_data = "s3a://udacity-dend/song_data/*/*/*/*.json"
    song_df = spark.read.json(song_data)

    # extract columns from joined song and log datasets to create songplays table
    songplays_table = df_logs.join(song_df, df_logs.song == song_df.title, how="inner")\
        .select(F.monotonically_increasing_id().alias('songplay_id'),
                col('start_time').alias('start_time'),
                col('userId').alias('user_id'),
                'level',
                'song_id',
                'artist_id',
                col('sessionId').alias('session_id'),
                'location',
                col('userAgent').alias('user_agent'))

    songplays_table = songplays_table\
        .join(time_table, songplays_table.start_time == time_table.start_time, how='inner') \
        .select('songplay_id', songplays_table.start_time, 'user_id', 'level', 'song_id',
                'artist_id', 'session_id', 'location', 'user_agent', time_table.year, time_table.month)

    # write songplays table to parquet files partitioned by year and month
    df_logs.write.mode('overwrite').partitionBy(
        'year', 'month').parquet(output_data+'songplays_table/')


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://sparkify-lake/"

    process_song_data(spark, input_data, output_data)
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
