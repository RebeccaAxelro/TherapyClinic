CREATE TABLE client (
       clientID int(6) NOT NULL,
       name varchar(50),
       address varchar(100),
       email varchar(50),
       phoneNumber varchar(10),
       PRIMARY KEY (clientID)
);
CREATE TABLE therapist (
       therapistID int(6) NOT NULL,
       name varchar(50),
       email varchar(50),
       room_no varchar(20),
       PRIMARY KEY (therapistID)
);
CREATE TABLE disorder (
       disorderCode varchar(20) NOT NULL,
       disorderName varchar(100),
       PRIMARY KEY (disorderCode)
);
CREATE TABLE diagnosed (
       clientID int(6) NOT NULL,
       disorderCode varchar(20) NOT NULL,
       FOREIGN KEY (clientID) REFERENCES client (clientID),
       FOREIGN KEY (disorderCode) REFERENCES disorder (disorderCode)
);
CREATE TABLE specializes (
       therapistID int(6) NOT NULL,
       disorderCode varchar(20) NOT NULL,
       FOREIGN KEY (therapistID) REFERENCES therapist (therapistID),
       FOREIGN KEY (disorderCode) REFERENCES disorder (disorderCode)
);
CREATE TABLE treatment (
       treatmentID int(6) NOT NULL,
       treatmentName varchar(100),
       PRIMARY KEY (treatmentID)
);
CREATE TABLE appointment (
       appointmentID int(6) NOT NULL,
       clientID int(6) NOT NULL,
       therapistID int(6) NOT NULL, 
       treatmentID int(6) NOT NULL,
       date datetime,
       duration varchar(20),
       PRIMARY KEY (appointmentID),
       FOREIGN KEY (clientID) REFERENCES client (clientID),
       FOREIGN KEY (therapistID) REFERENCES therapist (therapistID),
       FOREIGN KEY (treatmentID) REFERENCES treatment (treatmentID)
);


/* command in mysql: source makeClinic.sql  

/*Insert the data from text files*/
LOAD DATA LOCAL INFILE 'client.txt'
into table client COLUMNS TERMINATED BY '|';
LOAD DATA LOCAL INFILE 'therapist.txt'
into table therapist COLUMNS TERMINATED BY '|';
LOAD DATA LOCAL INFILE 'disorder.txt'
into table disorder COLUMNS TERMINATED BY '|';
LOAD DATA LOCAL INFILE 'diagnosed.txt'
into table diagnosed COLUMNS TERMINATED BY '|';
LOAD DATA LOCAL INFILE 'specializes.txt'
into table specializes COLUMNS TERMINATED BY '|';
LOAD DATA LOCAL INFILE 'treatment.txt'
into table treatment COLUMNS TERMINATED BY '|';
LOAD DATA LOCAL INFILE 'appointment.txt'
into table appointment COLUMNS TERMINATED BY '|';
