My IRX Race

Part 1

My data types are suitable using basic text, integers, and strings. Using B tree indexing and the small database pool I have queries are as simple as they can get minus stating starting_position AS sp and so forth with my other column names. Qualifying times, average lap times, and best lap time would be worth indexing in comparsion to ending position to get a better understanding of pace of each driver to where they ended up. 

Part 2

Added within the plot.py file

Part 3

It is a collection of race times varied by qualifying, best laps, starting and ending position as well as incidents within the race.

The API methods used are GET, POST, and DELETE. My connections made by Driver to Car are one to one relationships, Car to Races is many to many, and Races to Incident one to many. The foreign keys nested in each table respesctively. 

The concept started from the ER Diagram into basic tables with alter table section separate from the tables. It became the SQL file that is the building blocks that allowed me to move into the flask portion adding a PSYCOPG2 database with all my race information using ORM, the main focus of ORM was that it worked when I first used it over the trial and errors faced with SQL. My future improvements would be to expand the creation function to mock up races.