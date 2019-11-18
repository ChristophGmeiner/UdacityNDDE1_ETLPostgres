import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import json

def process_song_file(cur, filepath):
    # open song file
    df =  pd.read_json(filepath, typ = "series")

    # insert song record
    song_data = list(df.loc[["song_id", "title", "artist_id", "year", 
                             "duration"]].values)
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = list(df.loc[["artist_id", "artist_name", "artist_location", 
                               "artist_latitude", "artist_longtitude"]].values)
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df.page == "NextSong"]

    # convert timestamp column to datetime
    t = pd.to_datetime(df.ts, unit="ms")
    
    # insert time data records
    time_data = zip(t.dt.to_pydatetime(), t.dt.hour, t.dt.day, 
                    t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.dayofweek)
    column_labels = ("start_time", "hour", "day",
                     "week", "month", "year", "weekday")
    time_df = pd.DataFrame(data=list(time_data), columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = user_df = df.loc[:, ["userId", "firstName", "lastName", "gender", "level"]]
    user_df.drop_duplicates(inplace=True)

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        #get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
       # print(results)
    
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = row.loc[["ts", "userId", "level", "song", "artist", 
                               "sessionId", "location", "userAgent"]]
        songplay_data.ts = pd.to_datetime(songplay_data.ts, unit="ms")
        songplay_data.song = songid
        songplay_data.artist = artistid
        cur.execute(songplay_table_insert, songplay_data)
        conn.commit()


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    all_files = [x for x in all_files if x.find("ipynb") == -1]

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()