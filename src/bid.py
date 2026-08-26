import psycopg2


def place_bid(connection):
    cursor = connection.cursor()

    bid_id = input("Enter bid ID: ")
    auction_id = input("Enter auction ID: ")
    buyer_login = input("Enter buyer login: ")
    bid_amount = input("Enter bid amount: ")

    cursor.execute(
        """
        SELECT seller_login, current_highest_bid, auction_status
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

    seller_login = auction[0]
    current_highest_bid = auction[1]
    auction_status = auction[2]

    if buyer_login == seller_login:
        print("Seller cannot bid on their own auction")
        cursor.close()
        return

    if auction_status != "Active":
        print("Auction is not active")
        cursor.close()
        return

    if float(bid_amount) <= float(current_highest_bid):
        print("Bid must be greater than the current highest bid")
        cursor.close()
        return

    cursor.execute(
        """
        INSERT INTO bid
        (bid_id, auction_id, buyer_login, bid_amount)
        VALUES (%s, %s, %s, %s);
        """,
        (bid_id, auction_id, buyer_login, bid_amount)
    )

    cursor.execute(
        """
        UPDATE auction
        SET current_highest_bid = %s
        WHERE auction_id = %s;
        """,
        (bid_amount, auction_id)
    )

    connection.commit()

    print("Bid placed successfully")

    cursor.close()


def view_auction_bids(connection):
    cursor = connection.cursor()

    auction_id = input("Enter auction ID: ")

    cursor.execute(
        """
        SELECT bid_id, buyer_login, bid_amount, bid_timestamp
        FROM bid
        WHERE auction_id = %s;
        """,
        (auction_id,)
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("Bid ID =", row[0])
            print("Buyer =", row[1])
            print("Bid Amount =", row[2])
            print("Bid Timestamp =", row[3])
            print()
    else:
        print("No bids found")

    cursor.close()


def view_user_bids(connection):
    cursor = connection.cursor()

    buyer_login = input("Enter buyer login: ")

    cursor.execute(
        """
        SELECT bid_id, auction_id, bid_amount, bid_timestamp
        FROM bid
        WHERE buyer_login = %s;
        """,
        (buyer_login,)
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("Bid ID =", row[0])
            print("Auction ID =", row[1])
            print("Bid Amount =", row[2])
            print("Bid Timestamp =", row[3])
            print()
    else:
        print("No bids found")

    cursor.close()