# Data Warehouse
---
  
## **Overview**
---
This project has us build an ETL pipeline using AWS. Data extraction from S3, staging into Redshift where data is transformed into dimensional tables for use by Sprkify's analytic team. Sparkify has grown their user and song database and would like to move their processes into the cloud.

## **Project Datasets**
---
The datasets reside in AWS S3. Links for the datasets are as follows:

Song Data: s3://udacity-dend/song_data
Log Data:  s3://udacity-dend/log_data
JSON Path: s3://udacity-dend/log_json_path.json

## **Song Dataset**
---
The song dataset is a subset of [Million Song Dataset](http://millionsongdataset.com).
  
Sample record:  
```json
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

## **Log Dataset**
---
Logs dataset has been generated by [Event Simulator](https://github.com/Interana/eventsim).

Sample log file:
![Sample log file](log-data.png)

## Schema  
---  
### Fact Table  
**songplays** - record of data in log data associated with song plays for example, records with page `NextSong`

```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
```

### Dimension Tables
**users** - table of app users

```
user_id, first_name, last_name, gender, level
```

**songs** - table of song titles in music db

```
song_id, title, artist_id, year, duration
```

**artists** - table of artists in music db

```
artist_id, name, location, latitude, longitude
```

**time** - table containing timestamps of songs in **songplays** by unit of time

```
start_time, hour, day, week, month, year, weekday
```

## Project Files
---
```create_tables.py``` -> used for creating **sparkify** fact and dimension tables in star schema in Redshift  
```dwh.cfg``` -> configuration file for AWS
```etl.py``` -> load data from S3 into staging tables on Redshift then process data into Analytic tables on Redshift
```sql_queries.py``` -> used to define SQL statements which will be imported into two other py files


## Environment
---
Python 3.6 or above

AWS Redshift

AWS S3

psycopg2 2.7 or above - PostgresSQL database adapter for Python

JupyterLab 1.0 or above - for db analysis

## To run
---
Run the ```create_tables.py``` and the ```etl.py``` files independently as follows:
```
python create_tables.py
python etl.py
```

#### References:
[AWS Documentation](https://docs.aws.amazon.com/index.html)

[Psycopg](http://initd.org/psycopg/docs/)