import mysql.connector


class MysqlDB:

    def __init__(self):
        self._mydb = None
        self._my_cursor = None

    def connect(self):
        self._mydb = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="sql9355624",
            password="pTjiIAFGGK",
            database="hackaton"
        )
        self._my_cursor = self._mydb.cursor()

    def close_connection(self):
        if self._mydb.is_connected():
            self._my_cursor.close()
            self._mydb.close()

    def get_all_users(self):
        user_list = []

        try:

            self.connect()
            user_select_query = "SELECT user_id, user_name, user_email, user_phone FROM users"
            self._my_cursor.execute(user_select_query)
            mysql_response_list = self._my_cursor.fetchall()
            for user in mysql_response_list:
                user_list.append({"user_id": user[0],
                                  "user_name": user[1],
                                  "user_email": user[2],
                                  "user_phone": user[3]})

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            self.close_connection()
            return user_list

    def get_email_list(self):
        email_string = ""

        try:
            self.connect()
            user_select_query = "SELECT user_email FROM users"
            self._my_cursor.execute(user_select_query)
            mysql_response_list = self._my_cursor.fetchall()
            for user in mysql_response_list:
                email_string += user[0] + "; "

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            self.close_connection()
            return email_string

    def set_user(self, user_data):
        try:
            user_tuple = (user_data['user_name'], user_data['user_email'], user_data['user_phone'],)
            self.connect()
            user_select_query = "INSERT INTO users (user_name, user_email, user_phone) VALUES (%s, %s, %s)"
            self._my_cursor.execute(user_select_query, user_tuple)
            self._mydb.commit()

        except mysql.connector.Error as error:
            print("Failed to insert record into MySQL table {}".format(error))

        finally:
            self.close_connection()


if __name__ == "__main__":
    user_dictionary = {"user_name": "John Doe",
                       "user_email": "johndoe@mail.com",
                       "user_phone": "555112233"}

    sql = MysqlDB()

    # sql.set_user(user_dictionary)
    print(sql.get_email_list())
