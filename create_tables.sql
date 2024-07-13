DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS computers;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS software;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS events;

CREATE TABLE IF NOT EXISTS clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    registration_date DATE
);

CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    position VARCHAR(50),
    hire_date DATE
);

CREATE TABLE IF NOT EXISTS computers (
    computer_id SERIAL PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50),
    purchase_date DATE
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    client_id INT REFERENCES clients(client_id),
    employee_id INT REFERENCES employees(employee_id),
    computer_id INT REFERENCES computers(computer_id),
    transaction_date DATE,
    transaction_type VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS software (
    software_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    version VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS classes (
    class_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    instructor_id INT REFERENCES employees(employee_id),
    schedule TIMESTAMP
);

CREATE TABLE IF NOT EXISTS equipment (
    equipment_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

CREATE TABLE IF NOT EXISTS events (
    event_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    organizer_id INT REFERENCES employees(employee_id),
    event_date DATE
);
