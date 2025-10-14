import pymysql as psql


class Database:
    def __init__(self, host, user, password, db):
        self.connection = psql.connect(
            host=host,
            user=user,
            password=password,
            database=db,
            cursorclass=psql.cursors.DictCursor,
        )
        self.cursor = self.connection.cursor()


db = None
try:
    db = Database(host="localhost", user="root", password="", db="master_pol")
    print("Database connection established.")
except psql.MySQLError as e:
    print(f"Error connecting to database: {e}")
