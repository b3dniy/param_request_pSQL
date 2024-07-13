---

# Parametric Request with PostgreSQL

## Overview

This project demonstrates how to use parametric requests with PostgreSQL databases using Python. The project includes scripts to create tables, perform parametric queries, and handle database configurations.

## Files

- `settings.ini`: Configuration file for database connection settings.
- `param_request.py`: Main script to perform parametric queries on the PostgreSQL database.
- `output.txt`: Output log file containing the results of executed queries.
- `create_tables.sql`: SQL script to create necessary tables in the PostgreSQL database.

## Repository

[GitHub Repository Link](https://github.com/b3dniy/param_request_pSQL)

## Usage

### Prerequisites

- Python 3.x
- PostgreSQL database
- Required Python packages (psycopg2 or any other as needed)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/b3dniy/param_request_pSQL.git
cd param_request_pSQL
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Configure the database settings in `settings.ini`:

```ini
[database]
host = your_host
port = your_port
dbname = your_dbname
user = your_username
password = your_password
```

### Database Setup

1. Execute the SQL script to create necessary tables:

```bash
psql -U your_username -d your_dbname -f create_tables.sql
```

### Running the Script

1. Run the parametric request script:

```bash
python param_request.py
```

This will perform parametric queries as defined in the script and output the results to the console and `output.txt`.

## Details

### settings.ini

This file contains the configuration settings for connecting to the PostgreSQL database. Update this file with your database credentials and connection details.

### param_request.py

This script handles the connection to the PostgreSQL database and performs parametric queries. It reads the configuration from `settings.ini` and executes the queries, outputting the results.

### output.txt

This file logs the output of the executed queries, including the number of clients and the results of specific email queries.

### create_tables.sql

This SQL script sets up the required tables in the PostgreSQL database. Ensure you run this script before executing the main parametric request script.

## Example Output

```plaintext
The number of clients:  4
(10, 'Andrey', 'Suchov', 'Andrey.Suchov@mail.com', datetime.date(2024, 6, 5)) 
(11, 'Andrey', 'Kozlov', 'andrey.kozlov@gmail.com', datetime.date(2024, 6, 5))
(12, 'Andrey', 'Suchov', 'Andrey.Suchov@mail.com', datetime.date(2024, 6, 5)) 
(13, 'Andrey', 'Kozlov', 'andrey.kozlov@gmail.com', datetime.date(2024, 6, 5))

Parametric request:

Clients with email Andrey.Suchov@mail.com:
(49, 'Andrey', 'Suchov', 'Andrey.Suchov@mail.com', datetime.date(2024, 6, 7))

Clients with email BHsbci.doidiaj@gmail.com:
(51, 'dfnasjkfna', 'sdASDJJDIJ', 'BHsbci.doidiaj@gmail.com', datetime.date(2024, 6, 7))

Clients with email andrey.kozlov@gmail.com:
(50, 'Andrey', 'Kozlov', 'andrey.kozlov@gmail.com', datetime.date(2024, 6, 7))
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---
