import pymysql as pms
from pymysql import cursors
from dto.partner_card_info import PartnerAddDTO, PartnerUpdateDTO


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
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        with self.connection.cursor() as cur:
            cur.execute(query, (login, password))
            result = cur.fetchone()
            return result is not None

    def show_partners(self):
        with self.connection.cursor() as cur:
            cur.execute("SELECT * FROM show_partners")
            result = cur.fetchall()
            return result

    def get_disc(self, partner_id: int):
        with self.connection.cursor() as cur:
            cur.execute("SELECT get_disc(%s)", (partner_id,))
            result = cur.fetchone()  # {"get_disc(4)": 15}
            return result.get(f"get_disc({partner_id})")

    def get_partners_types(self):
        with self.connection.cursor() as cur:
            cur.execute("SELECT id, name from partners_type")
            result = cur.fetchall()
            return result

    def delete_partner(self, partner_id: int):
        with self.connection.cursor() as cur:
            cur.execute("DELETE FROM partners WHERE id = %s", (partner_id,))
            self.connection.commit()
            return

    def update_partner(self, partner_info: PartnerUpdateDTO):
        with self.connection.cursor() as cur:
            cur.callproc(
                "upd_partner",
                (
                    partner_info.type_id,
                    partner_info.id,
                    partner_info.partner_name,
                    partner_info.first_name,
                    partner_info.last_name,
                    partner_info.middle_name,
                    partner_info.email,
                    partner_info.phone_partner,
                    partner_info.address,
                    partner_info.inn_number,
                    partner_info.rating,
                ),
            )
            self.connection.commit()
            return

    def insert_partner(self, partner_info: PartnerAddDTO):
        with self.connection.cursor() as cur:
            cur.callproc(
                "add_parther",
                (
                    partner_info.type_id,
                    partner_info.partner_name,
                    partner_info.first_name,
                    partner_info.last_name,
                    partner_info.middle_name,
                    partner_info.email,
                    partner_info.phone_partner,
                    partner_info.address,
                    partner_info.inn_number,
                    partner_info.rating,
                ),
            )
            self.connection.commit()
            return


db = Database(host="localhost", user="root", password="", db="master_pol")
