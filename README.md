Running Notes:

Runscript holds all running scripts in an etl way

git is initiated
create script finshed until select songs, also etl py and ipynb

pk violation artist_id, double check mit if...ggf mit dict in py -- solved
now same case with user

<h1>ETL process for creating Sparkify data model in Postgres</h1>

<p> Sparkify is a simulated online music streaming service </p>

<p>This Git repository shows how to script an etl process for loading data from json raw data to a Postgre SQL Database and for creating fact and dimension tables in that manner.</p>

<p>This is done using Python and the mainly the libraries pandas and psycopg2</p>


<h2>Purpose of the database sparkifydb</h2>
<p> The sparkifydb database is postgre SQL based and is about storing information about songs and listening behaviour of the users </p>
<p> The analytical goal of this database to get all kings of insight into the user beahviour </p>

