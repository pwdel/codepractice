#!/usr/bin/python

import psycopg2
import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE rpibatterydata (
            datapoint_id SERIAL PRIMARY KEY,
            battery_voltage NUMERIC NOT NULL,
            temperature NUMERIC NOT NULL,
            signal_strength NUMERIC NOT NULL,
            cpu_percent NUMERIC NOT NULL
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname='riobslkg' user='riobslkg' host='kashin.db.elephantsql.com' password='4JLeCneouzv2zA9p40L_xnnFZAj9rPAB'")
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