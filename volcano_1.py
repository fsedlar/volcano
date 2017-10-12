'''
Indonesian Volcano visualization project
Data from the Smithsonian Global Volcanism Program
http://volcano.si.edu/database/search_eruption_results.cfm#

NOAA also has data
https://catalog.data.gov/dataset/global-significant-volcanic-eruptions-database-4360-bc-to-present

1. Function to write the excel file into a postgres db
2. Set up a NodeJS Project
3. Initialize basic Koa server
4. Add basic postgres integration
5. Add Geojson endpoints
6. Advanced postgis queries
7. Integreate Redis
8. Leaflet, flask, postgis




'''

import psycopg2
import sys

from psycopg2.extensions import AsIs

## Set up a postgres table
#connect to the postres db
conn_string = "host='localhost' dbname='volcano_data' user='frank' password='B00tl3gged'"

conn = psycopg2.connect(conn_string)
print "Opened databse successfully"

#create a table in the postres db
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS volcano_GVP(ID serial PRIMARY KEY, Volcano_Number VARCHAR(40),
	Volcano_Name VARCHAR(40), Eruption_Number VARCHAR(40), VEI VARCHAR(40),
	Start_Year VARCHAR(40), Start_Month VARCHAR(40), Start_Day VARCHAR(40),
	End_Year VARCHAR(40), END_Month VARCHAR(40), END_Day VARCHAR(40),
	Latitude VARCHAR(40), Longitude VARCHAR(40))''')
print "Table created successfully"

#copy data from the GVP file
sqlstr = "COPY volcano_GVP FROM STDIN DELIMITER ',' CSV"
with open('/Users/Phrank/Desktop/volcano/GVP_1.csv') as f:
	cur.copy_expert(sqlstr, f)
conn.commit()

#cur.execute(''' \COPY volcano_GVP (Volcano_Number, Volcano_Name, Eruption_Number, VEI) FROM 'C:/Users/frank.sedlar/Desktop/volcano/GVP.csv' DELIMITER ',' CSV HEADER ''')


print "Records created successfully"
conn.close()
