from mysql.connector import connect

from database.settings import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

class Database:
    
    def __init__(self):
        self.connection = connect(
            user = DB_USER,
            host = DB_HOST,
            database = DB_NAME,
            password = DB_PASSWORD
        )

    def select_all_from(self, table):
        query = f"SELECT * FROM {table}"

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        
        return result        

    def get_user(self, login, password):
        query = f"""
            SELECT * FROM users WHERE 
            `login` = '{login}' AND
            `password` = '{password}'
        """

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            user = cursor.fetchall()

        return user

    def delete_user(self, user_id):
        query = f"""
            DELETE FROM users WHERE `id` = {user_id}
        """

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

    def add_user(self, columns, values):
        query = f"""
            INSERT INTO users ({columns}) VALUES ({values})
        """       

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

    def clear_table(self, table_name):
        query = f"""
            DELETE * FROM {table_name}
        """

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

    def get_spends(self, user_id, category, date):
        query = f"""
            SELECT * FROM spends WHERE
            `user_id` = {user_id}
        """

        if(len(category) != 0):
            query = ' AND '.join((query, category))

        if(len(date) != 0):
            query = ' AND '.join((query, date))

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            spends = cursor.fetchall()

        return spends

    def add_spend(self, columns, values):
        query = f"""
            INSERT INTO spends ({columns}) VALUES ({values})
        """

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            self.connection.commit()

        print("its worked")