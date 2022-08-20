from settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from mysql.connector import connect

users_table_rows = [
    "('admin', 'admin', 'admin')",
    "('user', '123', 'default')"
]

spends_table_rows = [
    "('food', '1', '200', '2022-08-20')",
    "('food', '1', '350', '2022-08-19')",
    "('food', '1', '444', '2022-07-18')",
    "('food', '2', '110', '2022-07-20')",
    "('food', '2', '150', '2022-08-20')",
    "('food', '2', '777', '2022-08-19')",
    "('sport', '1', '400', '2022-07-15')",
    "('sport', '1', '610', '2022-08-19')",
    "('sport', '1', '160', '2022-08-20')",
    "('sport', '2', '133', '2022-08-18')",
    "('sport', '2', '50', '2022-08-19')",
    "('sport', '2', '400', '2022-08-20')",
    "('health', '1', '450', '2022-07-20')",
    "('health', '1', '190', '2022-07-15')",
    "('health', '1', '570', '2022-08-20')",
    "('health', '2', '500', '2022-07-19')",
    "('health', '2', '770', '2022-07-20')",
    "('health', '2', '420', '2022-08-20')",
]


with connect(
    user = DB_USER,
    host = DB_HOST,
    password = DB_PASSWORD
) as connection:
    cursor = connection.cursor()

    cursor.execute(f"CREATE DATABASE {DB_NAME}")

# reconnect with specified database name
with connect(
    user = DB_USER,
    host = DB_HOST,
    password = DB_PASSWORD,
    database = DB_NAME
) as connection:
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE users (
            id int not null auto_increment,
            login varchar(63) not null,
            password varchar(63) not null,
            status varchar(10) not null,
            PRIMARY KEY(id),
            UNIQUE(login)
        )"""
    )

    cursor.execute(
        """CREATE TABLE spends (
            id int not null auto_increment,
            category varchar(63) not null,
            user_id int not null,
            spends int not null,
            date date not null,
            PRIMARY KEY(id),
            FOREIGN KEY(user_id) REFERENCES users(id)
        )"""
    )

    for row in users_table_rows:
        cursor.execute(f"""
            INSERT INTO users
            (`login`, `password`, `status`)
            VALUES {row}
        """)
        connection.commit()

    for row in spends_table_rows:
        cursor.execute(f"""
            INSERT INTO spends
            (`category`, `user_id`, `spends`, `date`)
            VALUES {row}
        """)
        connection.commit()