import psycopg2


def create_user(connection):
    cursor = connection.cursor()

    login = input("Enter login: ")
    password = input("Enter password: ")
    phone_num = input("Enter phone number: ")
    address = input("Enter address: ")
    favorite_category = input("Enter favorite category: ")

    cursor.execute(
        """
        INSERT INTO users
        (login, password, phone_num, address, favorite_category)
        VALUES (%s, %s, %s, %s, %s);
        """,
        (login, password, phone_num, address, favorite_category)
    )

    connection.commit()
    cursor.close()


def login_user(connection):
    cursor = connection.cursor()

    login = input("Enter login: ")
    password = input("Enter password: ")

    cursor.execute(
        """
        SELECT login, role
        FROM users
        WHERE login = %s AND password = %s;
        """,
        (login, password)
    )

    row = cursor.fetchone()

    if row:
        print("Login successful")
        print("Login =", row[0])
        print("Role =", row[1])
    else:
        print("Invalid login or password")

    cursor.close()


def view_profile(connection):
    cursor = connection.cursor()

    login = input("Enter login: ")

    cursor.execute(
        """
        SELECT login, phone_num, address, role, favorite_category
        FROM users
        WHERE login = %s;
        """,
        (login,)
    )

    row = cursor.fetchone()

    if row:
        print("Login =", row[0])
        print("Phone Number =", row[1])
        print("Address =", row[2])
        print("Role =", row[3])
        print("Favorite Category =", row[4])
    else:
        print("User not found")

    cursor.close()


def update_profile(connection):
    cursor = connection.cursor()

    login = input("Enter login: ")
    phone_num = input("Enter new phone number: ")
    address = input("Enter new address: ")
    favorite_category = input("Enter new favorite category: ")

    cursor.execute(
        """
        UPDATE users
        SET phone_num = %s,
            address = %s,
            favorite_category = %s
        WHERE login = %s;
        """,
        (phone_num, address, favorite_category, login)
    )

    connection.commit()
    cursor.close()