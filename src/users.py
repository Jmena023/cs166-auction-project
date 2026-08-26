import psycopg2


def create_user(connection):
    cursor = connection.cursor()

    login = input("Enter login: ")
    password = input("Enter password: ")
    phone_num = input("Enter phone number: ")
    address = input("Enter address: ")
    favorite_category = input("Enter favorite category: ")
    while True:
        role = input("Enter role (Buyer, Seller, or Admin): ").strip().capitalize()

        if role in ("Buyer", "Seller", "Admin"):
            break
        else:
            print("Invalid role. Please enter Buyer, Seller, or Admin.")

    cursor.execute(
        """
        INSERT INTO users
        (login, password, phone_num, address, favorite_category, role)
        VALUES (%s, %s, %s, %s, %s, %s);
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
        
        cursor.close()
        return row[0], row[1]
    else:
        print("Invalid login or password")

    cursor.close()
    return None, None


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

def update_user_role(connection):
    cursor = connection.cursor()

    admin_login = input("Enter admin login: ")
    user_login = input("Enter user login: ")
    new_role = input("Enter new role (Buyer, Seller, Admin): ")

    cursor.execute(
        """
        SELECT role
        FROM users
        WHERE login = %s;
        """,
        (admin_login,)
    )

    row = cursor.fetchone()

    if not row:
        print("Admin not found")
        cursor.close()
        return

    if row[0] != "Admin":
        print("Only an Admin can change roles")
        cursor.close()
        return

    cursor.execute(
        """
        UPDATE users
        SET role = %s
        WHERE login = %s;
        """,
        (new_role, user_login)
    )

    connection.commit()

    print("User role updated")

    cursor.close()