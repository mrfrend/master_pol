import pymysql as psql
from dto.partners_dto import PartnerUpdateDto


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

    def execute_select(self, query, params=None):
        """Выполняет SELECT запрос и возвращает результаты"""
        with self.connection.cursor() as cur:
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            return cur.fetchall()

    def get_partner_types(self):
        """Получает все типы партнеров из таблицы partner_types"""
        query = "SELECT * FROM partners_type"
        with self.connection.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def update_partner(self, partners_info: PartnerUpdateDto):
        with self.connection.cursor() as cur:
            cur.callproc(
                "upd_partner",
                (
                    partners_info.partner_type_id,
                    partners_info.id,
                    partners_info.partner_name,
                    partners_info.first_name,
                    partners_info.last_name,
                    partners_info.middle_name,
                    partners_info.email,
                    partners_info.phone,
                    partners_info.address,
                    partners_info.inn,
                    partners_info.rating,
                ),
            )
            self.connection.commit()

    def get_disc(self, partner_name):
        """
        Получает скидку для партнера, вызывая функцию get_disc из БД
        """
        # Сначала получим ID партнера по его имени
        query = "SELECT id FROM partners WHERE partner_name = %s"
        with self.connection.cursor() as cur:
            cur.execute(query, (partner_name,))
            result = cur.fetchone()

            if not result:
                return 0

            # Вызываем функцию get_disc из БД
            query = "SELECT get_disc(%s) as discount"
            cur.execute(query, (result["id"],))
            discount_result = cur.fetchone()

            return discount_result["discount"] if discount_result else 0


db = None
try:
    db = Database(host="localhost", user="root", password="", db="master_pol")
    print("Database connection established.")
except psql.MySQLError as e:
    print(f"Error connecting to database: {e}")
