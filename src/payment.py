import psycopg2


def make_payment(connection):
    cursor = connection.cursor()

    payment_id = input("Enter payment ID: ")
    auction_id = input("Enter auction ID: ")
    buyer_login = input("Enter buyer login: ")
    amount = input("Enter payment amount: ")

    cursor.execute(
        """
        SELECT winner_login, auction_status
        FROM auction
        WHERE auction_id = %s;
        """,
        (auction_id,)
    )

    auction = cursor.fetchone()

    if not auction:
        print("Auction not found")
        cursor.close()
        return

    winner_login = auction[0]
    auction_status = auction[1]

    if auction_status != "Closed":
        print("Auction is not closed")
        cursor.close()
        return

    if buyer_login != winner_login:
        print("Only the winning buyer can make the payment")
        cursor.close()
        return

    cursor.execute(
        """
        INSERT INTO payment
        (payment_id, auction_id, buyer_login, amount)
        VALUES (%s, %s, %s, %s);
        """,
        (payment_id, auction_id, buyer_login, amount)
    )

    connection.commit()

    print("Payment created successfully")

    cursor.close()


def view_payment(connection):
    cursor = connection.cursor()

    payment_id = input("Enter payment ID: ")

    cursor.execute(
        """
        SELECT payment_id, auction_id, buyer_login, amount, payment_status
        FROM payment
        WHERE payment_id = %s;
        """,
        (payment_id,)
    )

    row = cursor.fetchone()

    if row:
        print("Payment ID =", row[0])
        print("Auction ID =", row[1])
        print("Buyer =", row[2])
        print("Amount =", row[3])
        print("Payment Status =", row[4])
    else:
        print("Payment not found")

    cursor.close()


def view_user_payments(connection):
    cursor = connection.cursor()

    buyer_login = input("Enter buyer login: ")

    cursor.execute(
        """
        SELECT payment_id, auction_id, amount, payment_status
        FROM payment
        WHERE buyer_login = %s;
        """,
        (buyer_login,)
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("Payment ID =", row[0])
            print("Auction ID =", row[1])
            print("Amount =", row[2])
            print("Payment Status =", row[3])
            print()
    else:
        print("No payments found")

    cursor.close()


def update_payment_status(connection):
    cursor = connection.cursor()

    buyer_login = input("Enter your login: ")
    payment_id = input("Enter payment ID: ")
    auction_id = input("Enter auction ID: ")

    cursor.execute(
        """
        SELECT buyer_login
        FROM payment
        WHERE payment_id = %s
          AND auction_id = %s;
        """,
        (payment_id, auction_id)
    )

    payment = cursor.fetchone()

    if not payment:
        print("Payment not found for that payment ID and auction ID")
        cursor.close()
        return

    if payment[0] != buyer_login:
        print("Only the buyer who made this payment can update its status")
        cursor.close()
        return

    payment_status = input("Enter new payment status (Pending/Completed/Failed): ")

    cursor.execute(
        """
        UPDATE payment
        SET payment_status = %s
        WHERE payment_id = %s;
        """,
        (payment_status, payment_id)
    )

    connection.commit()

    print("Payment status updated")

    cursor.close()