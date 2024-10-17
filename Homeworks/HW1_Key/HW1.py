# Jacob Williamson
# CYBR493A
# Fall24
# HW#1 Key
print('Jacob Williamson \nCYBR493A \nFall24 \nHW#1 Key')

import DBConnector
import os

def CreateTable(my_db):
    """
    This method creates a table
    :return: N/A
    """
    # SQL command to create a new table
    sqlCommand = 'CREATE TABLE IF NOT EXISTS Williamson_Jacob_HW1_IPs_Key (IP  VARCHAR, TimeStamp  VARCHAR, Status VARCHAR);'
    # Execute the SQL command.
    my_db.query(sqlCommand, '')

def ping_target(ip_address):
    """
    Pings IPs
    :param: ip_address: The ip address of ping
    :return: ping_result: the status of the ping
    """
    ping_command = "ping -c 4 " + ip_address
    ping_result = os.system(ping_command)
    return ping_result

def main():
    ips = ["127.0.0.1", "127.1.1.1", "127.2.2.2", "1.1.1.1"]
    for ip in ips:
        print("The status is", ping_target(ip))
    # Create a new instance of the DB
    #my_db = DBConnector.MyDB()
    #CreateTable(my_db)

if __name__ == "__main__":
    main()
