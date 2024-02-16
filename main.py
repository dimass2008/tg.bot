import sqlite3

class Database:
    def init(self) -> None:
        self.conn = sqlite3.connect("base.db", check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_users(self, user_id):
        self.cursor.execute(f"SELECT user_name FROM table WHERE id={user_id}")
        return self.cursor.fetchone()[0]

    def register(self, user_id, user_name):
        self.conn = sqlite3.connect("base.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"INSERT INTO table (id, user_name) VALUES (?, ?)", (user_id, user_name))
        self.conn.commit()
        return True

    def update_balance(self, id, balance, status):
        """
        status = True - add balance
        status = False - take balance
        """
        if status:
            self.cursor.execute(f"UPDATE table SET balance=balance+? WHERE id=?", (balance, id))
        else:
            self.cursor.execute(f"UPDATE table SET balance=balance-? WHERE id=?", (balance, id))
        self.conn.commit()
        self.cursor.execute("SELECT balance FROM table WHERE id=?", (id,))
        updated_balance = self.cursor.fetchone()[0]
        return updated_balance