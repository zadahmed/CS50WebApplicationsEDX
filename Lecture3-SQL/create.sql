CREATE TABLE flights (
	id SERIAL PRIMARY KEY, #serial is used to have automated id number
	origin VARCHAR NOT NULL, #varchar for text aka string
	destination VARCHAR NOT NULL,
	duration  INTEGER NOT NULL
);

# to insert data into table
INSERT INTO flights (origin , destination , duration ) VALUES ('New York' , 'London' , 415);

SELECT * FROM flights; #to display table

SELECT origin , destination FROM flights;
#returns origin and destination from table.

SELECT * FROM flights WHERE id = 3;
# to display the row with id = 3.

SELECT AVG(duration) FROM flights;
#gets the average duration

SELECT COUNT(*) FROM flights;
#NUMBER OF ROWS IN FLIGHTS

SELECT MIN(duration) FROM flights;

SELECT * FROM flights WHERE origin LIKE '%a%';
#returned back with a in the origin 

#UPDATE THE DATABASE 
UPDATE flights 
	SET duration = 430
	WHERE origin = 'New York'
	AND destination = 'London';

#delete
DELETE from flights
	WHERE destination = 'Tokyo';

SELECT origin , COUNT(*) FROM flights GROUP BY origin;
#group by

SELECT origin , COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) >1;
#HAVING IS SIMILAR TO WHERE BUT FOR COUNT *


#Foreign key to create relationships between tables
CREATE TABLE passengers(
	id SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL,
	flight_id INTEGER REFERENCES flights
);

#Join tables that are related
SELECT origin , destination , name FROM flights JOIN passengers ON passengers.flight_id = flights.id;


#sql injection
'1' OR '1' = '1' #Returns true of password
#irrespective of the password

#race conditions
UPDATE bank
SET balance = balance - 100
WHERE Id = 1;