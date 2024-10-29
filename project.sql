use project;
create table user (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50) NOT NULL
);
CREATE TABLE doctor (
    doctorid VARCHAR(10) PRIMARY KEY,
    drname VARCHAR(50),
    specialisation VARCHAR(50),
    experienced INT,
    doctorsfee DECIMAL(10, 2),
    opd VARCHAR(10)
);
CREATE TABLE patient (
    name VARCHAR(50),
    bloodgroup VARCHAR(5),
    gender VARCHAR(10),
    dob DATE,
    opd VARCHAR(10) PRIMARY KEY,
    patienthistory TEXT,
    roomno VARCHAR(10)
);
CREATE TABLE appointment (
    doctorid VARCHAR(10),
    opd VARCHAR(10),
    sessionst TIME,
    sessionends TIME,
    gender VARCHAR(10),
    PRIMARY KEY (doctorid, opd),
    FOREIGN KEY (doctorid) REFERENCES doctor(doctorid),
    FOREIGN KEY (opd) REFERENCES patient(opd)
);
CREATE TABLE room (
    roomno VARCHAR(10) PRIMARY KEY,
    roomtype VARCHAR(20),
    roomcharges DECIMAL(10, 2)
);


