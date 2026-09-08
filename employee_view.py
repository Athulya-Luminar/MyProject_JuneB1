import mysql.connector

class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Athulya@2907",
                database="gym_db_b1"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(DbConnect):
    pass


connection_instance = DbConnect()
connection_instance.get_connection()