DROP DATABASE IF EXISTS Local_Library_Schema;

CREATE DATABASE Local_Library_Schema;

USE Local_Library_Schema;

CREATE TABLE MEMBERS(
    mb_id INT(8) PRIMARY KEY AUTO_INCREMENT,
    mb_fname VARCHAR(50) NOT NULL,
	mb_lname VARCHAR(50) NOT NULL,
    mb_age INT(3),
	mb_birthday DATE,
	mb_phone VARCHAR(13),
	mb_email VARCHAR(50),
	mb_national_id VARCHAR(13),
	mb_passport_id VARCHAR(8),
	mb_address VARCHAR(100)
);

CREATE TABLE AUTHOR(
    a_id INT(8) PRIMARY KEY AUTO_INCREMENT,
    a_fname VARCHAR(50) NOT NULL,
    a_lname VARCHAR(50)
);

CREATE TABLE PUBLISHER(
    p_id INT(8) PRIMARY KEY AUTO_INCREMENT,
    p_name VARCHAR(100) NOT NULL
);

CREATE TABLE BOOKS(
    b_id INT(8) PRIMARY KEY AUTO_INCREMENT,
    b_name VARCHAR(50) NOT NULL,
    b_desc VARCHAR(200),
    b_status BOOLEAN,
    a_id INT(8),
    FOREIGN KEY(a_id) REFERENCES AUTHOR(a_id),
    p_id INT(8),
    FOREIGN KEY(p_id) REFERENCES PUBLISHER(p_id)
);

CREATE TABLE LENDING(
    l_id INT(8) PRIMARY KEY AUTO_INCREMENT,
    l_start_date DATETIME NOT NULL,
    l_due_date DATE NOT NULL,
    l_return_date DATETIME,
    mb_id INT(8) NOT NULL,
    FOREIGN KEY(mb_id) REFERENCES MEMBERS(mb_id),
    b_id INT(8) NOT NULL,
    FOREIGN KEY(b_id) REFERENCES BOOKS(b_id)
);
