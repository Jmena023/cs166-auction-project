import psycopg2


def create_shipment(connection):
    cursor = connection.cursor()

    shipment_id = input("Enter shipment ID: ")
    auction_id = input("Enter auction ID: ")
    address = input("Enter shipping address: ")

    cursor.execute(
        """
        SELECT payment_status
        FROM payment
        WHERE auction_id = %s;
        """,
        (auction_id,)
    )

    payment = cursor.fetchone()

    if not payment:
        print("No payment found for this auction")
        cursor.close()
        return

    if payment[0] != "Completed":
        print("Payment must be completed before creating a shipment")
        cursor.close()
        return

    cursor.execute(
        """
        INSERT INTO shipment
        (shipment_id, auction_id, address)
        VALUES (%s, %s, %s);
        """,
        (shipment_id, auction_id, address)
    )

    connection.commit()

    print("Shipment created successfully")

    cursor.close()


def view_shipment(connection):
    cursor = connection.cursor()

    shipment_id = input("Enter shipment ID: ")

    cursor.execute(
        """
        SELECT shipment_id, auction_id, address, shipment_status, tracking_number
        FROM shipment
        WHERE shipment_id = %s;
        """,
        (shipment_id,)
    )

    row = cursor.fetchone()

    if row:
        print("Shipment ID =", row[0])
        print("Auction ID =", row[1])
        print("Address =", row[2])
        print("Shipment Status =", row[3])
        print("Tracking Number =", row[4])
    else:
        print("Shipment not found")

    cursor.close()


def update_shipment_status(connection):
    cursor = connection.cursor()

    shipment_id = input("Enter shipment ID: ")
    shipment_status = input("Enter new shipment status (Pending/Shipped/Delivered): ")
    tracking_number = input("Enter tracking number (optional): ")

    cursor.execute(
        """
        UPDATE shipment
        SET shipment_status = %s,
            tracking_number = %s
        WHERE shipment_id = %s;
        """,
        (shipment_status, tracking_number, shipment_id)
    )

    connection.commit()

    print("Shipment status updated")

    cursor.close()