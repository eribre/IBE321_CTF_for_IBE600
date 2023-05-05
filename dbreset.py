import sqlite3
import os
from dbconnection import Database

# A script to reset the database to its original state

path = "./user_db.db"

if os.path.isfile(path):
    os.remove("user_db.db")

with Database() as db:
    create = db(
        """CREATE TABLE users(id INTEGER PRIMARY KEY,
 		name TEXT NOT NULL, password TEXT NOT NULL, UNIQUE(name, password));"""
    )
    insert = db(
        """INSERT INTO users(name, password)
 				VALUES('admin', 'admin1'), ('secUsr', 'blowfish'),
	 			('root', 'root1'), ('Roger', 'Password1'), ('Jonathan', '12345');"""
    )
    # print("test")


# TODO: Make this run every 10-15 minutes
