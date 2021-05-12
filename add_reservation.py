<<<<<<< HEAD
#!/usr/bin/python

import psycopg2
import datetime
from config import config



def insert_reservation(house, id, check_in_date, check_in_time, check_out_date, guest_name,
                       guest_cell, guest_telegram, num_guest, comment, confirm):
    """ insert a new reservation into the reservation table """
    sql = """INSERT INTO %s VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s', %s) RETURNING reservation_id;"""
    conn = None
    reservation_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        print(sql % (house, id, check_in_date, check_in_time, check_out_date, guest_name,
                       guest_cell, guest_telegram, num_guest, comment, confirm))
        cur.execute(sql, (house, id, check_in_date, check_in_time, check_out_date, guest_name,
                       guest_cell, guest_telegram, num_guest, comment, confirm))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return reservation_id

insert_reservation('emerald', 121, '03/03/2014', '02:03:04', '03/03/2014',
=======
#!/usr/bin/python

import psycopg2
import datetime
from config import config



def insert_reservation(house, id, check_in_date, check_in_time, check_out_date, guest_name,
                       guest_cell, guest_telegram, num_guest, comment, confirm):
    """ insert a new reservation into the reservation table """
    sql = """INSERT INTO %s VALUES(%s, '%s', '%s', '%s', '%s', '%s', '%s', %s, '%s', %s) RETURNING reservation_id;"""
    conn = None
    reservation_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        print(sql % (house, id, check_in_date, check_in_time, check_out_date, guest_name,
                       guest_cell, guest_telegram, num_guest, comment, confirm))
        cur.execute(sql, (house, id, check_in_date, check_in_time, check_out_date, guest_name,
                       guest_cell, guest_telegram, num_guest, comment, confirm))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return reservation_id

insert_reservation('emerald', 121, '03/03/2014', '02:03:04', '03/03/2014',
>>>>>>> origin/master
                   'Jack of Blades', '+79150840000', 'noo', 2, 'quite room please', 'false')