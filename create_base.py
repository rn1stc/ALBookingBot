#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE emerald (
            reservation_id SERIAL PRIMARY KEY,
            check_in_date DATE NOT NULL,
            check_in_time TIME,
            check_out_date DATE NOT NULL,
            guest_name VARCHAR(255) NOT NULL,
            guest_cell VARCHAR(16) NOT NULL,
            guest_telegram VARCHAR(255),
            num_guest SMALLINT,
            comment VARCHAR(255),
            confirm BOOLEAN NOT NULL
        )
        ""","""
        CREATE TABLE amethyst (
            reservation_id SERIAL PRIMARY KEY,
            check_in_date DATE NOT NULL,
            check_in_time TIME,
            check_out_date DATE NOT NULL,
            guest_name VARCHAR(255) NOT NULL,
            guest_cell VARCHAR(16) NOT NULL,
            guest_telegram VARCHAR(255),
            num_guest SMALLINT,
            comment VARCHAR(255),
            confirm BOOLEAN NOT NULL
        )
        ""","""
        CREATE TABLE lazurite (
            reservation_id SERIAL PRIMARY KEY,
            check_in_date DATE NOT NULL,
            check_in_time TIME,
            check_out_date DATE NOT NULL,
            guest_name VARCHAR(255) NOT NULL,
            guest_cell VARCHAR(16) NOT NULL,
            guest_telegram VARCHAR(255),
            num_guest SMALLINT,
            comment VARCHAR(255),
            confirm BOOLEAN NOT NULL
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()