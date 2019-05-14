from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'raxelro11'

TABLES = {}
TABLES['client'] = (
    "CREATE TABLE `client` ("
    "  `clientID` int(20) NOT NULL,"
    "  `name` varchar(50),"
    "  `address` varchar(100),"
    "  `email` varchar(50),"
    "  `phoneNumber' int(20),"
    "  PRIMARY KEY (`clientID`)"
    ") ENGINE=InnoDB")

TABLES['therapist'] = (
    "CREATE TABLE `therapist` ("
    "  `therapistID` int(20) NOT NULL,"
    "  `name` varchar(50),"
    "  `email` varchar(50),"
    "  PRIMARY KEY (`therapistID`)"
    ") ENGINE=InnoDB")

TABLES['diagnosed'] = (
    "CREATE TABLE `diagnosed` ("
    "  `clientID` int(20) NOT NULL,"
    "  `disorderCode` float(20,10) NOT NULL,"
    "  FOREIGN KEY (`clientID`) REFERENCES `cleint` (`clientID'),"
    "  FOREIGN KEY (`disorderCode`) REFERENCES `disorder` (`disorderCode')"
    ") ENGINE=InnoDB")

TABLES['specializes'] = (
    "CREATE TABLE `diagnosed` ("
    "  `therapistID` int(20) NOT NULL,"
    "  `disorderCode` float(20,10) NOT NULL,"
    "  FOREIGN KEY (`therapistID`) REFERENCES `therapist` (`therapistID'),"
    "  FOREIGN KEY (`disorderCode`) REFERENCES `disorder` (`disorderCode')"
    ") ENGINE=InnoDB")

TABLES['disorder'] = (
    "  CREATE TABLE `disorder` ("
    "  `disorderCode` float(20,10) NOT NULL,"
    "  `disorderName` varchar(100),"
    "  PRIMARY KEY (`disorderCode`)"
    ") ENGINE=InnoDB")

TABLES['treated'] = (
    "CREATE TABLE `treated` ("
    "  `clientID` int(20) NOT NULL,"
    "  `appointmentID` int(20) NOT NULL,"
    "  FOREIGN KEY (`clientID`) REFERENCES `cleint` (`clientID'),"
    "  FOREIGN KEY (`appointmentID`) REFERENCES `appointment` (`appointmentID')"
    ") ENGINE=InnoDB")

TABLES['treating'] = (
    "CREATE TABLE `treating` ("
    "  `therapistID` int(20) NOT NULL,"
    "  `appointmentID` int(20) NOT NULL,"
    "  FOREIGN KEY (`therapistID`) REFERENCES `therapist` (`therapistID'),"
    "  FOREIGN KEY (`appointmentID`) REFERENCES `appointment` (`appointmentID'\
)"
    ") ENGINE=InnoDB")

TABLES['appointment'] = (
    "  CREATE TABLE `appointment` ("
    "  `appointmentID` int(20) NOT NULL,"
    "  `treatmentID` int(20) NOT NULL,"
    "  `date` datetime,"
    "  `room_no` varchar(20),"
    "  `duration` varchar(20),"
    "  PRIMARY KEY (`appointmentID`),"
    "  PRIMARY KEY (`treatmentID`)"
    ") ENGINE=InnoDB")

TABLES['treatment'] = (
    "  CREATE TABLE `treatment` ("
    "  `treatmentID` int(20) NOT NULL,"
    "  `treatmentName` varchar(100),"
    "  PRIMARY KEY (`treatmentID`)"
    ") ENGINE=InnoDB")

##----------------------
cnx = mysql.connector.connect(user='raxelro1', password='rikikiki98', host = 'lo\
calhost')
cursor = cnx.cursor()

##---------------------------
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

##----------------------                                                         

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()

##---------------
# Normal form
# My tables are 4th normal form
# Because:
# 1) In first normal form:
# a) each cell in singled valued
# b) entries in a column are same type
# c) rows uniquely identified
# 2) In second normal form:
# a) all attributes dependent on the key - theyre seperated, with then connecting them in another table
# 3) In third normal form:
# a) all fields can be determined only by the key in the table and no other column
# 4) In forth normal form:
# a) no multi-valued dependencies
# --  For a single value A , there are not mulitple values of B
# ex: Every table, is unique in their value becuase there are table to split them up. You will only see a unique client in client table, a unique treamtment in treatment tbale, etc.
