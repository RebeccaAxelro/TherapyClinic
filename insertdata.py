from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='raxelro1', password = 'rikikiki98', host = 'localhost', database='raxelro11')
cursor = cnx.cursor()

#---------------format of data------------------------------------------------
# insert data into table format
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

#---------------insert this data----------------------------------

# Insert client information                                              
data_client1 = (000001,'Judy Leon', '585 Orchard Avenue Brooklyn, NY 11207', 'jleon123@gmail.com', 3472009920)
data_client2 = (000002,'Kristi Glover', '94 Fieldstone Street Brooklyn, NY 11203', 'kglover123@gmail.com', 3472031686)
data_client3 = (000003,'Amelia Banks', '7985 Lookout Street Brooklyn, NY 11237', 'abanks123@gmail.com', 3472047816)
data_client4 = (000004,'Brittney Ferguson', '9 Rock Maple Street Brooklyn, NY 11221', 'bferguson123@gmail.com', 3472101447)

# Insert therapist information
data_therapist1 = (100001,'Lynsey Kline', 'lkline@pathsahead.com')
data_therapist2 = (100002,'Katie Rose', 'krose@pathsahead.com')
data_therapist3 = (100003,'Lara Carson', 'lcarson@pathsahead.com')

# Insert Diagnosed informatiom
data_diagnosed1 = (000001, 300.02)
data_diagnosed2 = (000002, 300.01)
data_diagnosed3 = (000003, 300.3)
data_diagnosed4 = (000004, 309.81)

# Insert Specializes information
data_specializes1 = (100001, 300.02)
data_specializes2 = (100002, 300.01)
data_specializes3 = (100003, 300.3)
data_specializes4 = (100004, 309.81)

# Insert disorder information
data_disorder1 = (300.02, 'Generalized Anxiety Disorder')
data_disorder2 = (300.01, 'Panic Disorder')
data_disorder3 = (300.3, 'Obsessive-Compulsive Disorder')
data_disorder4 = (309.81, 'Posttraumatic Stress Disorder')

# Insert treated information
data_treated1 = (000001, 200001)
data_treated2 = (000002, 200002)
data_treated3 = (000003, 200003)
data_treated4 = (000004, 200004)

# Insert treating information                                      
data_treating1 = (100001, 200001)
data_treating2 = (100001, 200002)
data_treating3 = (100002, 200003)
data_treating4 = (100003, 200004)

# Insert appointment information
data_appointment1 = (200001, 300001, 2019-05-06 14:30:00, 201, 45 min)
data_appointment2 = (200002, 300001, 2019-05-06 16:00:00, 201, 45 min)
data_appointment3 = (200003, 300002, 2019-05-07 13:30:00, 202, 45 min)
data_appointment4 = (200004, 300003, 2019-05-08 09:00:00, 203, 45 min)

# Insert treatment information
data_treatment1 = (300001, 'Cognitive Behavioral Therapy')
data_treatment2 = (300002, 'Exposure Response Prevention Therapy')
data_treatment3 = (300003, 'EMDR')

#------------------- Now Execute---------------------------------------------------

# Insert new cleint                                    
cursor.execute(add_client, data_client1)
cursor.execute(add_client, data_client2)
cursor.execute(add_client, data_client3)
cursor.execute(add_client, data_client4)


#Insert new therapist
cursor.execute(add_therapist, data_therapist1)
cursor.execute(add_therapist, data_therapist2)
cursor.execute(add_therapist, data_therapist3)

# Insert new diagnosed
cursor.execute(add_diagnosed, data_diagnosed1)
cursor.execute(add_diagnosed, data_diagnosed2)
cursor.execute(add_diagnosed, data_diagnosed3)
cursor.execute(add_diagnosed, data_diagnosed4)

# Insert new specializes
cursor.execute(add_specializes, data_specializes1)
cursor.execute(add_specializes, data_specializes2)
cursor.execute(add_specializes, data_specializes3)
cursor.execute(add_specializes, data_specializes4)

# Insert new disorder
cursor.execute(add_disorder, data_disorder1)
cursor.execute(add_disorder, data_disorder2)
cursor.execute(add_disorder, data_disorder3)
cursor.execute(add_disorder, data_disorder4)

# Insert new treated
cursor.execute(add_treated, data_treated1)
cursor.execute(add_treated, data_treated2)
cursor.execute(add_treated, data_treated3)
cursor.execute(add_treated, data_treated4)

# Insert new treating
cursor.execute(add_treating, data_treating1)
cursor.execute(add_treating, data_treating2)
cursor.execute(add_treating, data_treating3)
cursor.execute(add_treating, data_treating4)

# Insert new appointment
cursor.execute(add_appointment, data_appointment1)
cursor.execute(add_appointment, data_appointment2)
cursor.execute(add_appointment, data_appointment3)
cursor.execute(add_appointment, data_appointment)

# Insert new treatmenr
cursor.execute(add_treatment, data_treatment1)
cursor.execute(add_treatment, data_treatment2)
cursor.execute(add_treatment, data_treatment3)


# Make sure data is committed to the database     
cnx.commit()

cursor.close()
cnx.close()
