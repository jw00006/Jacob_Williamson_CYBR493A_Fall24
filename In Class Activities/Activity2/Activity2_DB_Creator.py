# Jacob Williamson
# CYBR493A
# Fall24
# Activity #2
print('Jacob Williamson \nCYBR493A \nFall24 \nActivity #2')

import DBConnector

# Create a new instance of the DB
my_db = DBConnector.MyDB()

# SQL command to create a new table
sqlCommand = 'CREATE TABLE IF NOT EXISTS Williamson_Jacob_Table (MID  VARCHAR, MNAME  VARCHAR);'

# Execute the SQL command.
my_db.query(sqlCommand, '')
