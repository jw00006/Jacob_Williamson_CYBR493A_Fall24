# Jacob Williamson
# CYBR493A
# Fall24
# Activity #2 Pro
print('Jacob Williamson \nCYBR493A \nFall24 \nActivity #2 Pro')

import DBConnector

def CreateTable(my_db):
    """
    This method creates a table
    :return: N/A
    """
    # SQL command to create a new table
    sqlCommand = 'CREATE TABLE IF NOT EXISTS Williamson_Jacob_Table (MID  VARCHAR, MNAME  VARCHAR);'
    # Execute the SQL command.
    my_db.query(sqlCommand, '')

def DropTable(my_db):
    """
    This method drops the table
    :return: N/A
    """
    # SQL command to create a new table
    sqlCommand = 'DROP TABLE Williamson_Jacob_Table;'
    # Execute the SQL command.
    my_db.query(sqlCommand, '')

def main():
    # Create a new instance of the DB
    my_db = DBConnector.MyDB()
    CreateTable(my_db)
    sqlStatement = 'INSERT INTO Williamson_Jacob_Table VALUES(%s, %s);'
    my_db.query(sqlStatement, ("1", "One"))
    my_db.query(sqlStatement, ("2", "One"))
    my_db.query(sqlStatement, ("3", "One"))
    my_db.query(sqlStatement, ("4", "One"))
    my_db.query(sqlStatement, ("5", "One"))
    DropTable(my_db)


if __name__ == "__main__":
    main()
