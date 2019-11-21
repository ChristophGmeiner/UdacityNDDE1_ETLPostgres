# DROP TABLES

#define variables for sql statements to avoid typos
table1 = "songplays"
table2 = "users"
table3 = "songs"
table4 = "artists"
table5 = "time"

dropsql = "DROP TABLE IF EXISTS "
createsql = "CREATE TABLE "

songplay_table_drop = dropsql + table1
user_table_drop = dropsql + table2
song_table_drop = dropsql + table3
artist_table_drop = dropsql + table4
time_table_drop = dropsql + table5

# CREATE TABLES

songplay_table_create = (createsql + table1 + " (songplay_id serial primary key, \
                         start_time timestamp not null, user_id int not null, level \
                         varchar, song_id varchar, artist_id varchar, \
                         session_id int, location varchar, user_agent \
                         varchar)")

user_table_create = (createsql + table2 + " (user_id int not null primary key, \
                     first_name varchar, last_name varchar, gender varchar, \
                     level varchar)")

song_table_create = (createsql + table3 + " (song_id varchar not null \
                     primary key, title varchar, artist_id varchar not null, \
                     year int, duration float)")

artist_table_create = (createsql + table4 + " (artist_id varchar not null \
                       primary key, name varchar, \
                       location varchar, latitude float, longitude float)")

time_table_create = (createsql + table5 + " (start_time timestamp not null \
                     primary key, hour int, day int, week int, month int, \
                     year int, weekday int)")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays (start_time,\
                          user_id, level, song_id, artist_id, \
                          session_id, location, user_agent) VALUES \
                          (%s, %s, %s, %s, %s, %s, %s, %s)")

user_table_insert = ("INSERT INTO users (user_id, first_name, \
                      last_name, gender, level) VALUES \
                      (%s, %s, %s, %s, %s) \
                      ON CONFLICT(user_id) DO UPDATE SET LEVEL = EXCLUDED.LEVEL")

song_table_insert = ("INSERT INTO songs (song_id, title, artist_id, \
                      year, duration) VALUES \
                      (%s, %s, %s, %s, %s) \
                      ON CONFLICT DO NOTHING")

artist_table_insert = ("INSERT INTO artists (artist_id, name, \
                        location, latitude, longitude) VALUES \
                      (%s, %s, %s, %s, %s) \
                      ON CONFLICT DO NOTHING")

time_table_insert = ("INSERT INTO time (start_time, hour, day,\
                     week, month, year, weekday) VALUES \
                      (%s, %s, %s, %s, %s, %s, %s) \
                      ON CONFLICT DO NOTHING")

# FIND SONGS

song_select = ("SELECT s.song_id, a.artist_id FROM songs s \
                LEFT JOIN artists a \
                ON a.artist_id = s.artist_id where s.title = %s and \
                a.name = %s and s.duration = %s")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, 
                        song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, 
                      song_table_drop, artist_table_drop, time_table_drop]