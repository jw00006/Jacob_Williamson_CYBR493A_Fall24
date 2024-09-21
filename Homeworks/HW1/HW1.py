# Jacob Williamson
# CYBR493A
# Fall24
# HW#1
print('Jacob Williamson \nCYBR493A \nFall24 \nHomework #1')

import DBConnector
import os
from datetime import datetime

def ping_something (ip_address):
    """
    Helper function to ping a provided IP address.
    """
    # added '-c 4' tag because my mac will ping IPs indefinitely if not told to count
    ping_command = 'ping -c 4 ' + ip_address
    # actually pinging the addresses
    ping_result = os.system(ping_command)
    return ping_result

def main():
    """
    Main function to return whether an IP address is responding.
    """
    #
    my_db = DBConnector.MyDB()
    # list of IPs to ping
    ips = ["127.0.0.1", "2.2.2.2", "7.7.7.7", "8.8.8.8", "192.168.10.10", "1.1.1.1", "9.9.9.9", "4.2.2.2", "192.168.0.1", "1.0.0.1"]
    # counters for total num of good and bad pings
    good_count = 0
    bad_count = 0
    status = False
    # for loop for pinging list of IPs
    for ip in ips:
        current_time = (datetime.now())
        ping_result = ping_something(ip)
        # if ping goes through
        if(ping_result == 0):
            status = True
            print(f"\n{ip} is responding.\n{current_time} \nStatus = {status}\n")
            good_count += 1
            # sql insert command
            sqlCommand = 'INSERT INTO Williamson_Jacob_HW1_Ips (ip, timestamp, status) VALUES(%s, %s, %s)'
            # holding values to be used in the db.query parameter
            values = (ip, current_time, status)
            # actually runs the insert query on the db
            my_db.query(sqlCommand, values)

        # if ping does not go through
        else:
            status = False
            print(f"\n{ip} is not responding.\n{current_time} \nStatus = {status}\n")
            bad_count += 1
            # sql insert command
            sqlCommand = 'INSERT INTO Williamson_Jacob_HW1_Ips (ip, timestamp, status) VALUES(%s, %s, %s)'
            # holding values to be used in the db.query parameter
            values = (ip, current_time, status)
            # actually runs the insert query on the db
            my_db.query(sqlCommand, values)

    # returning counters of good and bad IPs
    print(f"Good pings: {good_count}")
    print(f"Bad pings: {bad_count}")


if __name__ == "__main__":
    main()
