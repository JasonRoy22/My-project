
-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'my_irxrace' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS my_irxrace;
CREATE DATABASE my_irxrace;
-- connect via psql
\c my_irxrace

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;






-- CREATE TABLES --

CREATE TABLE drivers (
    id SERIAL,
    name TEXT NOT NULL UNIQUE,
    email_address TEXT UNIQUE,
    password TEXT NOT NULL,
    driver_id INT,
    car_id INT,
    PRIMARY KEY (id)
);

CREATE TABLE cars (
    id SERIAL,
    license CHAR(1) NOT NULL,
    year INT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    car_id INT,
    driver_id INT,
    PRIMARY KEY (id)
);

CREATE TABLE races (
    id SERIAL,
    starting_position INT NOT NULL UNIQUE,
    ending_position INT NOT NULL UNIQUE,
    qualifying_time INT,
    average_lap_times INT NOT NULL,
    best_lap_times INT NOT NULL,
    race_id INT,
    car_id INT,
    PRIMARY KEY (id)
);

CREATE TABLE incident (
    id SERIAL,
    cars_involved INT NOT NULL,
    number_of_incidents INT NOT NULL,
    race_id INT,
    PRIMARY KEY (id)
);

-- ADD CONSTRAINTS --

ALTER TABLE drivers
ADD CONSTRAINT fk_drivers_cars
FOREIGN KEY (car_id)
REFERENCES cars (id);

ALTER TABLE cars
ADD CONSTRAINT fk_cars_drivers
FOREIGN KEY (driver_id)
REFERENCES drivers (id);

ALTER TABLE races
ADD CONSTRAINT fk_cars_races
FOREIGN KEY (car_id)
REFERENCES cars (id);

ALTER TABLE incident
ADD CONSTRAINT fk_race_incident
FOREIGN KEY (race_id)
REFERENCES races (id);