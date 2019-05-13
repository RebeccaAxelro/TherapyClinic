from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='raxelro1', password = 'rikikiki98', host = '\
localhost', database='raxelro11')
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_client = ("INSERT INTO client "
               "(clientID, name, address, email, phoneNumber) "
               "VALUES (%s, %s, %s, %s, %s)")
add_therapist = ("INSERT INTO therapist "
               "(therapistID, name, email) "
               "VALUES (%s, %s, %s)")
add_diagnosed = ("INSERT INTO diagnosed "
               "(clientID, disorderCode) "
                 "VALUES (%s, %s)")
add_specializes = ("INSERT INTO specializes "
               "(therapistID, disorderCode) "
                 "VALUES (%s, %s)")   
add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%s, %s, %s, %s)")
add_disorder = ("INSERT INTO disorder "
                "(disorderCode, disorderName) "
                 "VALUES (%s, %s)")
add_treated = ("INSERT INTO treated "
               "(clientID, appointmentID) "
                 "VALUES (%s, %s)")
add_treating = ("INSERT INTO treating "
               "(therapistID, appointmentID) "
                 "VALUES (%s, %s)")
add_appointment = ("INSERT INTO appointment "
                   "(appointmentID, treatmentID, date, room_no, duration) "
                   "VALUES (%s, %s, %s, %s, %s)")
add_treatment = ("INSERT INTO treatment "
               "(treatmentID, treatmentName) "
                 "VALUES (%s, %s)")



# Insert client information                                              
data_client = {000001,'Judy Leon', '585 Orchard Avenue Brooklyn, NY 11207', 'jleon123@gmail.com', '347-200-9920'))
}

# didnt have a chance to insert evrything, but look at sampleData.txt

# Insert new cleint                                    
cursor.execute(add_client, data_client)

# Make sure data is committed to the database                                    
cnx.commit()

cursor.close()
cnx.close()
