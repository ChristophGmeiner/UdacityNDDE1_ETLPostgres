<h1>ETL process for Creating Sparkify Data Model in Postgres</h1>
<p>This is my first project for the Udacity Nanodegree of Data Engineering. It is about an etl process (postgres based) for Sparkify.</p>
<p> Sparkify is a simulated (not-real) online music streaming service.</p>

<p>This Git repository shows how to script an etl process for loading data from json raw data to a Postgre SQL Database and for creating fact and dimension tables in that manner.</p>

<p>This is done using Python, mainly with pandas and psycopg2</p>


<h2>Purpose of the Database sparkifydb</h2>
<p> The sparkifydb database is postgre SQL based and is about storing information about songs and listening behaviour of the users </p>
<p> The analytical goal of this database to get all kings of insight into the user beahviour </p>

<h2>Description of the ETL Pipeline</h2>

<h3>Description of the raw Datasets</h3>
<p>Raw data comes in json formats and is stored in several subdirectories und the /data directory</p>

<h4>log data</h4>
<p>This directory contains jsons which show basically user activity per day on Sparkify.</p>

<h4>song data</h4>
<p>This directory contains jsons which show basically available songs and artists on Sparkify.</p>

<h3>Scripts and Files</h3>
<p>Basically the shell script RunScripts.sh contains the relevant etl files. So basically running this script (./RunScripts.sh) resets the sparkify database to an empty state and then creates all the table structures (create_tables.py). After that all the necessary data is derived from the json files under the /data directory and loaded into the tables created with the etl.py. The functions from sql_queries.py are used in both of these scripts for dropping, creating and inserting in postgre tables.</p>

<h4>Other Files</h4>

<h5>test.ipynb</h5>
<p>A notebook for testing the contents of the sql tables.</p>

<h3>Final Data Structure</h3>
<p>Please find descriptions of the final tables below</p>

<h4>songplays</h4>
<p>This is supposed to be the fact table and shows every single songplay activity, i.e. a user listened to a speicifc song at a specific time and so on. It has an artifical primary key via identity column and all other sorts of attributes concerning the songplay activity.</p>

<h4>users</h4>
<p>This table contains master data on users</p>

<h4>songs</h4>
<p>This table contains master data on songs</p>

<h4>artists</h4>
<p>This table contains master data on artists</p>

<h4>time</h4>
<p>This table contains master data on the timestamp, i.e. what hour, day, month, etc.</p>

<h4>analysis</h4>
<p>This notebook shows some basic analysis.</p>

<h2>Potential next steps and imporovements</h2>
* <p>Use Bulk method for loading data. This would be necessary if you have to load much bigger amounts of the data to speed up the performance</p>
* <p>Create a way to make only increment loads</p>
* Create alerts or similar to monitor the etl pipeline

