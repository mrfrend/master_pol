import pymysql as pms
from pymysql import cursors

class Database:
    def __init__(self, host, user, password, db):
        self.connection = pms.connect(
            host=host,
            user=user,
            password=password,
            database=db,
            cursorclass=pms.cursors.DictCursor,
        )

    def authorize_user(self, login, password):
        query="SELECT * FROM users WHERE username=%s AND password=%s"
        with self.connection.cursor() as cur:
            cur.execute(query, (login, password))
            result = cur.fetchone()
            return result is not None


db = Database(host="localhost", user="root", password="", db="master_pol")

