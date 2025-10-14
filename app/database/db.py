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

    def authorize_user(self, username, password):
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        with self.connection.cursor() as cur:
            cur.execute(query, (username, password))
            result = cur.fetchone()
            return result is not None


db = None
try:
    db = Database(host="localhost", user="root", password="", db="master_pol")
    print("Database connection established.")
except psql.MySQLError as e:
    print(f"Error connecting to database: {e}")
