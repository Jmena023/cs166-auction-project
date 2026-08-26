import psycopg2


def create_item(connection):
    cursor = connection.cursor()

    item_id = input("Enter item ID: ")
    item_name = input("Enter item name: ")
    category = input("Enter category: ")
    starting_price = input("Enter starting price: ")
    image_url = input("Enter image URL (optional): ")
    item_condition = input("Enter item condition (optional): ")
    description = input("Enter description (optional): ")
    seller_login = input("Enter seller login: ")

    cursor.execute(
        """
        SELECT role
        FROM users
        WHERE login = %s;
        """,
        (seller_login,)
    )

    user = cursor.fetchone()

    if not user:
        print("User not found")
        cursor.close()
        return

    if user[0] != "Seller":
        print("Only sellers can create items")
        cursor.close()
        return

    cursor.execute(
        """
        INSERT INTO item
        (item_id, item_name, category, starting_price, image_url, item_condition, description, seller_login)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """,
        (item_id, item_name, category, starting_price, image_url, item_condition, description, seller_login)
    )

    connection.commit()

    print("Item created successfully")

    cursor.close()


def update_item(connection):
    cursor = connection.cursor()

    item_id = input("Enter item ID: ")
    seller_login = input("Enter your login: ")

    cursor.execute(
        """
        SELECT seller_login
        FROM item
        WHERE item_id = %s;
        """,
        (item_id,)
    )

    item = cursor.fetchone()

    if not item:
        print("Item not found")
        cursor.close()
        return

    if item[0] != seller_login:
        print("Only the seller who listed this item can update it")
        cursor.close()
        return

    item_name = input("Enter new item name: ")
    category = input("Enter new category: ")
    starting_price = input("Enter new starting price: ")
    image_url = input("Enter new image URL (optional): ")
    item_condition = input("Enter new item condition (optional): ")
    description = input("Enter new description (optional): ")

    cursor.execute(
        """
        UPDATE item
        SET item_name = %s,
            category = %s,
            starting_price = %s,
            image_url = %s,
            item_condition = %s,
            description = %s
        WHERE item_id = %s;
        """,
        (item_name, category, starting_price, image_url, item_condition, description, item_id)
    )

    connection.commit()

    print("Item updated successfully")

    cursor.close()


def view_item(connection):
    cursor = connection.cursor()

    item_id = input("Enter item ID: ")

    cursor.execute(
        """
        SELECT item_id, item_name, category, starting_price, image_url, item_condition, description, seller_login
        FROM item
        WHERE item_id = %s;
        """,
        (item_id,)
    )

    row = cursor.fetchone()

    if row:
        print("Item ID =", row[0])
        print("Item Name =", row[1])
        print("Category =", row[2])
        print("Starting Price =", row[3])
        print("Image URL =", row[4])
        print("Condition =", row[5])
        print("Description =", row[6])
        print("Seller =", row[7])
    else:
        print("Item not found")

    cursor.close()


def browse_items(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT item_id, item_name, category, starting_price, seller_login
        FROM item
        ORDER BY item_id;
        """
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("Item ID =", row[0])
            print("Item Name =", row[1])
            print("Category =", row[2])
            print("Starting Price =", row[3])
            print("Seller =", row[4])
            print()
    else:
        print("No items found")

    cursor.close()


def admin_remove_item(connection):
    cursor = connection.cursor()

    admin_login = input("Enter your admin login: ")
    item_id = input("Enter item ID to remove: ")

    cursor.execute(
        """
        SELECT role
        FROM users
        WHERE login = %s;
        """,
        (admin_login,)
    )

    admin = cursor.fetchone()

    if not admin or admin[0] != "Admin":
        print("Only admins can remove items")
        cursor.close()
        return

    cursor.execute(
        """
        DELETE FROM item
        WHERE item_id = %s;
        """,
        (item_id,)
    )

    connection.commit()

    print("Item removed successfully")

    cursor.close()