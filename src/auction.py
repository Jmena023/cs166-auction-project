import psycopg2


def create_auction(connection):
    cursor = connection.cursor()

    auction_id = input("Enter auction ID: ")
    item_id = input("Enter item ID: ")
    seller_login = input("Enter seller login: ")

    cursor.execute(
        """
        SELECT seller_login, starting_price
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
        print("Only the seller who listed this item can create an auction for it")
        cursor.close()
        return

    starting_price = item[1]

    cursor.execute(
        """
        INSERT INTO auction
        (auction_id, item_id, seller_login, current_highest_bid)
        VALUES (%s, %s, %s, %s);
        """,
        (auction_id, item_id, seller_login, starting_price)
    )

    connection.commit()

    print("Auction created successfully")

    cursor.close()


def browse_auctions(connection):
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT a.auction_id, i.item_name, i.category, a.current_highest_bid, a.auction_status
        FROM auction a
        JOIN item i ON a.item_id = i.item_id
        WHERE a.auction_status = 'Active'
        ORDER BY a.auction_id;
        """
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("Auction ID =", row[0])
            print("Item Name =", row[1])
            print("Category =", row[2])
            print("Current Highest Bid =", row[3])
            print("Status =", row[4])
            print()
    else:
        print("No active auctions found")

    cursor.close()


def search_auctions(connection):
    cursor = connection.cursor()

    category = input("Enter category to search: ")

    cursor.execute(
        """
        SELECT a.auction_id, i.item_name, i.category, a.current_highest_bid, a.auction_status
        FROM auction a
        JOIN item i ON a.item_id = i.item_id
        WHERE i.category = %s
        ORDER BY a.auction_id;
        """,
        (category,)
    )

    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("Auction ID =", row[0])
            print("Item Name =", row[1])
            print("Category =", row[2])
            print("Current Highest Bid =", row[3])
            print("Status =", row[4])
            print()
    else:
        print("No auctions found in that category")

    cursor.close()


def end_auction(connection):
    cursor = connection.cursor()

    auction_id = input("Enter auction ID: ")
    seller_login = input("Enter your login: ")

    cursor.execute(
        """
        SELECT seller_login, auction_status
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

    if auction[0] != seller_login:
        print("Only the seller who created this auction can end it")
        cursor.close()
        return

    if auction[1] != "Active":
        print("Auction is already closed")
        cursor.close()
        return

    cursor.execute(
        """
        SELECT buyer_login
        FROM bid
        WHERE auction_id = %s
        ORDER BY bid_amount DESC
        LIMIT 1;
        """,
        (auction_id,)
    )

    top_bid = cursor.fetchone()
    winner_login = top_bid[0] if top_bid else None

    cursor.execute(
        """
        UPDATE auction
        SET auction_status = 'Closed',
            winner_login = %s
        WHERE auction_id = %s;
        """,
        (winner_login, auction_id)
    )

    connection.commit()

    if winner_login:
        print("Auction closed. Winner =", winner_login)
    else:
        print("Auction closed. No bids were placed.")

    cursor.close()