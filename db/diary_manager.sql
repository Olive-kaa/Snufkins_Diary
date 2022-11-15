DROP TABLE IF EXISTS bagged_munros;
DROP TABLE IF EXISTS munros;
DROP TABLE IF EXISTS regions;
DROP TABLE IF EXISTS hikers;


CREATE TABLE regions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE munros (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    region_id INT REFERENCES regions(id),
    altitude INT
);

CREATE TABLE hikers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE bagged_munros (
    id SERIAL PRIMARY KEY,
    hiker_id INT REFERENCES hikers(id),
    munro_id INT REFERENCES munros(id),
    date_bagged DATE NOT NULL
);
