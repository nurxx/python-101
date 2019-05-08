import sqlite3

def create_users_table():
    connection=sqlite3.connect('business_cards.db')
    cursor=connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Users(
            id INTEGER  PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR(100) NOT NULL,
            email VARCHAR(30) NOT NULL,
            age INTEGER NOT NULL,
            phone VARCHAR(20) NOT NULL,
            additional_info TEXT
            );"""
            )
    connection.commit()
    connection.close()
# 
# 
def add(full_name,email,age,phone,additional_info):
    connection=sqlite3.connect('business_cards.db')
    cursor=connection.cursor()
    cursor.execute(
        """INSERT INTO Users(full_name,email,age,phone,additional_info)
            VALUES('{name}','{email}',{age},'{phone}','{additional_info}')
            """.format(name=full_name,email=email,age=age,phone=phone,additional_info=additional_info)
            )
    connection.commit()
    connection.close()

def list():
    connection=sqlite3.connect('business_cards.db')
    cursor=connection.cursor()
    cursor.execute(
        """
        SELECT *
        FROM Users
        """
        )
    users=cursor.fetchall()
    connection.commit()
    connection.close()
    return users

def get(user_id):
    connection=sqlite3.connect('business_cards.db')
    cursor=connection.cursor()
    cursor.execute(
        """
        SELECT *
        FROM Users
        WHERE id={id}
        """.format(id=user_id)
        )
    user=cursor.fetchone()
    connection.commit()
    connection.close()
    
    return user

def delete(user_id):
    connection=sqlite3.connect('business_cards.db')
    cursor=connection.cursor()
    cursor.execute(
        """
        DELETE FROM Users
        WHERE id={id};
        """.format(id=user_id)
        )
    connection.commit()
    connection.close()

def help():
    options = """
    1. `add` - insert new business card
    2. `list` - list all business cards
    3. `delete` - delete a certain business card (`ID` is required)
    4. `get` - display full information for a certain business card (`ID` is required)
    5. `help` - list all available options
    6. `exit` - close program
    """
    return options

