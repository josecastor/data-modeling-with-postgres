import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    drop_table_queries = ["songplays", "users", "songs", "artists", "time"]
    for query in drop_table_queries:
        cur.execute('DROP TABLE IF EXISTS {}'.format(query))
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    "CREATE TABLE songplays"
    sqlCreateSongPlays = "CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, \
                                                                start_time varchar NOT NULL, \
                                                                user_id varchar NOT NULL, \
                                                                level varchar, \
                                                                song_id varchar, \
                                                                artist_id varchar, \
                                                                session_id varchar, \
                                                                location varchar, \
                                                                user_agent varchar);"
    "CREATE TABLE users"
    sqlCreateUsers = "CREATE TABLE IF NOT EXISTS users (user_id int NOT NULL, \
                                                        first_name varchar, last_name varchar, gender varchar, level varchar);"
    "CREATE TABLE songs"
    sqlCreateSongs = "CREATE TABLE IF NOT EXISTS songs (song_id varchar NOT NULL, \
                                                            title varchar, artist_id varchar, year int, duration numeric);"
    "CREATE TABLE artists"
    sqlCreateArtists = "CREATE TABLE IF NOT EXISTS artists (artist_id varchar NOT NULL, \
                                                            name varchar, location varchar, latitude numeric, longitude numeric);"
    "CREATE TABLE time"
    sqlCreateTime = "CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour int, day int, week int, month int, year int, weekday int);"
    
    create_table_queries = [sqlCreateSongPlays, sqlCreateUsers, sqlCreateSongs, sqlCreateArtists, sqlCreateTime]
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()