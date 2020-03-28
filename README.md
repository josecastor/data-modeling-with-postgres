# Data Modeling with Postgres



## **Overview**
For this project, Data Modeling with Postgres and an ETL pipeline using Python was applied. The startup Sparkify wants to analyze the data they are collecting about music and user activity in its new music streaming app. They are currently collecting data in the json format and the analytics team is particularly interested in understanding what songs users are listening to.



## **Datasets**

**Song**
Sample Record :
```
{"num_songs": 1, "artist_id": "AR8IEZO1187B99055E", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Marc Shaiman", "song_id": "SOINLJW12A8C13314C", "title": "City Slickers", "duration": 149.86404, "year": 2008}
```

**Log**
Sample Record :
```
{"artist": "Sydney Youngblood", "auth": "Logged In", "firstName": "Jacob", "gender": "M", "itemInSession": 53, "lastName": "Klein", "length": 238.07955, "level": "paid", "location": "Tampa-St. Petersburg-Clearwater, FL", "method": "PUT", "page": "NextSong", "registration": 1.540558e+12, "sessionId": 954, "song": "Ain't No Sunshine", "status": 200, "ts": 1543449657796, "userAgent": ""Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2"", "userId": "73"}
```



## **Schema**

### Dimension Tables

**songs**  - songs of table
```
song_id, title, artist_id, year, duration
```

**artists**  - artists of table
```
artist_id, name, location, latitude, longitude
```

**time**  - time of table
```
start_time, hour, day, week, month, year, weekday
```

**users**  - users of table
```
user_id, first_name, last_name, gender, level
```

### Fact Table 

**songplays** - songplays of table
```
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
```



## Project Files

```create_tables.py``` -> Code for setting up database. Running this file creates **database** and **fact** and **dimension tables**.

```sql_queries.py``` -> Code sql queries for dropping, creating and insertion tables.

```etl.ipynb``` -> Jupyter notebook to test and analyse datasets. 

```etl.py``` -> Read and process files **song_data** and **log_data**

```test.ipynb``` -> Jupyter notebook to connect in postgres db and validate the data. You can use ```etl.ipynb``` for this job.



## How to run

Run the files ```create_tables.py``` and ```etl.py``` as below.
```
!python create_tables.py 
``` 
and
```
!python etl.py 
```
